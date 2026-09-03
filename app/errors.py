class NotVaccinatedError(Exception):
    """ Exception if key not found """


class OutdatedVaccineError(Exception):
    """ Exception if data of vaccine is expired """


class NotWearingMaskError(Exception):
    """ Exception if wearing mask is False """
