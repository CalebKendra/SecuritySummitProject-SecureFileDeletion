import os
import random
from PIL import Image, ImageDraw, ImageFont

def random_wipe(file_path: str) -> None:
    """Random method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)
        passes = random.randint(1, 10)  # Random number of passes between 1 and 10
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(length))

def gutmann_wipe(file_path: str) -> None:
    """Gutmann method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)
        for _ in range(35):
            f.seek(0)
            f.write(os.urandom(length))

def dod_wipe(file_path: str) -> None:
    """US DoD 5220.22-M (8-306./E, C & E) (7 passes) method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)

        f.seek(0)
        f.write(b'\x00' * length)

        f.seek(0)
        f.write(b'\xFF' * length)

        f.seek(0)
        f.write(os.urandom(length))

        f.seek(0)
        f.write(os.urandom(length))

        f.seek(0)
        f.write(b'\x00' * length)

        f.seek(0)
        f.write(b'\xFF' * length)

        f.seek(0)
        f.write(os.urandom(length))

def hmg_is5_wipe(file_path: str) -> None:
    """British HMG IS5 (Enhanced) (3 passes) method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)
        f.seek(0)
        f.write(b'\x00' * length)

        f.seek(0)
        f.write(b'\xFF' * length)

        f.seek(0)
        f.write(os.urandom(length))

def create_test_png(file_path: str) -> None:
    """Create a test file with some content."""
    width, height = 600, 600
    image = Image.new('RGB', (width, height), 16777215)

    draw = ImageDraw.Draw(image)

    font_size = 35
    try:
        font = ImageFont.truetype("Ubuntu-R.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), file_path, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), file_path, fill="black", font=font)

    image.save(file_path)
    image.show()
