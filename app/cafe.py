import datetime

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str | Exception:
        try:
            vaccine = visitor["vaccine"]
            assert vaccine["expiration_date"] >= datetime.date.today()
        except KeyError:
            raise NotVaccinatedError(f"{visitor['name']} has no vaccine!")
        except AssertionError:
            raise OutdatedVaccineError(f"{visitor['name']}'s "
                                       f"vaccine is expired!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(f"{visitor['name']} has no mask!")
        return f"Welcome to {self.name}"
