class VaccineError(Exception):
    """Base class for vaccine related errors."""


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
