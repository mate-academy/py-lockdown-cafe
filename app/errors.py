class VaccineError(Exception):
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated.")


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing mask.")
