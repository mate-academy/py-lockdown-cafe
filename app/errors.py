class VaccineError(Exception):
    pass


class NotWearingMaskError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotVaccinatedError(VaccineError):
    pass
