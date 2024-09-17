class VaccineError(Exception):
    """Check vaccination condition"""
    pass


class NotVaccinatedError(VaccineError):
    """Raise vaccination error if not present"""
    pass


class OutdatedVaccineError(VaccineError):
    """Raise error if vaccine expired"""
    pass


class NotWearingMaskError(Exception):
    """Raise error is mask not present"""
    pass
