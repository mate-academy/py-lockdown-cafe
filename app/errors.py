class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return "Visitor doesn't have a mask!"


class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return "Unfortunately visitor's 'vaccine' has expired!"


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return "Visitor has not been vaccinated!"
