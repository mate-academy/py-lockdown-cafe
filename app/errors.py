class VaccineError(Exception):
    """Parent class for vaccine-related errors"""


class NotVaccinatedError(VaccineError):
    """Get vaccine!"""


class OutdatedVaccineError(VaccineError):
    """Get new vaccine!"""


class NotWearingMaskError(Exception):
    """Need to buy mask"""