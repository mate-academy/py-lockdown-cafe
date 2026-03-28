class VaccineError(Exception):

    def __str__(self) -> str:
        return f"raising {type(self).__name__}"


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    pass


class NotWearingMaskError(Exception):

    def __str__(self) -> str:
        return f"raising {type(self).__name__}"


if __name__ == "__main__":
    pass
