from pydantic import BaseModel, Field, model_validator
from typing import Annotated, Optional
import sys


class MazeConfig(BaseModel):
    width: Annotated[int,
                     Field(gt=0, description="Maze width (number of cells)")]
    height: Annotated[int,
                      Field(gt=0, description="Maze height (number of cells)")]
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None

    @model_validator(mode="after")
    def validate_coordinates(self) -> "MazeConfig":
        ex, ey = self.entry
        xx, xy = self.exit

        if not (0 <= ex < self.width and 0 <= ey < self.height):
            raise ValueError(
                f"ENTRY {self.entry} is out of bounds "
                f"(maze is {self.width}x{self.height})"
            )
        if not (0 <= xx < self.width and 0 <= xy < self.height):
            raise ValueError(
                f"EXIT {self.exit} is out of bounds "
                f"(maze is {self.width}x{self.height})"
            )
        if self.entry == self.exit:
            raise ValueError("ENTRY and EXIT must be different cells")
        return self


def _parse_raw(filepath: str) -> dict[str, str]:
    raw: dict[str, str] = {}
    with open(filepath, "r") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                raise ValueError(
                    f"Line {lineno}: "
                    f"invalid syntax '{line}' (expected KEY=VALUE)"
                )
            key, _, value = line.partition("=")
            raw[key.strip().upper()] = value.strip()
    return raw


def _parse_coord(value: str, key: str) -> tuple[int, int]:
    parts = value.split(",")
    if len(parts) != 2:
        raise ValueError(f"{key} must be in 'x,y' format, got '{value}'")
    try:
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        raise ValueError(f"{key} coordinates must be integers, got '{value}'")


def parse_config(filepath: str) -> MazeConfig:
    try:
        raw = _parse_raw(filepath)
    except FileNotFoundError:
        print(f"Error: config file '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    missing = required - raw.keys()
    if missing:
        print("Error: missing keys in config: "
              f"{', '.join(sorted(missing))}", file=sys.stderr)
        sys.exit(1)

    try:
        config = MazeConfig(
            width=int(raw["WIDTH"]),
            height=int(raw["HEIGHT"]),
            entry=_parse_coord(raw["ENTRY"], "ENTRY"),
            exit=_parse_coord(raw["EXIT"], "EXIT"),
            output_file=raw["OUTPUT_FILE"],
            perfect=raw["PERFECT"].lower() == "true",
            seed=int(raw["SEED"]) if "SEED" in raw else None,
        )
    except (ValueError, Exception) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    return config


if __name__ == "__main__":
    print(parse_config(sys.argv[1]))
