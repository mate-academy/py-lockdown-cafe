class VaccineError(Exception):
    """Parent class for all errors connected with vaccination"""


class NotWearingMaskError(Exception):
    """Pops up if visitor does not wear a mask"""


class NotVaccinatedError(VaccineError):
    """Pops up if visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Pops up if visitor has outdated vaccination and
    needs to carry out procedure again"""
