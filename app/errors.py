class VaccineError(Exception):
    """Parent class for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """Error that raises when visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Error that raises when visitors vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Error that raises when visitor have not a mask"""
