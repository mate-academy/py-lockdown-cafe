class VaccineError(Exception):
    def __init__(self, mess: str = None) -> None:
        self.mess = mess

    def __str__(self) -> str:
        return self.mess


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, mess: str = None) -> None:
        self.mess = mess

    def __str__(self) -> str:
        return self.mess
