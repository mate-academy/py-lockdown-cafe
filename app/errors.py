class VaccineError(BaseException):
    ...


class NotVaccinatedError(VaccineError):
    ...


class OutdatedVaccineError(VaccineError):
    ...


class NotWearingMaskError(BaseException):
    ...
