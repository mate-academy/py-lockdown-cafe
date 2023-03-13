class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """If the visitor does not have a vaccine key,
     it means that he is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""
