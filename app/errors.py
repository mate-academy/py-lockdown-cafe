class CafeError(Exception):
    pass


class VaccineError(CafeError):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(CafeError):
    pass
