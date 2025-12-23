class VaccineError (Exception):
    def __init__(self, message : str = "VaccineError") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Visitor is not vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "Visitor is not vaccinated."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Mask Error"
