class NotWearingMaskError(Exception):
    ...


class VaccineError(Exception):
    ...


class NotVaccinatedError(VaccineError):
    ...


class OutdatedVaccineError(VaccineError):
    ...
