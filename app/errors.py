class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return "No vaccine no cafe!"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return "Vaccine is expired!"


class NotWearingMaskError(Exception):
    def __str__(self):
        return "No musk no fries"
