class QuarantineError(Exception):
    def __str__(self) -> str:
        return "Quarantine rules violation! Don't joke about that!"


class NotWearingMaskError(QuarantineError):
    def __str__(self) -> str:
        return "Please, wear a mask... IMMEDIATELY!"


class VaccineError(QuarantineError):
    def __str__(self) -> str:
        return "Something wrong with your vaccination!"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "You're not vaccinated yet!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "You should get vaccinated. AGAIN!"
