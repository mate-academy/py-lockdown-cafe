class VaccineError(Exception):
    """This Exception raises when there is some problems with vaccinating"""
    def __init__(self, *args: object) -> None:
        super().__init__(args)
#   What is "Unnecessary here", I didn't get it.


class NotVaccinatedError(VaccineError):
    """This Exception raises when person didn't vaccinate"""
    pass


class OutdatedVaccineError(VaccineError):
    """This Exception raises when person's vaccination is out of date"""
    pass


class NotWearingMaskError(Exception):
    """This Exception raises when person don't have mask"""
    def __init__(self, *args: object) -> None:
        super().__init__(args)
