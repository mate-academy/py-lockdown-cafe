"""
This main.py module is checking a group of visitors
for some cafe. Function takes a list of visitors
and an instance of cafe, and checks, if every
visitor has a vaccine with correct expiration
date, and wearing a mask when he is going to visit
the cafe. If masks for visitors needed - function
returns some quantity of masks to buy. If all is
OK - function tells it.
"""

from app.errors import NotWearingMaskError, \
    VaccineError


def go_to_cafe(friends, cafe):
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return "Friends can go to KFC"
