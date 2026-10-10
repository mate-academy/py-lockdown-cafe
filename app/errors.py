class VaccineError(Exception):
    def __str__(self) -> str:
        return "Vaccine Error"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Not Vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Outdated Vaccine"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Not Wearing Mask"
