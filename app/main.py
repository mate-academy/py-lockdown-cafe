"""
This module contains the main function for the lockdown cafe application.
"""
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """
    Simulates a group of friends going to a cafe.

    This function checks if each friend in the group can enter the cafe. If
    any friend is not vaccinated, the function returns a message that all
    friends should be vaccinated. If any friend is not wearing a mask, the
    function counts the number of masks to buy and returns a message with
    the number of masks to buy. If all friends meet the requirements, the
    function returns a message that the friends can go to the cafe.

    :param friends: A list of dictionaries, where each dictionary
                    represents a friend.
    :type friends: list[dict]
    :param cafe: A Cafe object representing the cafe.
    :type cafe: Cafe
    :return: A message indicating whether the friends can go to the cafe.
    :rtype: str
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
