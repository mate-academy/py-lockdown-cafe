class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You must wear a mask to enter the cafe."


class VaccineError(Exception):
    def __str__(self) -> str:
        return "Something wrong with your vaccine"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You need to be vaccinated to enter the cafe."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is outdated. Please update your vaccination."
