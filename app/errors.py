class VaccineError(Exception):
    ...


class OutdatedVaccineError(VaccineError):
    ...


class NotVaccinatedError(VaccineError):
    ...


class NotWearingMaskError(Exception):
    ...
