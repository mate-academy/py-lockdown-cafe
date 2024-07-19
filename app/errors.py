class VaccineError(Exception):
    def __str__(self) -> str:
        return "Vaccination status is missing or invalid for the entity"


class NotVaccinatedError(VaccineError):
    """Person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine term has expired"""


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Entity is not wearing a mask"
