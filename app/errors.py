class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "No mask — no pass"


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Can not enter if not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Vaccine has expired, can not enter"
