import datetime


def go_to_cafe(friends: list, cafe: dict) -> str:
    vaccinated_friends = sum(
        1 for friend in friends if friend.get("vaccine")
        and friend["vaccine"]["expiration_date"] >= datetime.date.today())
    wearing_mask_friends = sum(
        1 for friend in friends if friend.get("wearing_a_mask", False))

    if vaccinated_friends != len(friends):
        return "All friends should be vaccinated"

    if wearing_mask_friends != len(friends):
        return (
            f"Friends should buy {len(friends) - wearing_mask_friends} "
            "masks"
        )


    return f"Friends can go to {cafe.name}"
