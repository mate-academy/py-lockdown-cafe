import datetime
from cafe import Cafe
from errors import NotVaccinatedError
from errors import OutdatedVaccineError
from errors import NotWearingMaskError
import datetime

def go_to_cafe(friends: list, cafe: Cafe) -> str:
