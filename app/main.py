from app.errors import (VaccineError, NotWearingMaskError)
from app.cafe import Cafe
import datetime


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    masks_to_buy = sum(1 for friend in friends if not friend["wearing_a_mask"])

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
            count += 1
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
    
# kfc = ([                   {
#                         "name": "Alisa",
#                         "vaccine": {
#                             "name": "Pfizer",
#                             "expiration_date": datetime.date.today(),
#                         },
#                         "wearing_a_mask": False,
#                     },
#                     {
#                         "name": "Bob",
#                         # "vaccine": {
#                         #     "name": "Pfizer",
#                         #     # "expiration_date": datetime.date.today(),
#                         # },
#                         "wearing_a_mask": False,
#                     },
#                 ])
#                 # Cafe("KFC"))
#                 # "All friends should be vaccinated",

# print(go_to_cafe(kfc, Cafe("KFC")))