class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Go to the hospital and get vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is out of date, go for an update"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Friends should buy"
