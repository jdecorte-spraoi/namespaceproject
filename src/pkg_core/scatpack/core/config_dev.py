from dataclasses import dataclass, asdict


@dataclass
class Config:
    uuid: str = "1234343"
    helper: str = "no"

    def __iter__(self):
        return iter(asdict(self).keys())
