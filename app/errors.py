class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    def __init__(self, name: None = None, masks_to_buy: None = None) -> None:
        self.name = name
        self.masks_to_buy = masks_to_buy

    def __str__(self) -> str:
        if self.masks_to_buy is not None:
            return f"Friends should buy {self.masks_to_buy} masks"
        return f"{self.name} is not wearing a mask"
