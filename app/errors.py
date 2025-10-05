class VaccineError(Exception):
    ...


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor must be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Visitor's vaccinate is outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor must wear a mask!"
