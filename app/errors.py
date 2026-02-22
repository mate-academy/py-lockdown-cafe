import datetime

class VaccineError(Exception):
    pass

class NotVaccinatedError(VaccineError):
    def __init__(self, visitor_name):
        super().__init__(f"{visitor_name} is not vaccinated!")

class OutdatedVaccineError(VaccineError):
    def __init__(self, visitor_name, expiration_date):
        super().__init__(f"{visitor_name}'s vaccine expired on {expiration_date}!")

class NotWearingMaskError(Exception):
    def __init__(self, visitor_name):
        super().__init__(f"{visitor_name} is not wearing a mask!")
