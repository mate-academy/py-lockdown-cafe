class VaccineError(Exception):
    def __init__(self,
                 message: str = "Everyone need's to be vaccinated") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The person in not vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The vaccine is expired!"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "The person does not wearing the mask!"
