class VaccineError(Exception):
    def __str__(self):
        return "Error: VaccineError"

class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "Error: Person is not vaccinated"

class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Error: Vaccine is outdated"

class NotWearingMaskError(Exception):
    def __str__(self):
        return "Error: Person doesn't wear mask"
