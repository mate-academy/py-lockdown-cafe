class VaccineError(Exception):
    """Main class for all Vaccine related errors."""


class NotVaccinatedError(VaccineError):
    """This option is disabled when a user
    or object does not have the required vaccination."""


class OutdatedVaccineError(VaccineError):
    """This option is disabled when a user
    or object has the required vaccination."""


class NotWearingMaskError(Exception):
    """This option is disabled when a user
    or object does not have the required mask."""
