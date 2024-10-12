class VaccineError(Exception):
    """ Visitor has problem with vaccine """


class NotVaccinatedError(VaccineError):
    """ Visitor is not vaccinated """


class OutdatedVaccineError(VaccineError):
    """ The vaccine is expired """


class NotWearingMaskError(Exception):
    """ Visitor without mask """
