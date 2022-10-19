class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "You should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Your vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "Not allowed to enter without a mask"
