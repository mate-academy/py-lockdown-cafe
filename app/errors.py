class VaccineError(Exception):
    """All friends should be vaccinated"""
    pass


class NotVaccinatedError(VaccineError):
    """Everyone should have the vaccine"""
    pass


class OutdatedVaccineError(VaccineError):
    """The vaccine should be with the normal term"""
    pass


class NotWearingMaskError(Exception):
    """All guests must wear masks"""
    pass
