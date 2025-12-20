class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is outdated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Friends should buy masks"
