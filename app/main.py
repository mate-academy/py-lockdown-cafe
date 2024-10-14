import datetime
from typing import List, Dict, Any
from app.cafe import Cafe


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    for friend in friends:
        if "vaccine" not in friend:
            return "All friends should be vaccinated"

    not_vaccinated_count = sum(
        1 for friend in friends
        if friend["vaccine"]["expiration_date"] < datetime.date.today())
    mask_needed_count = sum(
        1
        for friend in friends
        if not friend.get("wearing_a_mask", True))

    if not_vaccinated_count > 0:
        return "All friends should be vaccinated"

    if mask_needed_count > 0:
        if mask_needed_count == 1:
            return f"Friends should buy {mask_needed_count} mask"
        else:
            return f"Friends should buy {mask_needed_count} masks"

    return f"Friends can go to {cafe.name}"


if __name__ == "__main__":
    kfc = Cafe("KFC")

    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
    ]
    print(go_to_cafe(friends, kfc))
    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": False
        },
    ]
    print(go_to_cafe(friends, kfc))

    friends = [
        {
            "name": "Alisa",
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
    ]
    print(go_to_cafe(friends, kfc))
