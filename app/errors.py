class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotVaccinatedError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
