from datetime import datetime, timedelta


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "Each person should be vaccinated!"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return (f"Your vaccine has to not be expired! "
                f"Current minimum requirement date to it should be: "
                f"{datetime.now() + timedelta(1)}")


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Each person should wear a mask!"
