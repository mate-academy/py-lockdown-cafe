class VaccineError(Exception):
    ...


class NotWearingMaskError(Exception):
    ...


class NotVaccinatedError(VaccineError):
    ...


class OutdatedVaccineError(VaccineError):
    ...
