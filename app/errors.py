class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Vaccination is mandatory for visitors!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The visitor has an outdated vaccine passport!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visiting without a mask is prohibited!"
