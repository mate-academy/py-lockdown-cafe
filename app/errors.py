class VaccineError(Exception):
    def __str__(self) -> str:
        return "All visitors should be vaccinated and with proper date"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All visitors should be with masks"
