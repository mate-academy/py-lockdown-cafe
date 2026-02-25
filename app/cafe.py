import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Vaccine:
    def __init__(self, data: dict = None) -> None:
        self.expiration = None
        expiration_date = None
        if data:
            expiration_date  = data.get("expiration_date", None)
            if isinstance(expiration_date, datetime.date):
                self.expiration = expiration_date
            elif isinstance(expiration_date, str):
                try:
                    self.expiration = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
                except ValueError:
                    raise ValueError(f"Invalid date format: {expiration_date}. Expected YYYY-MM-DD.")
            else:
                self.expiration = None


class Person:
    def __init__(self, data: dict) -> None:
        self.name = ""
        self.is_in_mask = False
        self.vaccine = Vaccine()
        if data:
            self.name = data.get("name", "")
            self.is_in_mask = data.get("wearing_a_mask", False)
            self.vaccine = Vaccine(data.get("vaccine", None))


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        guest = Person(visitor)
        if guest.vaccine.expiration is None:
            raise NotVaccinatedError()

        if guest.vaccine.expiration < datetime.date.today():
            raise OutdatedVaccineError()

        if not guest.is_in_mask:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
