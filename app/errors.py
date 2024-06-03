class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated!")


class OutdatedVaccineError(VaccineError):
    def __init__(self, expiration_date: str) -> None:
        super().__init__(f"Vaccine is outdated! "
                         f"Expiration date: {expiration_date}")


class NotWearingMaskError(Exception):
    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask!")
