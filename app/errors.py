class LockdownError(Exception):
    def __init__(self, message: str = "Cafe is in lockdown!") -> None:
        super().__init__(message)


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
