class VaccineError(Exception):
    """Parent exception to NotVaccinatedError and OutdatedVaccineError"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception if visitor has outdated vaccine"""


class NotWearingMaskError(Exception):
    """Exception if visitor is not wearing a mask"""

