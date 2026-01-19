class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should wear a mask"
