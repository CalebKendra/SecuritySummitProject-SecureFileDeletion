from enum import Enum
import time
import os

import typer # type: ignore
from rich.console import Console # type: ignore
from securedelete.delete import gutmann_wipe, dod_wipe, hmg_is5_wipe, random_wipe, create_test_png

cli = typer.Typer()

console = Console()

class Mode(Enum):
    GUTMANN = "gutmann"
    DOD = "dod"
    HMG_IS5 = "hmg_is5"
    RANDOM = "random"
    SIMPLE = "simple"

@cli.command()
def securedelete(
    mode: Mode = typer.Option(
        Mode.GUTMANN,
        "--mode",
        help="Specify the mode.",
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose mode."),
    log: bool = typer.Option(False, "--log", help="Enable logging."),
) -> None:
    """Securely delete files."""
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    time_lock = time.time()
    file_path = f"{time_lock}-{mode.value}.png"
    create_test_png(file_path)

    if verbose:
        console.print(f"Securely deleting file {file_path} using {mode.value} method.\n")
        console.print("3...")
        time.sleep(1)
        console.print("2...")
        time.sleep(1)
        console.print("1...")
        time.sleep(1)


    if mode == Mode.GUTMANN:
        gutmann_wipe(file_path)
    elif mode == Mode.DOD:
        dod_wipe(file_path)
    elif mode == Mode.HMG_IS5:
        hmg_is5_wipe(file_path)
    elif mode == Mode.RANDOM:
        random_wipe(file_path)

    file_size = os.path.getsize(file_path)
    os.remove(file_path)

    if verbose:
        console.print(f"\nFile {file_path} ({file_size}) securely deleted using {mode.value} method.")

    if log:
        console.print(f"Logging to `log.txt`")
        with open('log.txt', 'a') as f:
            f.write(f"[{formatted_time}] [File] {file_path} [Size] {file_size} [Method] {mode.value}\n")
