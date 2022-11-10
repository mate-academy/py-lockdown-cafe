class VaccineError(Exception):
    def __str__(self) -> str:
        return "You need to be vaccinated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "You should buy masks"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass
