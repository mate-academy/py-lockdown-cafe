from app.errors import OutdatedVaccineError, NotWearingMaskError
from app.errors import NotVaccinatedError
from datetime import date


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        base_text_error = (
            f"Visitor {visitor.get('name', 'unknown')}"
            " cannot enter {self.name}"
        )
        expiration_date = visitor['vaccine']['expiration_date']

        if "vaccine" not in visitor:
            raise NotVaccinatedError(f"{base_text_error}: not vaccinated.")
        elif date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError(
                (
                    f"{base_text_error}: expired vaccine"
                    f" {expiration_date.strftime('%Y-%m-%d')}"
                )
            )
        elif not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError(
                (
                    f"{base_text_error}: "
                    "need to wear a mask"
                )
            )
        return f"Welcome to {self.name}"
