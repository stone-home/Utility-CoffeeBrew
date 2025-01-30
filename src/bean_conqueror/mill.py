from typing import Dict, List, Optional
from .base import BaseData


class Mill(BaseData):
    pass


class Mills:
    def __init__(self, data: List[Dict]):
        self._mills: Dict[str, Mill] = {}
        for mill in data:
            mill_class = Mill(mill)
            self._mills[mill_class.uuid] = mill_class

    @property
    def mills(self) -> List[Mill]:
        return list(self._mills.values())

    def get_mill_by_uuid(self, uuid: str) -> Mill:
        return self._mills.get(uuid)

    def get_mill_by_name(self, name: str) -> Optional[Mill]:
        for mill in self._mills.values():
            if mill.name == name:
                return mill
        return None
