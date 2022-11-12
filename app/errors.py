class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    masks_to_buy = 0

    def __str__(self) -> str:
        return f"Friends should buy {NotWearingMaskError.masks_to_buy} masks"
