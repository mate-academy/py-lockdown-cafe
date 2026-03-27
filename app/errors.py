class VaccineError(ValueError):
    pass


class NotWearingMaskError(ValueError):
    """Visitor is not wear mask. All visitors must wear masks!"""
    pass


class OutdatedVaccineError(VaccineError):
    """Outdated vaccine. Visitor must be vaccinated!"""
    pass


class NotVaccinatedError(VaccineError):
    """Visitor is not vaccinate."""
    pass
