import datetime


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, name: str,
                 message: str = "Visitor is not vaccinated.") -> None:
        self.name = name
        super().__init__(f"{self.name}: {message}")


class OutdatedVaccineError(VaccineError):
    def __init__(self, name: str,
                 expiration_date: datetime.date,
                 message: str = "Vaccine is outdated.") -> None:
        self.name = name
        self.expiration_date = expiration_date
        super().__init__(f"{self.name}: "
                         f"{message} (Expired on {self.expiration_date})")


class NotWearingMaskError(Exception):
    def __init__(self, name: str,
                 message: str = "Visitor is not wearing a mask.") -> None:
        self.name = name
        super().__init__(f"{self.name}: {message}")
