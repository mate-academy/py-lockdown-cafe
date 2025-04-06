class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Visitor's vaccine has expired"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Friends should buy masks"
