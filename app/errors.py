class VaccineError(Exception):
    """Main error class"""


class NotVaccinatedError(VaccineError):
    """This exception checks whether a visitor is vaccinated"""


class OutdatedVaccineError(VaccineError):
    """This exception checks vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """This exception checks if the visitor is wearing a mask"""
