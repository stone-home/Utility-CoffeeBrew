import datetime
from typing import List, Dict


class BaseData:
    def __init__(self, data: Dict):
        self.data: dict = data

    def __str__(self):
        return f"Name: {self.name}, UUID: {self.uuid}"

    def __repr__(self):
        return f"Name: {self.name}, UUID: {self.uuid}"

    def _get_nested(self, *keys: str, default=None):
        """Safely get nested dictionary values."""
        current = self.data
        for key in keys:
            if not isinstance(current, dict):
                return default
            current = current.get(key, default)
            if current is None:
                return default
        return current

    @property
    def uuid(self) -> str:
        return self._get_nested("config", "uuid", default="")

    @property
    def name(self) -> str:
        return self.data.get("name")

    @property
    def timestamp(self) -> str:
        timestamp = self._get_nested("config", "unix_timestamp")
        datetime_object = datetime.datetime.fromtimestamp(timestamp)
        return datetime_object.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def attachments(self) -> List[str]:
        return self.data.get("attachments", [])

    @property
    def archived(self) -> bool:
        return self.data.get("finished")
