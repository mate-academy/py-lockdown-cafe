from __future__ import annotations
from datetime import date


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
        super().__init__(f"{visitor_name} is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name: str, expiration_date: date) -> None:
        self.visitor_name = visitor_name
        self.expiration_date = expiration_date
        super().__init__(f"{visitor_name} has an outdated vaccine"
                         f"(expired on {expiration_date}).")


class NotWearingMaskError(Exception):
    def __init__(self, visitor_name: str) -> None:
        self.visitor_name = visitor_name
        super().__init__(f"{visitor_name} is not wearing a mask.")
