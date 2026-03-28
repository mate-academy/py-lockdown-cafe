class VaccineError(Exception):
    """Visitor has some issue with vaccine"""


class NotVaccinatedError(VaccineError):
    """Visitor are not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Visitor has expired vacc date"""


class NotWearingMaskError(Exception):
    """Visitor has no mask"""
