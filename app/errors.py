class NotWearingMaskError(Exception):
    """Not all visitors wear masks"""
    pass


class VaccineError(Exception):
    """"VaccineError parent class for NotVaccinatedError
     and OutdatedVaccineError errors"""
    pass


class NotVaccinatedError(VaccineError):
    """If the visitor does not have a vaccine key, it means
    that he is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """The vaccine expired"""
    pass
