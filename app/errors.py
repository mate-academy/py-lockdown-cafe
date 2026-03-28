class VaccineError(Exception):
    """Parent class for NotVaccinatedError and OutdatedVaccineError errors"""


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "Sorry, you should have vaccine first"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Unfortunately, it's expired"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Can you please wear your mask first"
