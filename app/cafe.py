import datetime
import errors as e


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name
    
    
    def visit_cafe(self, visitor: dict) -> None | str:
        if "vaccine" not in visitor:
            raise e.NotVaccinatedError()
        elif datetime.date.today() > visitor["vaccine"].get("expiration_date"):
            raise e.OutdatedVaccineError()
        elif not visitor["wearing_a_mask"]:
            raise e.NotWearingMaskError()
        else:
            return f"Welcome to {self.name}"
