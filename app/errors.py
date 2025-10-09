class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotVaccinatedError(VaccineError):
    pass
