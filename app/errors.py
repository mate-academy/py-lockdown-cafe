class VaccineError(Exception):
    def __init__(
            self,
            message: str = "All friends should be vaccinated"
    ) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    ...


class OutdatedVaccineError(VaccineError):
    ...


class NotWearingMaskError(Exception):
    def __init__(self, masks_to_buy: int = 0) -> None:
        self.masks_to_buy = masks_to_buy

    def __str__(self) -> str:
        return f"Friends should buy {self.masks_to_buy} masks"
