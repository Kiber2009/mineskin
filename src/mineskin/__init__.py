from enum import Enum, auto
from .utils import check_all_regions_transparency

from PIL import Image, ImageDraw


class MinecraftSkinFormat(Enum):
    OLD = auto()
    NEW_1_8 = auto()

    @staticmethod
    def detect(img):
        match img.size:
            case (64, 64):
                return MinecraftSkinFormat.NEW_1_8
            case (64, 32):
                return MinecraftSkinFormat.OLD
            case _:
                raise ValueError("Unable to determine skin format")


class MinecraftSkin:
    def __init__(self, img):
        self._img = img
        self._fmt = MinecraftSkinFormat.detect(img)

    @staticmethod
    def open(fp):
        return MinecraftSkin(Image.open(fp))

    def close(self):
        self._img.close()

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.close()

    def load(self):
        self._img.load()

    def save(self, fp):
        self._img.save(fp)

    def is_slim(self, check_overlay=True):
        match self._fmt:
            case MinecraftSkinFormat.OLD:
                return False
            case MinecraftSkinFormat.NEW_1_8:
                return check_all_regions_transparency(
                    self._img,
                    (
                        # Right arm
                        (50, 16, 52, 20),
                        (54, 20, 56, 32),
                        # Right arm overlay
                        *(
                            ((50, 32, 52, 36), (54, 36, 56, 48))
                            if check_overlay
                            else ()
                        ),
                        # Left arm
                        (42, 48, 44, 52),
                        (46, 52, 48, 64),
                        # Left arm overlay
                        *(
                            ((58, 48, 60, 52), (62, 52, 64, 64))
                            if check_overlay
                            else ()
                        ),
                    ),
                )
            case _:
                raise NotImplementedError

    def optimize(self, keep_ears=False):
        match self._fmt:
            case MinecraftSkinFormat.OLD:
                draw = ImageDraw.Draw(self._img)
                draw.rectangle(
                    (0, 0, 8, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (56, 0, 64, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (0, 16, 4, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (12, 16, 20, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (36, 16, 44, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (52, 16, 56, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (56, 16, 64, 32), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                if keep_ears:
                    draw.rectangle(
                        (24, 0, 25, 1), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (37, 0, 38, 1), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (24, 7, 38, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (38, 0, 40, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                else:
                    draw.rectangle(
                        (24, 0, 40, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
            case MinecraftSkinFormat.NEW_1_8:
                draw = ImageDraw.Draw(self._img)
                draw.rectangle(
                    (0, 0, 8, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (56, 0, 64, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (0, 16, 4, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (12, 16, 20, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (36, 16, 44, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (52, 16, 56, 20), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (0, 32, 4, 36), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (12, 32, 20, 36), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (36, 32, 44, 36), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (52, 32, 56, 36), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (0, 48, 4, 52), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (12, 48, 20, 52), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (28, 48, 36, 52), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (44, 48, 52, 52), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (60, 48, 64, 52), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                draw.rectangle(
                    (56, 16, 64, 48), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                )
                if keep_ears:
                    draw.rectangle(
                        (24, 0, 25, 1), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (37, 0, 38, 1), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (24, 7, 38, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                    draw.rectangle(
                        (38, 0, 40, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
                else:
                    draw.rectangle(
                        (24, 0, 40, 8), fill=(0, 0, 0, 0), outline=(0, 0, 0, 0), width=0
                    )
            case _:
                raise NotImplementedError

    def convert(self, fmt, ignore_slim=False, use_left_arm=False, use_left_leg=False):
        if self._fmt == fmt:
            return self._img.copy()
        match (self._fmt, fmt):
            case (MinecraftSkinFormat.OLD, MinecraftSkinFormat.NEW_1_8):
                img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
                img.paste(self._img, box=(0, 0))
                img.paste(self._img.crop((0, 16, 16, 32)), box=(16, 48))
                img.paste(self._img.crop((40, 16, 56, 32)), box=(32, 48))
                return img
            case (MinecraftSkinFormat.NEW_1_8, MinecraftSkinFormat.OLD):
                if (not ignore_slim) and self.is_slim(check_overlay=False):
                    raise ValueError("Slim skins cannot be converted to old format")
                if not (use_left_leg or use_left_arm):
                    return self._img.crop((0, 0, 64, 32))
                img = Image.new("RGBA", (64, 32), (0, 0, 0, 0))
                img.paste(self._img.crop((0, 0, 64, 16)), box=(0, 0))
                img.paste(self._img.crop((16, 16, 40, 32)), box=(16, 16))
                if use_left_arm:
                    img.paste(self._img.crop((16, 48, 32, 64)), box=(0, 16))
                else:
                    img.paste(self._img.crop((0, 16, 16, 32)), box=(0, 16))
                if use_left_leg:
                    img.paste(self._img.crop((32, 48, 48, 64)), box=(40, 16))
                else:
                    img.paste(self._img.crop((40, 16, 56, 32)), box=(40, 16))
                return img
            case _:
                raise NotImplementedError

    @property
    def format(self):
        return self._fmt

    @property
    def has_overlay(self):
        match self._fmt:
            case MinecraftSkinFormat.OLD:
                return not check_all_regions_transparency(
                    self._img,
                    (
                        (40, 0, 56, 8),
                        (32, 8, 64, 16),
                    ),
                )
            case MinecraftSkinFormat.NEW_1_8:
                return not check_all_regions_transparency(
                    self._img,
                    (
                        (40, 0, 56, 8),
                        (32, 8, 64, 16),
                        (4, 32, 12, 36),
                        (20, 32, 36, 36),
                        (44, 32, 52, 36),
                        (0, 36, 56, 48),
                        (4, 48, 12, 52),
                        (0, 52, 16, 64),
                        (52, 48, 60, 52),
                        (48, 52, 64, 64),
                    ),
                )
            case _:
                raise NotImplementedError


__all__ = ("MinecraftSkin", "MinecraftSkinFormat")
