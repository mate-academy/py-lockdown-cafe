class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, mask_count: int = 0) -> None:
        self.mask_count = mask_count

    def __str__(self) -> str:
        return f"Friends should buy {self.mask_count} masks"
