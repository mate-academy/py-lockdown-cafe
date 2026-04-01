class VaccineError(Exception):
    """This Exception raises when there is some problems with vaccinating"""


class NotVaccinatedError(VaccineError):
    """This Exception raises when person didn't vaccinate"""


class OutdatedVaccineError(VaccineError):
    """This Exception raises when person's vaccination is out of date"""


class NotWearingMaskError(Exception):
    """This Exception raises when person don't have mask"""
