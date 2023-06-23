from app.errors import VaccineError
import datetime


def go_to_cafe(friends: dict, cafe: str) -> str:
    masks_needed = 0
    expiration_1 = 0
    for friend in friends:
        try:
            if "vaccine" in friend and "expiration_date" in friend["vaccine"]:
                expiration_date = friend["vaccine"]["expiration_date"]
                if (
                    expiration_date >= datetime.date.today()
                    and not friend["wearing_a_mask"]
                ):
                    masks_needed += 1

                elif expiration_date < datetime.date.today():
                    expiration_1 += 1
                    return "All friends should be vaccinated"
            else:
                raise VaccineError(
                    "All friends should be vaccinated"
                )
        except VaccineError:
            return "All friends should be vaccinated"

    try:
        if masks_needed == 0:
            return "Friends can go to {}".format(cafe.name)
        elif expiration_1 > 0:
            raise VaccineError(
                "All friends should be vaccinated"
            )
        else:
            return (
                "Friends should buy {} mask{}".
                format(masks_needed, "s" if masks_needed > 1 else "")
            )
    except VaccineError:
        return "All friends should be vaccinated"
   