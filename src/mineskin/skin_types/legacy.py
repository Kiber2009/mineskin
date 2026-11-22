from typing import Any

from PIL import Image, ImageDraw

from mineskin.skin_types.abc import MinecraftSkin
from mineskin.skin_types.abc import MinecraftSkinFormat
from mineskin.utils import check_all_regions_transparency


class LegacyMinecraftSkin(MinecraftSkin):
    def __init__(self, img: Image.Image) -> None:
        self._img = img

    @property
    def image(self) -> Image.Image:
        return self._img

    @property
    def format(self) -> MinecraftSkinFormat:
        return MinecraftSkinFormat.LEGACY

    @property
    def slim(self) -> bool:
        return False

    @property
    def has_overlay(self) -> bool:
        return not check_all_regions_transparency(
            self._img,
            (
                (40, 0, 56, 8),
                (32, 8, 64, 16),
            ),
        )

    def optimize(self, keep_ears: bool = False) -> None:
        draw = ImageDraw.Draw(self._img)
        draw.rectangle((0, 0, 7, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle((56, 0, 63, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle((0, 16, 3, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0)
        draw.rectangle(
            (12, 16, 19, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (36, 16, 43, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (52, 16, 55, 19), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        draw.rectangle(
            (56, 16, 63, 31), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
        )
        if keep_ears:
            draw.rectangle(
                (24, 0, 24, 0), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (37, 0, 37, 0), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (24, 7, 37, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
            draw.rectangle(
                (38, 0, 39, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )
        else:
            draw.rectangle(
                (24, 0, 39, 7), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
            )

    def convert(self, fmt: MinecraftSkinFormat, **kwargs: Any) -> MinecraftSkin:
        from skin_types.new_1_8 import MinecraftSkinV1_8

        match fmt:
            case MinecraftSkinFormat.LEGACY:
                return LegacyMinecraftSkin(self._img.copy())
            case MinecraftSkinFormat.V1_8:
                img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
                img.paste(self._img, box=(0, 0))
                img.paste(self._img.crop((0, 16, 16, 32)), box=(16, 48))
                img.paste(self._img.crop((40, 16, 56, 32)), box=(32, 48))
                return MinecraftSkinV1_8(img)
            case _:
                raise NotImplementedError(f"Unsupported skin format: {fmt}")


__all__ = ("LegacyMinecraftSkin",)
