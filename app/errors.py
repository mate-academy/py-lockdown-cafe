class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("You don't have a vaccine")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Your vaccine is expired")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("You don't have a mask")
