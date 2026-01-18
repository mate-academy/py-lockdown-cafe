class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):

    def __init__(self, count: int = 0) -> None:
        self.count = count

    def __str__(self) -> str:
        return f"Friends should buy {self.count} masks"
