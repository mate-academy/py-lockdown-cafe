
class VaccineError(Exception):
    """Vaccine error"""


class NotVaccinatedError(VaccineError):
    """When not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """When not vaccine is expired"""


class NotWearingMaskError(Exception):
    """Maskless scum"""
