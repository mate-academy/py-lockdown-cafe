class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> None:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> None:
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    pass
