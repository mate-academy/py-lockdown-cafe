class VaccineError(Exception):
    """All must be vaccinated."""
    pass


class NotVaccinatedError(VaccineError):
    """If the visitor does not have
     a vaccine key, it means that he is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired."""
    pass


class NotWearingMaskError(Exception):
    """All visitors must wear masks."""
    pass
