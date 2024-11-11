import os
import random

def simple_delete(file_path: str) -> None:
    """Simple deletion using os.remove."""
    os.remove(file_path)

def random_wipe(file_path: str) -> None:
    """Random method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)
        passes = random.randint(1, 10)  # Random number of passes between 1 and 10
        for _ in range(passes):
            f.seek(0)
            f.write(os.urandom(length))
    os.remove(file_path)

def gutmann_wipe(file_path: str) -> None:
    """Gutmann method for secure deletion."""
    with open(file_path, 'r+b') as f:
        length = os.path.getsize(file_path)
        for _ in range(35):
            f.seek(0)
            f.write(os.urandom(length))
    os.remove(file_path)

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

    os.remove(file_path)

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

    os.remove(file_path)

def create_test_file(file_path: str) -> None:
    """Create a test file with some content."""
    with open(file_path, 'w') as f:
        f.write("This is a test file for secure deletion.")
