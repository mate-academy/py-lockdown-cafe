from datetime import date
from app.errors import NotVaccinatedError, OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        vaccine = visitor.get("vaccine")
        is_visitor_in_mask = visitor.get("wearing_a_mask", False)

        if not vaccine:
            raise NotVaccinatedError(
                f"{visitor["name"]}, "
                f"you should be vaccinated."
            )

        if vaccine["expiration_date"] < date.today():
            raise OutdatedVaccineError(f"{visitor["name"]}, "
                                       f" you need to get vaccinated again")

        if not is_visitor_in_mask:
            raise NotWearingMaskError(f"{visitor["name"]}, please wear a mask")

        return f"Welcome to {self.name}"
