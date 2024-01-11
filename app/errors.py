class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor should be vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor should be wearing a mask!"
