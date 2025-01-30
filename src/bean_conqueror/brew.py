from typing import Optional, List
from .base import BaseData


class Brew(BaseData):
    @property
    def bean(self) -> str:
        """Bean UUID"""
        return self.data.get("bean")

    @property
    def preparation(self) -> str:
        """Preparation UUID"""
        return self.data.get("method_of_preparation")

    @property
    def mill(self) -> str:
        """Mill UUID"""
        return self.data.get("mill")

    @property
    def tool_of_preparation(self) -> list:
        """List of Tools UUID"""
        return self.data.get("method_of_preparation_tools", [])

    @property
    def flow_profile(self) -> Optional[str]:
        return self.data.get("flow_profile", None)

    @property
    def rating(self) -> Optional[int]:
        return self.data.get("rating", None)

    @property
    def brew_time(self) -> int:
        return int(self.data.get("brew_time"))

    @property
    def grind_weight(self) -> float:
        return float(self.data.get("grind_weight"))

    @property
    def grind_size(self) -> float:
        """The size of the mill"""
        return float(self.data.get("grind_size"))

    @property
    def brew_quantity(self) -> float:
        return float(self.data.get("brew_beverage_quantity"))

    @property
    def brew_unit(self) -> str:
        return self.data.get("brew_beverage_quantity_type").lower()


class Brews:
    def __init__(self, data: dict):
        self._brews = {}
        for brew in data:
            brew = Brew(brew)
            self._brews[brew.uuid] = brew

    @property
    def brews(self) -> List[Brew]:
        return list(self._brews.values())
