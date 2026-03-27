class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated")


class OutdatedVaccineError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor's vaccine is outdated")


class NotWearingMaskError(ValueError):
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask!")
