class VaccineError(Exception):
    def __str__(self) -> str:
        return "There are some problems with your vaccine"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should be vaccinated to visit cafes"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is expired, you can't visit cafes"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should wear a mask to visit cafes"
