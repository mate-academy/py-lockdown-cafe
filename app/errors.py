class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Visitor {name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Visitor {name} has an outdated vaccine.")


class NotWearingMaskError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Visitor {name} is not wearing a mask.")
