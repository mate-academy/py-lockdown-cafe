class VaccineError(Exception):
    """Parent vaccine exception"""


class NotVaccinatedError(VaccineError):
    """Visitor isn't vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Visitor is not wearing a mask"""
