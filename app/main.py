import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = [
        indx + 1
        for indx, friend in enumerate(friends)
        if not friend["wearing_a_mask"]
    ]

    for friend in friends:
        try:
            if not friend["vaccine"] or friend["vaccine"]["expiration_date"] < datetime.date.today():
                raise VaccineError
        except VaccineError:
            print("All friends should be vaccinated")

        try:
            if not friend["wearing_a_mask"]:
                raise NotWearingMaskError
        except NotWearingMaskError:
            print(f"Friends should buy {masks_to_buy} masks")

    return f"Friends can go to {cafe.name}"
