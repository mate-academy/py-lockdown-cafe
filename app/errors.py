class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """If you are not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """If your vaccine has expired"""
    pass


class NotWearingMaskError(Exception):
    """In case you are not wearing a mask"""
    pass
