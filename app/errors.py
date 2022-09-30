class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Sorry, the visitor's vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Only visitors wearing masks allowed"
