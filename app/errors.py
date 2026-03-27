class VaccineError(Exception):
    """Error called when some problems with vaccines exist"""


class NotVaccinatedError(VaccineError):
    """Error used when vaccine is not exist at all"""


class OutdatedVaccineError(VaccineError):
    """Error when vaccine outdated"""


class NotWearingMaskError(Exception):
    """Error when someone without mask"""
