from __future__ import annotations


class NotWearingMaskError(Exception):
    pass


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass
