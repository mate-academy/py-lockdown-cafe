class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, text: str = "Visitor is not vaccinated") -> None:
        super().__init__(text)


class OutdatedVaccineError(VaccineError):
    def __init__(self, text: str = "Vaccine is expired") -> None:
        super().__init__(text)


class NotWearingMaskError(Exception):
    def __init__(self, text: str = "Visitor is not wearing a mask") -> None:
        super().__init__(text)
