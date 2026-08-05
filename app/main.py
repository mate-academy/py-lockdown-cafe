"""
main.py

This module contains the go_to_cafe function, which checks whether a
group of friends is allowed to visit a cafe.
"""

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    """
    Check whether a group of friends can visit a cafe together.

    :param friends: list of dict, each dict describes a visitor.
    :param cafe: Cafe, the cafe the friends want to visit.
    :return: str, a message describing the outcome:
        - "All friends should be vaccinated" if at least one friend
          has a vaccine problem (missing or outdated vaccine).
        - "Friends should buy {masks_to_buy} masks" if everyone is
          vaccinated but some friends aren't wearing masks.
        - "Friends can go to {cafe.name}" if everyone is allowed in.
    """
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

    return f"Friends can go to {cafe.name}"
