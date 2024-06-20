from datetime import date
from app.cafe import Cafe
from app.errors import NotWearingMaskError, VaccineError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = sum(not friend.get("wearing_a_mask", False)
                       for friend in friends)
    vaccinated_friends = [friend for friend in friends
                          if friend.get("vaccine")
                          and friend["vaccine"]["expiration_date"]
                          >= date.today()]

    if len(vaccinated_friends) != len(friends):
        return "All friends should be vaccinated"

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"
    except VaccineError:
        return "All friends should be vaccinated"

    return f"Friends can go to {cafe.name}"
