class VaccineError(Exception):
    """Exception when person either don`t have vaccine or it`s outdated"""
    pass


class OutdatedVaccineError(VaccineError):
    """"Exception when Visitors vaccine is outdated"""
    pass


class NotVaccinatedError(VaccineError):
    """Exception when Visitor don`t have vaccine"""
    pass


class NotWearingMaskError(Exception):
    """Exception when Visitor is not wearing a mask"""
    pass
