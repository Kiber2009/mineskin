from PIL.Image import Image

from mineskin.skin_types.abc import MinecraftSkin
from mineskin.skin_types.legacy import LegacyMinecraftSkin
from mineskin.skin_types.new_1_8 import MinecraftSkinV1_8


def skin(img: Image) -> MinecraftSkin:
    match img.size:
        case (64, 64):
            return MinecraftSkinV1_8(img)
        case (64, 32):
            return LegacyMinecraftSkin(img)
        case _:
            raise ValueError("Unable to determine skin format")


__all__ = ("skin",)
