from typing import Optional


class VaccineError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message="Visitor is not vaccinated!"
    ) -> None:
        self.message = message
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            expiration_date: Optional,
            message="Vaccine is outdated!"
    ) -> None:
        self.expiration_date = expiration_date
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message="Visitor is not wearing a mask!"
    ) -> None:
        super().__init__(message)
