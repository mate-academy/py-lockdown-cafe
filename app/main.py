import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

day_today = datetime.date.today()


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    for friend in friends:

        try:
            cafe.visit_cafe(friend)

        except VaccineError as v:
            return str(v)

        except NotWearingMaskError:
            pass

    for friend in friends:
        try:
            cafe.visit_cafe(friend)

        except NotWearingMaskError as n:
            masks_to_buy = len([friend for friend in friends
                                if friend.get("wearing_a_mask") is False])
            return str(n) + f"{masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
