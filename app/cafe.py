import datetime


from app import errors


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if visitor.get("vaccine") is None:
            raise errors.NotVaccinatedError("Visitor must be vaccinated to enter the cafe")
        else:
            if visitor["vaccine"]["expiration_date"] < datetime.date.today():
                raise errors.OutdatedVaccineError("Visitor's vaccine has expired")
            else:
                if not visitor["wearing_a_mask"]:
                    raise errors.NotWearingMaskError("Visitor must wear a mask")
                else:
                    return f"Welcome to {self.name}"
