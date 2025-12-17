class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You must be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine has been outdated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should wear a mask"
