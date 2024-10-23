class VaccineError(Exception):
    """ A template error for inherited classes 'NotVaccinatedError'
    and 'OutdatedVaccineError' """


class NotVaccinatedError(VaccineError):
    """Raises if visitor don't have a 'vaccine' key in 'visitor' dict"""
    def __str__(self) -> str:
        return "The visitor not vaccinated"


class OutdatedVaccineError(VaccineError):
    """Raises if visitor's vaccine date has expired"""
    def __str__(self) -> str:
        return "The visitor has vaccine but with expired date"


class NotWearingMaskError(Exception):
    """Raises if visitor don't wear a mask"""
    def __str__(self) -> str:
        return "The visitor don't wear the mask"
