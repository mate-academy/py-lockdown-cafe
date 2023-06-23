class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Friends should buy {} mask(s)"
