from datetime import datetime

from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

day_today = datetime.date.today()


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:

    allowed_friends = 0

    for friend in friends:

        try:
            cafe.visit_cafe(friend)
            allowed_friends += 1

        except VaccineError as v:
            return str(v)

        except NotWearingMaskError:
            masks_to_buy = len([friend for friend in friends
                                if friend.get("wearing_a_mask") is False])
            return f"Friends should buy {masks_to_buy} masks"

    if allowed_friends == len(friends):
        return f"Friends can go to {cafe.name}"
