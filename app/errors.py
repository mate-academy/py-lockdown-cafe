"""
This errors.py module contains error classes
for every case the visitor can`t visit a cafe.
"""


class NotWearingMaskError(Exception):
    pass


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass
