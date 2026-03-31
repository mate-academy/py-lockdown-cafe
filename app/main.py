from typing import List, Dict, Any
from datetime import date
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    vaccine_issue = False
    mask_issue_count = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            vaccine_issue = True
        except NotWearingMaskError:
            mask_issue_count += 1

    if vaccine_issue:
        return "All friends should be vaccinated"
    if mask_issue_count:
        return f"Friends should buy {mask_issue_count} masks"
    return f"Friends can go to {cafe.name}"


# --- Example usage ---
if __name__ == "__main__":
    kfc = Cafe("KFC")

    # Example: All good
    friends1 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends1, kfc))  # Expected: "Friends can go to KFC"

    # Example: Mask issues but no vaccine problems
    friends2 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": date.today()},
            "wearing_a_mask": False,
        },
    ]
    print(go_to_cafe(friends2, kfc))  # Expected: "Friends should buy 2 masks"

    # Example: Vaccine issue present
    friends3 = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "wearing_a_mask": True,
        },
    ]
    print(go_to_cafe(friends3, kfc))
