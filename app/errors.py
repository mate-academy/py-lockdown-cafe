class VaccineError(Exception):
    """ Vaccine problem """


class NotVaccinatedError(VaccineError):
    """ Not vaccinated """

    def __str__(self) -> str:
        return "please do vaccine"


class OutdatedVaccineError(VaccineError):
    """ take a new vaccine """
    def __str__(self) -> str:
        return "Please retake vaccine"


class NotWearingMaskError(Exception):
    """ Wear a your's musk """
    def __str__(self) -> str:
        return "Pls wear a mask"
