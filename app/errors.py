class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass
