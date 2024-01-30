class VaccineError(Exception):
    """ error """


class NotVaccinatedError(VaccineError):
    """ no vaccine error"""


class OutdatedVaccineError(VaccineError):
    """ Outdated Vaccine Error """


class NotWearingMaskError(Exception):
    """ no mask error"""
