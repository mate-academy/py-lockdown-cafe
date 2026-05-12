from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: list, cafe: object):
    try:
        # On tente de faire entrer tout le monde
        for friend in friends:
            cafe.visit_cafe(friend)
        
        # Si la boucle se termine sans accroc
        return f"Friends can go to {cafe.name}"

    except VaccineError:
        # PRIORITÉ 1 : Si quelqu'un a un souci de vaccin, c'est le seul message qui compte
        return "All friends should be vaccinated"

    except NotWearingMaskError:
        # PRIORITÉ 2 : Si le vaccin est OK mais qu'il manque des masques
        # On doit recompter TOUTE la liste pour avoir le total exact
        masks_to_buy = 0
        for friend in friends:
            if friend.get("wearing_a_mask") is False:
                masks_to_buy += 1
        return f"Friends should buy {masks_to_buy} masks"
    
