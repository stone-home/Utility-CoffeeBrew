from typing import List, Dict, Optional
from .base import BaseData


class Tool(BaseData):
    pass


class Preparation(BaseData):
    @property
    def style_type(self) -> str:
        return self.data.get("style_type")

    @property
    def tools(self) -> List[Tool]:
        return [Tool(tool) for tool in self.data.get("tools", [])]

    def get_tool_by_uuid(self, uuid: str) -> Optional[Tool]:
        for tool in self.tools:
            if tool.uuid == uuid:
                return tool
        return None

class Preparations:
    def __init__(self, data: List[Dict]):
        self._preparations: Dict[str, Preparation] = {}
        for preparation in data:
            preparation_class = Preparation(preparation)
            self._preparations[preparation_class.uuid] = preparation_class

    @property
    def preparations(self) -> List[Preparation]:
        return list(self._preparations.values())

    def get_preparation_tool_by_uuid(self, uuid: str) -> Optional[Preparation]:
        _tools = {}
        for preparation in self._preparations.values():
            for tool in preparation.tools:
                _tools[tool.uuid] = tool
        return _tools.get(uuid)

    def get_preparation_by_uuid(self, uuid: str) -> Preparation:
        return self._preparations.get(uuid)

    def get_preparation_by_name(self, name: str) -> Optional[Preparation]:
        for preparation in self._preparations.values():
            if preparation.name == name:
                return preparation
        return None