class NotWearingMaskError(Exception):
    pass


class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotVaccinatedError(VaccineError):
    pass
