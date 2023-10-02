class NotWearingMaskError(Exception):
    """
    Idk(I don't know), what i
    must to write here
    """
    pass


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass
