import datetime


def go_to_cafe(friends: list, cafe):
    masks_to_buy = 0
    today = datetime.datetime.now().date()

    for friend in friends:
        if "vaccine" in friend:
            if friend["vaccine"]["expiration_date"] >= today:
                if friend["wearing_a_mask"] is False:
                    masks_to_buy += 1
            else:
                return "All friends should be vaccinated"
        else:
            return "All friends should be vaccinated"

    if masks_to_buy == 0:
        return f"Friends can go to {cafe.name}"
    return f"Friends should buy {masks_to_buy} masks"
