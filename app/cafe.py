from datetime import datetime
from app.machine import Machine
from app.errors import (
    VaccineError,
    NotVaccinatedError,
    OutdatedVaccineError,
    NoExpirationDateError,
)


class Cafe(Machine):
    def __init__(self):
        self.is_working = False

    def do_work(self):
        self.is_working = True

    def stop_work(self):
        self.is_working = False

    def visit_cafe(self, visitor: dict):
        """Allow entry if visitor has a valid vaccine record."""
        if not visitor.get("vaccine"):
            raise NotVaccinatedError(
                f"{visitor.get('name', 'Visitor')} is not vaccinated"
            )

        vaccine = visitor.get("vaccine")
        expiration_date = vaccine.get("expiration_date")

        if not expiration_date:
            raise NoExpirationDateError(
                f"{visitor.get('name', 'Visitor')} has no vaccine expiration date"
            )

        if expiration_date < datetime.now().date():
            raise OutdatedVaccineError(
                f"{visitor.get('name', 'Visitor')}'s vaccination has expired"
            )

        return f"Welcome to the cafe, {visitor.get('name', 'Guest')}!"
