import datetime


from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" in visitor:
            if ("expiration_date" in visitor["vaccine"]
                    and datetime.date.today()
                    <= visitor["vaccine"]["expiration_date"]):
                if visitor["wearing_a_mask"]:
                    return f"Welcome to {self.name}"
                else:
                    raise NotWearingMaskError
            else:
                raise OutdatedVaccineError
        else:
            raise NotVaccinatedError
