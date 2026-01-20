class VaccineError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
