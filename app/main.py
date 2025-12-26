from app import cafe, errors

def go_to_cafe(friends: list, cafe: cafe.Cafe) -> str:
    masks_to_buy = 0
    vaccinated_friends = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.VaccineError:
            vaccinated_friends += 1
        except errors.NotWearingMaskError:
            masks_to_buy += 1

    if vaccinated_friends > 0:
        return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
