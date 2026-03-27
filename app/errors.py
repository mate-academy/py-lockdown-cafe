class VaccineError(Exception):
    def __str__(self) -> str:
        return "All visitors should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Someone is not vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "All visitors should wear masks"
