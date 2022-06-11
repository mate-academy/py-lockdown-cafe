class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, messange="NotVaccinatedError"):
        super().__init__(messange)


class OutdatedVaccineError(VaccineError):
    def __init__(self, messange="OutdatedVaccineError"):
        super().__init__(messange)


class NotWearingMaskError(Exception):
    def __init__(self, messange="NotWearingMaskError"):
        super().__init__(messange)
