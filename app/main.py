import datetime

from app.cafe import Cafe
from app.errors import *


def go_to_cafe(friends: list, cafe: Cafe):
    no_mask = 0
    vaccine = True
    for visitor in friends:
        try:
            cafe.visit_cafe(visitor)
        except NotVaccinatedError as e:
            vaccine = False
        except NotWearingMaskError as e:
            no_mask += 1
        except OutdatedVaccineError as e:
            vaccine = False
    if not vaccine:
        print("All friends should be vaccinated")
    elif no_mask > 0:
        print(f"Friends should buy 2 masks")
    else:
        print(f"Friends can go to {cafe.name}")
