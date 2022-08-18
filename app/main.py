from app.errors \
    import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe):
    count = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            count += 1
    if count > 0:
        return f"Friends should buy {count} masks"
    return f"Friends can go to {cafe.name}"
