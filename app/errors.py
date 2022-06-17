class VaccineError(Exception):

    def __str__(self):
        return "You must be vaccinated"


class NotVaccinatedError(VaccineError):

    def __str__(self):
        return "You must be vaccinated"


class OutdatedVaccineError(VaccineError):

    def __str__(self):
        return "Your vaccine out of date"


class NotWearingMaskError(Exception):

    def __str__(self):
        return "You must be in mask"
