class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self):
        return f"Visitor is not vaccinated and cannot enter the cafe"


class OutdatedVaccineError(VaccineError):
    def __str__(self):
        return f"Visitors vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self):
        return f"Visitor is not wearing mask and cannot enter the cafe"