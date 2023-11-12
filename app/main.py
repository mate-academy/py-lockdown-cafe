import datetime
from app.cafe import Cafe
from app.errors import (
    VaccineError,
    OutdatedVaccineError,
    NotWearingMaskError
)


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    friend_with_no_mask = 0
    try:
        for friend in friends:
            if not friend.get("vaccine"):
                raise OutdatedVaccineError
            elif friend["vaccine"]["expiration_date"] < datetime.date.today():
                raise OutdatedVaccineError

        for friend in friends:
            if friend["wearing_a_mask"] is False:
                friend_with_no_mask += 1

        if friend_with_no_mask:
            raise NotWearingMaskError(friend_with_no_mask)

        for friend in friends:
            cafe.visit_cafe(visitor=friend)
    except VaccineError as e:
        return str(e)
    except NotWearingMaskError as e:
        e.friend_with_no_mask = friend_with_no_mask
        return str(e)
    return f"Friends can go to {cafe.name}"
