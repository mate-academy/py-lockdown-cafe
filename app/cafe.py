import datetime

from app.errors import NotVaccinatedError, OutdatedVaccineError, \
    NotWearingMaskError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self,
                   visitor: dict
                   ) -> str | NotVaccinatedError | \
            OutdatedVaccineError | NotWearingMaskError:

        if "vaccine" not in visitor:
            raise NotVaccinatedError

        current_date = datetime.datetime.now().date()
        if visitor["vaccine"]["expiration_date"] < current_date:
            raise OutdatedVaccineError

        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError(masks_to_buy=0)

        return f"Welcome to {self.name}"
