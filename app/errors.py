class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        self.message = "The visitor does not have a vaccine."
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        self.message = "The vaccine must not be expired."
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        self.message = "The visitor must wear a face mask."
        super().__init__(self.message)
