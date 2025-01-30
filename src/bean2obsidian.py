from copy import deepcopy
from pathlib import Path
from typing import Optional
from ures.markdown import Zettelkasten
from .bean_conqueror import BeanConquerorParser, Bean, BeanVariety, Mill, Brew


class Bean2Obsidian:
    def __init__(
        self,
        bean_file: str,
        obsidian_folder: str,
        bean_conqueror_folder: Optional[str] = None,
    ):
        if bean_conqueror_folder is None:
            bean_conqueror_folder = Path(bean_file).parent
        self.bean_conqueror_folder = Path(bean_conqueror_folder)
        self.bean_file = Path(bean_file)
        self.bean_data = BeanConquerorParser(bean_file)
        self.obsidian_folder = Path(obsidian_folder)
        self.coffee_folder = self.obsidian_folder.joinpath(
            "002-literature", "004-coffee"
        )
        self.tag_prefix = "life/☕coffee"

    def _insert_attachment(self, note: Zettelkasten, attachment: list):
        """Insert attachment to the note if it exists

        Args:
            note (Zettelkasten): A note object
            attachment (list): A list of attachments that are relevant path to BeanConqueror data directory

        """
        if len(attachment) > 0:
            note.set_frontmatter("banner", attachment[0])

    def compress_image(self, image_path, output_path):
        from PIL import Image

        img = Image.open(image_path).convert("RGB")
        img.save(output_path, "webp", lossless=False, quality=40)

    def mills(self):
        mill_notes = []
        mill_path = self.coffee_folder.joinpath("001-equipment", "001-grinder")
        if mill_path.is_dir() is False:
            mill_path.mkdir(parents=True, exist_ok=True)
        for mill in self.bean_data.mills.mills:
            mill_note = Zettelkasten(
                title=f"Coffee Grinder - {mill.name}",
                n_type="literature",
                url="",
            )
            note_path = mill_path.joinpath(f"{mill_note.title}.md")
            mill_note.add_tag(f"{self.tag_prefix}/equipment/grinder")
            mill_note.set_frontmatter("year", mill.timestamp)
            mill_note.add_alias(mill.uuid)
            self._insert_attachment(mill_note, mill.attachments)

            mill_notes.append({"note": mill_note, "path": note_path})
        return mill_notes

    def beans(self):
        bean_notes = []
        bean_path = self.coffee_folder.joinpath("002-beans")
        for name, bean in self.bean_data.beans.beans.items():
            bean_note = Zettelkasten(
                title=f"Coffee Beans - {bean['roaster']} - {bean['name']}",
                n_type="literature",
                url="",
            )
            example_bean_object: Bean = bean["history"][0]
            product_path = bean_path.joinpath(
                example_bean_object.roaster, example_bean_object.name
            )
            note_path = product_path.joinpath(f"{bean_note.title}.md")
            bean_note.add_alias(bean_note.get_frontmatter("id"))
            bean_note.set_frontmatter("coffeeBeanDecaf", example_bean_object.decaf)
            bean_note.set_frontmatter(
                "coffeeIsSingleOrigin", example_bean_object.is_single_origin()
            )
            bean_note.set_frontmatter(
                "coffeeBeanAromatics", example_bean_object.aromatics
            )
            bean_note.set_frontmatter(
                "coffeeBeanRoastLevel", example_bean_object.roasting_level
            )
            bean_note.set_frontmatter("coffeeBeanProcess", bean["process"])
            bean_note.set_frontmatter("coffeeBeanVariety", bean["varieties"])
            self._insert_attachment(bean_note, example_bean_object.attachments)

            for process in bean.get("process", []):
                tag = f"{self.tag_prefix}/beans/process/{process}"
                bean_note.add_tag(tag)
            for variety in bean.get("varieties", []):
                tag = f"{self.tag_prefix}/beans/variety/{variety}"
                bean_note.add_tag(tag)
            for aroma in bean.get("aromatics", []):
                tag = f"{self.tag_prefix}/beans/aromatics/{aroma}"
                bean_note.add_tag(tag)

            bean_note.add_content("## ☕Brews Records", append=True)
            bean_note.add_content(
                '`$=await dv.view("902-template/002-dataview/coffeeBeanView", {})`'
            )
            bean_notes.append({"note": bean_note, "path": note_path})

            # Start process history purchase
            record_path = product_path.joinpath("history")
            if record_path.is_dir() is False:
                record_path.mkdir(parents=True, exist_ok=True)
            for history in bean.get("history", []):
                history_note = Zettelkasten(
                    title=f"Coffee Purchase Record - {history.uuid}",
                    n_type="literature",
                    url="",
                )
                history_note.add_alias(history.uuid)
                history_note.set_frontmatter(
                    "price",
                    f"£{round((float(history.price)/float(history.weight))*100, 2)}/100g",
                )
                history_note.set_frontmatter("coffeeRoastDate", history.roasting_date)
                history_note.set_frontmatter("coffeeBuyDate", history.buy_date)
                history_note.set_frontmatter("coffeeBean", f"[[{bean_note.title}]]")
                history_note.add_tag(f"{self.tag_prefix}/beans/record")
                self._insert_attachment(history_note, history.attachments)
                note_path = record_path.joinpath(f"{history_note.title}.md")

                bean_notes.append({"note": history_note, "path": note_path})
        return bean_notes

    def preparations(self):
        notes = []
        method_path = self.coffee_folder.joinpath("001-equipment", "002-method")
        for prepare in self.bean_data.preparations.preparations:
            zettel_note = Zettelkasten(
                title=f"Coffee Preparation - {prepare.name}",
                n_type="literature",
                url="",
            )
            zettel_note.add_tag(f"{self.tag_prefix}/equipment/{prepare.style_type}")
            zettel_note.add_alias(prepare.uuid)
            zettel_note.set_frontmatter("shortName", prepare.name)

            notes.append(
                {
                    "note": zettel_note,
                    "path": method_path.joinpath(f"{zettel_note.title}.md"),
                }
            )

            # Start process prepartion tools
            tool_path = method_path.joinpath("tools")
            for tool in prepare.tools:
                tool_note = Zettelkasten(
                    title=f"Coffee Preparation Tool - {tool.uuid}",
                    n_type="literature",
                    url="",
                )
                tool_note.add_tag(f"{self.tag_prefix}/equipment/tool")
                tool_note.add_alias(tool.uuid)
                tool_note.set_frontmatter("shortName", tool.name)
                tool_note.set_frontmatter("CoffeeMethod", f"[[{zettel_note.title}]]")

                notes.append(
                    {
                        "note": tool_note,
                        "path": tool_path.joinpath(f"{tool_note.title}.md"),
                    }
                )
        return notes

    def brews(self):
        notes = []
        brew_path = self.coffee_folder.joinpath("003-brews")
        for brew in self.bean_data.brews.brews:
            zettel_note = Zettelkasten(
                title=f"Coffee Brew - {brew.uuid}",
                n_type="literature",
                url="",
            )

            zettel_note.add_tag(f"{self.tag_prefix}/brew")
            zettel_note.add_alias(brew.uuid)
            # Grinder Linnk
            mill = self.bean_data.mills.get_mill_by_uuid(brew.mill)
            zettel_note.set_frontmatter(
                "coffeeGrinder", f"[[Coffee Grinder - {mill.name}|{mill.name}]]"
            )
            # Bean Link
            bean = self.bean_data.beans.get_bean_by_uuid(brew.bean)
            zettel_note.set_frontmatter(
                "coffeeBean", f"[[Coffee Purchase Record - {brew.bean}|{bean.name}]]"
            )
            # Preparation Link
            preparation = self.bean_data.preparations.get_preparation_by_uuid(
                brew.preparation
            )
            tools = brew.tool_of_preparation
            methods = []
            if len(tools) > 0:
                for tool in tools:
                    tool_name = (
                        self.bean_data.preparations.get_preparation_tool_by_uuid(tool)
                    )
                    methods.append(
                        f"[[Coffee Preparation Tool - {tool_name.uuid}|{tool_name.name}]]"
                    )
            else:
                methods.append(
                    f"[[Coffee Preparation - {preparation.name}|{preparation.name}]]"
                )
            zettel_note.set_frontmatter("coffeeMethod", methods)
            zettel_note.set_frontmatter("coffeeGrinderSize", float(brew.grind_size))
            zettel_note.set_frontmatter("coffeePowderWeight", float(brew.grind_weight))
            zettel_note.set_frontmatter("coffeeBrewTime", int(brew.brew_time))
            zettel_note.set_frontmatter("coffeeBrewQuantity", float(brew.brew_quantity))
            zettel_note.set_frontmatter("coffeeBrewUnit", brew.brew_unit)
            zettel_note.set_frontmatter(
                "coffeeToWaterRatio",
                f"{round(brew.brew_quantity/brew.grind_weight, 2)}ml/g",
            )
            zettel_note.set_frontmatter("coffeeFlowProfile", brew.flow_profile)
            zettel_note.set_frontmatter("year", brew.timestamp)
            zettel_note.set_frontmatter("Ranking", brew.rating)

            notes.append(
                {
                    "note": zettel_note,
                    "path": brew_path.joinpath(f"{zettel_note.title}.md"),
                }
            )

        return notes

    def save(self):
        # save all grinder notes
        coffee_folder = self.obsidian_folder.joinpath("002-literature", "004-coffee")
        if coffee_folder.is_dir() is False:
            coffee_folder.mkdir(parents=True, exist_ok=True)

        for items in [self.mills(), self.beans(), self.preparations(), self.brews()]:
            for note in items:
                if note["path"].is_file() is False:
                    if note["path"].parent.is_dir() is False:
                        note["path"].parent.mkdir(parents=True, exist_ok=True)
                    # process the attachement
                    attachment_value = note["note"].get_frontmatter("banner")
                    if attachment_value is not None:
                        if attachment_value[0] == "/":
                            attachment_value = attachment_value[1:]

                        attachment_path = self.bean_conqueror_folder.joinpath(
                            attachment_value
                        )
                        if attachment_path.is_file():
                            new_image_name = (
                                note["note"].get_frontmatter("id") + ".webp"
                            )
                            new_path = note["path"].parent.joinpath(f"{new_image_name}")
                            self.compress_image(attachment_path, new_path)
                            note["note"].set_frontmatter(
                                "banner", f"![[{new_image_name}]]"
                            )

                    note["note"].save(note["path"])
                else:
                    # todo: check if the note has been updated.
                    # Due to Ures library, the frontmatter is always updated

                    # current_note = Zettelkasten.from_file(note["path"])
                    # current_note_frontmatter = deepcopy(current_note.metadata)
                    # del current_note_frontmatter['id']
                    # del current_note_frontmatter['create']
                    #
                    # new_note_frontmatter = deepcopy(note["note"].metadata)
                    # del new_note_frontmatter['id']
                    # del new_note_frontmatter['create']
                    #
                    # if current_note_frontmatter != new_note_frontmatter:
                    #     note["note"].save(note["path"])
                    pass
