class VaccineError(Exception):
    """Vaccination errors"""


class NotVaccinatedError(VaccineError):
    """The cafe visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Vaccination date is overdue"""


class NotWearingMaskError(Exception):
    """A cafe visitor is not wearing a mask"""
