class NotVaccinatedError(Exception):
    """The person is not vaccinated"""
    pass


class OutdatedVaccineError(Exception):
    """Vaccine has expired"""
    pass


class NotWearingMaskError(Exception):
    """The man has no mask"""
    pass
