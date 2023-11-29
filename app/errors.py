class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("This individual is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("An outdated or expired vaccine was used.")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__(
            "This individual is not wearing "
            "a mask when required."
        )
