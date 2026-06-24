class CafeValidationError(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(f"{name} {self.message_suffix}")


class VaccineError(CafeValidationError):
    pass


class NotVaccinatedError(VaccineError):
    message_suffix = "not vaccinated"


class OutdatedVaccineError(VaccineError):
    message_suffix = "vaccines out date"


class NotWearingMaskError(CafeValidationError):
    message_suffix = "not wearing mask"
