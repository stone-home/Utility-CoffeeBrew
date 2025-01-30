import datetime
from typing import List, Dict


class BaseData:
    def __init__(self, data: Dict):
        self.data: dict = data

    def __str__(self):
        return f"Name: {self.name}, UUID: {self.uuid}"

    def __repr__(self):
        return f"Name: {self.name}, UUID: {self.uuid}"

    @property
    def uuid(self) -> str:
        return self.data.get("config").get("uuid")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def timestamp(self) -> str:
        timestamp = int(self.data.get("config").get("unix_timestamp"))
        datetime_object = datetime.datetime.fromtimestamp(timestamp)
        return datetime_object.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def attachments(self) -> List[str]:
        return self.data.get("attachments", [])

    @property
    def archived(self) -> bool:
        return self.data.get("finished")
