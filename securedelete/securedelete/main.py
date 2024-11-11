from enum import Enum
import time

import typer
from rich.console import Console
from securedelete.delete import gutmann_wipe, dod_wipe, hmg_is5_wipe, random_wipe, simple_delete, create_test_file

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
) -> None:
    """Securely delete files."""
    file_path = f"{time.time()}-{mode.value}.txt"
    create_test_file(file_path)

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
    elif mode == Mode.SIMPLE:
        simple_delete(file_path)

    if verbose:
        console.print(f"\nFile {file_path} securely deleted using {mode.value} method.")
