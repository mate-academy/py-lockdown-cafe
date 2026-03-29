class NotWearingMaskError(Exception):
    """ Exception for handling mask issue """


class VaccineError(Exception):
    """ Exception for handling vaccination issue """


class NotVaccinatedError(VaccineError):
    """ Exception for handling not vaccinated guests """


class OutdatedVaccineError(VaccineError):
    """ Exception for handling guests with outdated vaccination """
