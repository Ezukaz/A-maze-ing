from pydantic import BaseModel, Field, model_validator, field_validator
import sys

"""validate and parse config.txt"""


class MazeConfig(BaseModel):
    """mandatory keys and values"""
    width: int = Field(gt=0, description="Maze width (number of cells)")
    height: int = Field(gt=0, description="Maze height (number of cells)")
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str = Field(min_length=1)
    perfect: bool

    @field_validator("entry", "exit")
    @classmethod
    def validate_coord(cls, v: tuple[int, int]) -> tuple[int, int]:
        """validate natural integer coord or not"""
        x, y = v
        if x < 0 or y < 0:
            raise ValueError(f"coordinates must be >= 0. got ({x}, {y})")
        return v

    @model_validator(mode="after")
    def validate_coordinates(self) -> "MazeConfig":
        """
        validate entry and exit coordinates are different and in maze range.
        """
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
    """
    parse contents in config.txt is written
        as specified format or not. (expected KEY=VALUE)
    """
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
            key, value = line.split("=", 1)
            raw[key.strip().upper()] = value.strip()
    return raw


def _parse_coord(value: str, key: str) -> tuple[int, int]:
    """parse coordinate / change values into integers"""
    parts = value.split(",")
    if len(parts) != 2:
        raise ValueError(f"{key} must be in 'x,y' format, got '{value}'")
    try:
        return int(parts[0].strip()), int(parts[1].strip())
    except ValueError:
        raise ValueError(f"{key} coordinates must be integers, got '{value}'")


def parse_config(filepath: str) -> MazeConfig:
    """this function is used ultimately as a module."""

    """call parse_raw"""
    try:
        raw = _parse_raw(filepath)
    except FileNotFoundError:
        print(f"Error: config file '{filepath}' not found.", file=sys.stderr)
        exit()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit()

    """validate all required key was in config.txt"""
    required = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}
    missing = required - raw.keys()
    if missing:
        print("Error: missing keys in config: "
              f"{', '.join(sorted(missing))}", file=sys.stderr)
        exit()

    try:
        """validate key-"PERFECT" to avoid mypy error"""
        perf = raw["PERFECT"].lower()
        if perf not in ("true", "false"):
            raise ValueError(
                f"'PERFECT' must be 'True' or 'False', got '{raw['PERFECT']}'")
        """initialize MazeConfig"""
        config = MazeConfig(
            width=int(raw["WIDTH"]),
            height=int(raw["HEIGHT"]),
            entry=_parse_coord(raw["ENTRY"], "ENTRY"),
            exit=_parse_coord(raw["EXIT"], "EXIT"),
            output_file=raw["OUTPUT_FILE"],
            perfect=perf == "true"
        )
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        exit()

    return config


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("no param.")
        exit()
    for key_value in parse_config(sys.argv[1]):
        print(key_value)
