# All errors should be defined in the errors.py module.
class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
