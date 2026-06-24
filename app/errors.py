class CafeValidationError(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class VaccineError(CafeValidationError):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(CafeValidationError):
    pass
