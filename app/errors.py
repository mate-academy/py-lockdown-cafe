class VaccineError(Exception):
    def __init__(self, message: str = "") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("All friends should be vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("All friends should be vaccinated")


class NotWearingMaskError(Exception):
    def __init__(self, masks_to_buy: int = 0) -> None:
        self.masks_to_buy = masks_to_buy

    def __str__(self) -> str:
        return f"Friends should buy {self.masks_to_buy} masks"
