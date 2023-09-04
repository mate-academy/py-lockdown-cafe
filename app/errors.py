class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """The person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccine has expired"""


class NotWearingMaskError(VaccineError):
    """The man has no mask"""
