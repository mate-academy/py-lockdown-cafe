class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "Visitor must be vaccinated to enter the cafe."


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Visitor must wear a mask."

