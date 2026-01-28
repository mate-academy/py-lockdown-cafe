class VaccineError(Exception):
    def __init(self, *args) -> None:
        super().__init__(super, args)

    def __str__(self) -> str:
        return "VaccineError"


class NotVaccinatedError(VaccineError):
    def __init(self, *args) -> None:
        super().__init__(super, args)

    def __str__(self) -> str:
        return "NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __init(self, *args) -> None:
        super().__init__(super, args)

    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __init(self, *args) -> None:
        super().__init__(super, args)

    def __str__(self) -> str:
        return "NotWearingMaskError"
