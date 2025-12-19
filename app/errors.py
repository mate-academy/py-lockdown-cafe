class VaccineError(Exception):
    """Parent class for OutdatedVaccineError and NotWearingMaskError
    """
    pass


class NotVaccinatedError(VaccineError):
    """NotVaccinatedError is exception
       if visitor does not vaccinated.
    """

    def __str__(self) -> str:
        return ("You did have not been vaccinated. "
                "So you can't visit the cafe.")


class OutdatedVaccineError(VaccineError):
    """OutdatedVaccineError is exception
       if the visitor has a vaccine  that has expired.
    """

    def __str__(self) -> str:
        return ("You have a vaccine certificate that has expired. "
                "Sorry, but you can't visit the cafe.")


class NotWearingMaskError(Exception):
    """NotWearingMaskError is exception
       if visitor doesn't wear mask.
    """

    def __str__(self) -> str:
        return ("If you want to visit the cafe "
                "you should wear a mask.")
