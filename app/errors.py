class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message="Sorry, you can't visit cafe without vaccine"):
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="Sorry, your vaccine's expired"):
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="Sorry, all cafe visitors should wear masks"):
        super().__init__(message)
