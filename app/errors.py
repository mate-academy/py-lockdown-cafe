class VaccineError(Exception):
    """ VaccineError """


class NotVaccinatedError(VaccineError):
    """ NotVaccinatedError """


class OutdatedVaccineError(VaccineError):
    """ OutdatedVaccineError """


class NotWearingMaskError(Exception):
    """ NotWearingMaskError """
