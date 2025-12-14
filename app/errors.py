class VaccineError(Exception):
    def __str__(self) -> str:
        return "You will die without vaccine!!!"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Your are not vaccinated, please visit a doctor"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Your vaccine is out of terms, please visit a doctor"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Go to a pharmacy and buy the mask"
