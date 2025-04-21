class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, masks: int = 0) -> None:
        self.masks = masks

    def __str__(self) -> str:
        return f"Friends should buy {self.masks} masks"
