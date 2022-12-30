from app.errors import VaccineError, NotWearingMaskError
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    m_error = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            m_error += 1
    if m_error != 0:
        return f"Friends should buy {m_error} masks"
    else:
        return f"Friends can go to {cafe.name}"
