class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass
