class VaccineError(Exception):
    def __str__(self) -> str:
        return "Access denied: Visitor is not vaccinated."


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Access denied: Visitor is not vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Access denied: Visitor vaccine is outdated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Access denied: Visitor do not have mask"
