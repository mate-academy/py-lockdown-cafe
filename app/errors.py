class VaccineError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NotVaccinatedError(VaccineError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class OutdatedVaccineError(VaccineError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NotWearingMaskError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
