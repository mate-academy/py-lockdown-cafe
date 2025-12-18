import datetime


def go_to_cafe(friends: list, cafe: any, wearing_a_mask: bool = False) -> str:
    all_vaccinated = True
    mask_needed_count = 0

    for friend in friends:
        if (
                "vaccine" not in friend
                or friend["vaccine"]["expiration_date"] < datetime.date.today()
        ):
            all_vaccinated = False

        if not friend.get("wearing_a_mask", False):
            mask_needed_count += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"
    if mask_needed_count > 0:
        return f"Friends should buy {mask_needed_count} masks"

    return f"Friends can go to {cafe.name}"
