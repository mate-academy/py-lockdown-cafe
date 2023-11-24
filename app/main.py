import app.errors
import datetime
from app.cafe import Cafe

from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(cafe: Cafe, friends: list[dict]) -> str:

    vaccinated_friends = 0
    mask_wearing_friends = 0

    for friend in friends:
        if ("vaccine" in friend and (
            friend["vaccine"]["expiration_date"]
            >= datetime.date.today()
        )):
            vaccinated_friends += 1

        if friend["wearing_a_mask"]:
            mask_wearing_friends += 1

    try:
        if vaccinated_friends == len(friends):
            if mask_wearing_friends == len(friends):
                return f"Friends can go to {cafe.name}"
            else:
                masks_to_buy = len(friends) - mask_wearing_friends
                return f"Friends should buy {masks_to_buy} masks"
        else:
            raise VaccineError("All friends should be vaccinated")
    except VaccineError as e:
        return str(e)
