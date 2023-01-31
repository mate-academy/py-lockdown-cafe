class VaccineError(Exception):
    def __init__(self) -> None:
        self.message = "All friends should be vaccinated"
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__()


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__()


class NotWearingMaskError(Exception):
    def __init__(self, masks_to_buy: int = 1) -> None:
        self.masks_to_buy = masks_to_buy
        self.message = f"Friends should buy {self.masks_to_buy} masks"
        super().__init__(self.message)
