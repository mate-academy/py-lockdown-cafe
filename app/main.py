from app.cafe import Cafe
from app.errors import VaccineError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0
    try:
        for friend in friends:
            if "vaccine" not in friend:
                from app.errors import NotVaccinatedError
                raise NotVaccinatedError
            import datetime
            if friend["vaccine"]["expiration_date"] < datetime.date.today():
                from app.errors import OutdatedVaccineError
                raise OutdatedVaccineError
    except VaccineError:
        return "All friends should be vaccinated"
    for friend in friends:
        if not friend.get("wearing_a_mask"):
            masks_to_buy += 1
    if masks_to_buy:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
