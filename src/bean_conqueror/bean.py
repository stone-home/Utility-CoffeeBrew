from .base import BaseData
from typing import List, Dict, Optional


class BeanVariety:
    def __init__(self, data: Dict):
        self.data = data

    def __repr__(self):
        return f"Bean Variety: {self.display_name})"

    @property
    def country(self) -> str:
        return self._capitalize_string(self.data.get("country", ""))

    @property
    def region(self) -> str:
        return self._capitalize_string(self.data.get("region", ""))

    @property
    def variety(self) -> str:
        return self._capitalize_string(self.data.get("variety", ""))

    @property
    def processing(self):
        return self._capitalize_string(self.data.get("processing", ""))

    def display_name(self):
        if len(self.region.strip()) == 0:
            return f"{self.country}/unknown/{self.variety}"
        else:
            return f"{self.country}/{self.region}/{self.variety}"

    def _capitalize_string(self, tag: str) -> str:
        return "".join([item.capitalize() for item in tag.split(" ")])


class Bean(BaseData):
    @property
    def buy_date(self) -> str:
        return self.data.get("buyDate")

    @property
    def roasting_date(self) -> str:
        return self.data.get("roastingDate")

    @property
    def roaster(self) -> str:
        return self.data.get("roaster")

    @property
    def roasting_level(self) -> float:
        return self.data.get("roast_range")

    @property
    def decaf(self) -> bool:
        return self.data.get("decaffeinated")

    @property
    def aromatics(self) -> list:
        aromatic = self.data.get("aromatics").replace("，", ",").split(",")
        aromatic = [self._capitalize_string(aroma.strip()) for aroma in aromatic]
        return aromatic

    @property
    def varieties(self) -> List[BeanVariety]:
        return [BeanVariety(variety) for variety in self.data.get("bean_information", [])]

    @property
    def price(self):
        return self.data.get("cost")

    @property
    def weight(self):
        return self.data.get("weight")

    def is_single_origin(self) -> bool:
        return self.data.get("beanMix") == "SINGLE_ORIGIN"

    def _capitalize_string(self, tag: str) -> str:
        return "".join([item.capitalize() for item in tag.split(" ")])


class Beans:
    def __init__(self, data: List[Dict]):
        self._beans: Dict[str, Bean] = {}
        for bean in data:
            bean_class = Bean(bean)
            self._beans[bean_class.uuid] = bean_class

    @property
    def beans(self) -> Dict[str, Dict]:
        _beans = {}
        for uuid, bean in self._beans.items():
            if bean.name not in _beans.keys():
                _beans[bean.name] = {
                    "name": bean.name,
                    "roaster": bean.roaster,
                    "decaf": bean.decaf,
                    "aromatics": bean.aromatics,
                    "varieties": [],
                    "process": [],
                    "history": []
                }
                _variety = []
                _process = []
                for variety in bean.varieties:
                    _variety.append(variety.display_name())
                    _process.append(variety.processing)
                _variety = list(set(_variety))
                _process = list(set(_process))
                _beans[bean.name]["varieties"] = _variety
                _beans[bean.name]["process"] = _process

            _beans[bean.name]["history"].append(bean)
        return _beans

    def get_bean_by_uuid(self, uuid: str) -> Bean:
        return self._beans.get(uuid)

    def get_bean_by_name(self, name: str) -> List[Bean]:
        beans = []
        for bean in self._beans.values():
            if bean.name == name:
                beans.append(bean)
        return beans