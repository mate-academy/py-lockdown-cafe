class VaccineError(Exception):
    def __str__(self):
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Excited vaccine date"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Friends should be in masks"
