from app.errors import NotWearingMaskError
from app.errors import VaccineError
from app.cafe import Cafe
import datetime


def go_to_cafe(
        cafe: Cafe,
        friends: list,
        cafe_name: str = "KFC"
) -> str:
    masks_to_buy = 0
    all_vaccinated = True

    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

        vaccine_info = friend["vaccine"]
        expiration_date = vaccine_info.get("expiration_date")

        if expiration_date and \
                expiration_date < datetime.date.today():
            all_vaccinated = False

        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    if not friends:
        return f"Friends can go to {cafe_name}"

    if not all_vaccinated:
        return "All friends should be vaccinated"

    return f"Friends can go to {cafe_name}"
