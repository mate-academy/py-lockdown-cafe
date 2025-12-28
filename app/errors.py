class VaccineError(Exception):
    def __str__(self) -> str:
        return "All friends should be vaccinated"


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"

    """This error will raise, when someone wouldn't been vaccinated"""


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "All friends should be vaccinated"

    """This error will raise, when vaccine's expire date"""


class NotWearingMaskError(Exception):
    """This error will raise, when someone, wouldn't wearing mask"""

    def __str__(self) -> str:
        return "Not wearing a mask"
