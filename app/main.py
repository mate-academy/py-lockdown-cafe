from app.cafe import * 


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    mask = 0
    for i in friends:
        try:
            cafe.visit_cafe(i)
        except (NotVaccinatedError, OutdatedVaccineError) as e:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask += 1
            
    if mask:
        return f"Friends should buy {mask} masks"
    
    return "Friends can go to KFC"