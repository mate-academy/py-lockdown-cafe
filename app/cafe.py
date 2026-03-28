import datetime
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError  # noqa: E501


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> None:
        if not ("vaccine" in visitor):
            raise NotVaccinatedError("You should be vaccinated")
        if visitor.get("vaccine").get("expiration_date") < datetime.date.today():  # noqa: E501
            raise OutdatedVaccineError("You should be vaccinated")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("You shoul wear a mask")
        return f"Welcome to {self.name}"


if __name__ == "__main__":
    pass
