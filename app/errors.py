class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):

    def __str__(self) -> str:
        return "Visitor is not vaccinated!"


class OutdatedVaccineError(VaccineError):

    def __str__(self) -> str:
        return "Your vaccine is expired! Go get another shot."


class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return ("We all know that you're handsome, "
                "but this time you need to cover your face with a mask")
