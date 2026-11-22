from typing import Any
from enum import Enum, auto

from PIL.Image import Image

from abc import ABC, abstractmethod


class MinecraftSkinFormat(Enum):
    LEGACY = auto()
    V1_8 = auto()


# TODO: has_ears
# TODO: validate
class MinecraftSkin(ABC):
    @property
    @abstractmethod
    def image(self) -> Image:
        pass

    @property
    @abstractmethod
    def format(self) -> MinecraftSkinFormat:
        pass

    @property
    @abstractmethod
    def slim(self) -> bool:
        pass

    @property
    @abstractmethod
    def has_overlay(self) -> bool:
        pass

    @abstractmethod
    def optimize(self, keep_ears: bool = False) -> None:
        pass

    @abstractmethod
    def convert(self, fmt: MinecraftSkinFormat, **kwargs: Any) -> MinecraftSkin:
        pass


__all__ = ("MinecraftSkinFormat", "MinecraftSkin")
