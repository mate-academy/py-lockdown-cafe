class CafeAccessError(Exception):
    pass


class VaccineError(CafeAccessError):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(CafeAccessError):
    pass
