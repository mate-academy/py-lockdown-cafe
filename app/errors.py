class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Attention! Walking without a vaccine is a criminal offense!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Danger! You need to inject again."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Disaster! Without a mask you are a murderer!"
