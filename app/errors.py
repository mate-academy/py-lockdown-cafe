class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "The guest has not been vaccinated."


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "The guest does not have a valid vaccination."


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Visitor does not have a mask"
