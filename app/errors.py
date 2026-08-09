class VaccineError(Exception):
    """Main vaccine error class"""
    pass


class NotVaccinatedError(VaccineError):
    """Raise when the visitor is not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """Raise when the vaccine is outdated"""
    pass


class NotWearingMaskError(Exception):
    """Raise when the visitor is not wearing mask"""
    pass
