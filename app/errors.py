class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should get vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Unfortunately, your vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should wear a mask!"
