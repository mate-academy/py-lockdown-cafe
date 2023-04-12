class VaccineError(Exception):
    """Parent class for vaccine-related errors"""
    pass


class NotVaccinatedError(VaccineError):
    """Get vaccine!"""
    pass


class OutdatedVaccineError(VaccineError):
    """Get new vaccine!"""
    pass


class NotWearingMaskError(Exception):
    """Need to buy mask"""
    pass
