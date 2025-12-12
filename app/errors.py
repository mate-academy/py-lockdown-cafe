class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All friends must wear masks."
