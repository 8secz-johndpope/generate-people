from PIL import Image
import os
from glob import glob


def convert_jpg():
    recentDir = max(
        glob(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "dist",
                "generated-images-1",
                "*/",
            )
        ),
        key=os.path.getmtime,
    )

    images = glob(os.path.join(recentDir, "*.png"))

    for filename in images:
        png = Image.open(filename)
        seedname = os.path.splitext(os.path.basename(filename))[0][4:]
        path = f"dist/images/{seedname}.jpg"
        rgb_png = png.convert("RGB")
        rgb_png_resized = rgb_png.resize((128, 128), Image.ANTIALIAS)
        rgb_png_resized.save(path)


if __name__ == "__main__":
    convert_jpg()
