class VaccineError(Exception):
    def __str__(self) -> str:
        return "The visitor has vaccine issue"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The visitor do not take vaccine!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The visitor vaccine is outdated!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The visitor do not wear a mask!"
