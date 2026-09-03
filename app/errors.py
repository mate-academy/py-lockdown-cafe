class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """ Exception if key not found """


class OutdatedVaccineError(VaccineError):
    """ Exception if data of vaccine is expired """


class NotWearingMaskError(Exception):
    """ Exception if wearing mask is False """
