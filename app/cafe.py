import datetime
from errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self, name):
        self.name = name

    def visit_cafe(self, visitor):
        try:
            if "vaccine" not in visitor:
                raise NotVaccinatedError("Visitor is not vaccinated.")

            expiration_date = visitor["vaccine"].get("expiration_date")
            if not expiration_date or expiration_date < datetime.date.today():
                raise OutdatedVaccineError("Vaccine is outdated.")

            if not visitor.get("wearing_a_mask", False):
                raise NotWearingMaskError("Visitor is not wearing a mask.")

            return f"Welcome to {self.name}"

        except (NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError) as e:
            return str(e)
