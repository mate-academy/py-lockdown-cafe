from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    count = 0
    v_error = 0
    m_error = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            v_error += 1
            count += 1
        except NotWearingMaskError:
            m_error += 1
            count += 1
    if v_error != 0:
        return "All friends should be vaccinated"
    elif m_error != 0:
        return f"Friends should buy {m_error} masks"
    elif count == 0:
        return f"Friends can go to {cafe.name}"
