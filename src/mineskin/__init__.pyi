from types import TracebackType
import os
from enum import Enum, auto
from typing import IO

from PIL.Image import Image

class MinecraftSkinFormat(Enum):
    OLD = auto()
    NEW_1_8 = auto()

    @staticmethod
    def detect(img: Image) -> MinecraftSkinFormat:
        """
        Determines the format of a skin

        :param img: Skin image

        :raise ValueError: Unable to determine format
        """
        ...

class MinecraftSkin:
    def __init__(self, img: Image) -> None: ...
    @staticmethod
    def open(
        fp: str | bytes | os.PathLike[str] | os.PathLike[bytes] | IO[bytes],
    ) -> MinecraftSkin: ...
    def close(self) -> None: ...
    def __enter__(self) -> MinecraftSkin: ...
    def __exit__[T: BaseException](
        self,
        _exc_type: type[T] | None,
        _exc_val: T | None,
        _exc_tb: TracebackType | None,
    ) -> None: ...
    def load(self) -> None: ...
    def save(
        self, fp: str | bytes | os.PathLike[str] | os.PathLike[bytes] | IO[bytes]
    ) -> None: ...
    def is_slim(self, check_overlay: bool = True) -> bool: ...
    def optimize(self, keep_ears: bool = False) -> None: ...
    def convert(
        self,
        fmt: MinecraftSkinFormat,
        ignore_slim: bool = False,
        use_left_arm: bool = False,
        use_left_leg: bool = False,
    ) -> Image: ...
    @property
    def format(self) -> MinecraftSkinFormat: ...
    @property
    def has_overlay(self) -> bool: ...

__all__ = ("MinecraftSkin", "MinecraftSkinFormat")
