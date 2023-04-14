class VaccineError(Exception):
    """Parent class for NotVaccinatedError and OutdatedVaccineError"""


class NotVaccinatedError(VaccineError):
    """Throws an error if the person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Throws an error if the vaccination is overdue"""


class NotWearingMaskError(Exception):
    """Throw an error if the person does not have a protective mask"""
