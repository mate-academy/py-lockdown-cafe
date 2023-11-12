class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, friend_with_no_mask: int = 0) -> None:
        self.friend_with_no_mask = friend_with_no_mask

    def __str__(self) -> str:
        return f"Friends should buy {self.friend_with_no_mask} masks"
