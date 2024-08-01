class VaccineError(Exception):
    ...
    # def __str__(self):
    #     return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    ...


class OutdatedVaccineError(VaccineError):
    ...


class NotWearingMaskError(Exception):
    masks_to_buy = 0

    def __str__(self) -> str:
        return f"Friends should buy {self.masks_to_buy} masks"
