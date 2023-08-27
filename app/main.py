from app.errors import NotVaccinatedError, NotWearingMaskError


def go_to_cafe(friends, cafe):
    try:
        all_wearing_masks = all(friend.get("wearing_a_mask", False) for friend in friends)

        if 'vaccine' not in friends:
            raise NotVaccinatedError("All friends should be vaccinated")

        if not all_wearing_masks:
            masks_to_buy = sum(not friend.get("wearing_a_mask", False) for friend in friends)
            raise NotWearingMaskError(f"Friends should buy {masks_to_buy} masks")

        return f"Friends can go to {cafe.name}"
    except NotVaccinatedError as e:
        return str(e)
    except NotWearingMaskError as e:
        return str(e)



