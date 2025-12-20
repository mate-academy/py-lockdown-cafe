class NotWearingMaskError(Exception):
    """
    Not wearing mask
    """


class VaccineError(Exception):
    """
    Main vaccine error check class
    """


class NotVaccinatedError(VaccineError):
    """
    Not vaccinated
    """


class OutdatedVaccineError(VaccineError):
    """
    Outdated vaccine
    """
