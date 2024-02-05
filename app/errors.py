class VaccineError(Exception):
    """ """


class NotVaccinatedError(VaccineError):
    """ """


class OutdatedVaccineError(VaccineError):
    """ """


class NotWearingMaskError(Exception):
    """ """
