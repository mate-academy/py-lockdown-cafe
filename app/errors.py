class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine is outdated"


class NotWearingMaskError(Exception):
    def __init__(self, masks_to_buy: int) -> None:
        self.masks_to_buy = masks_to_buy

    def __str__(self) -> str:
        return f"Friends should buy {self.masks_to_buy} masks"
