import datetime
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")
    today = datetime.date.today()
    group_ok = [
        {"name": "Alisa", "vaccine": {
            "expiration_date": today}, "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {
            "expiration_date": today}, "wearing_a_mask": True}
    ]
    print(go_to_cafe(group_ok, kfc))

    group_no_masks = [
        {"name": "Alisa", "vaccine": {
            "expiration_date": today}, "wearing_a_mask": False},
        {"name": "Bob", "vaccine": {
            "expiration_date": today}, "wearing_a_mask": False}
    ]
    print(go_to_cafe(group_no_masks, kfc))

    group_no_vaccine = [
        {"name": "Alisa", "wearing_a_mask": True},
        {"name": "Bob", "vaccine": {
            "expiration_date": today}, "wearing_a_mask": True}
    ]
    print(go_to_cafe(group_no_vaccine, kfc))
