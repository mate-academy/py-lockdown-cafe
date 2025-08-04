import datetime

from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError

"""xxx = [
                {
                    "name": "Ivan",
                    "vaccine": {
                        "name": "Moderna",
                        "expiration_date": datetime.date.today()
                        + datetime.timedelta(days=4),
                    },
                    "wearing_a_mask": True,
                },
                {
                    "name": "Oleksii",
                    "vaccine": {
                        "name": "Pfizer",
                        "expiration_date": datetime.date.today(),
                    },
                    "wearing_a_mask": True,
                },
            ]
"""

def go_to_cafe(friends: list, cafe: Cafe) -> str:
    missing_masks = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            missing_masks += 1
    if missing_masks == 0:
        return f"Friends can go to {cafe.name}"
    else:
        return f"Friends should buy {missing_masks} masks"


"""c = Cafe("gay")

print(go_to_cafe(cafe=c, friends=xxx))
"""