class VaccineError(Exception):
    def __str__(self) -> str:
        return "Person is not vaccinated"


class NotVaccinatedError(VaccineError):
    """Person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine term has expired"""


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Person is not wearing a mask"
