from datetime import date

from app.errors import NotVaccinatedError, \
    OutdatedVaccineError, NotWearingMaskError


class Cafe:
    def __init__(self,
                 name: str):
        self.name = name

    def visit_cafe(self, visitor: dict):
        if "vaccine" not in visitor:
            raise NotVaccinatedError("You are dirty with CoVid-19 ;(")
        if (visitor["vaccine"]["expiration_date"] - date.today()).days < 0:
            raise OutdatedVaccineError("Your vaccine seal is broken!")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("Cover your face, pleb!")
        return f"Welcome to {self.name}"
