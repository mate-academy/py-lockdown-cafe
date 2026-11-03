class VaccineError(Exception):
    """Exception: Vaccine Error"""


class NotVaccinatedError(VaccineError):
    """Exception: Visitor not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception: Vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Exception: Visitor is not wearing a mask"""
