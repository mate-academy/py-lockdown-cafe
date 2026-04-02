# app/main.py

# Utiliza importações relativas para funcionar dentro do pacote 'app'
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    """
    Determina se um grupo de amigos pode ir a um café.

    Verifica cada amigo de acordo com as regras de entrada do café,
    usando um bloco try/except para lidar com as exceções.

    Retorna:
        - Uma mensagem de sucesso se todos puderem entrar.
        - Uma mensagem para se vacinarem se alguém tiver um problema de vacina.
        - Uma mensagem para comprar máscaras se todos estiverem vacinados,
          mas alguns não tiverem máscaras.
    """
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        # Usa a classe pai VaccineError para capturar ambos os erros de vacina
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"


# Este bloco permite que o script seja executado diretamente para fins de teste
if __name__ == "__main__":
    # A importação do datetime foi movida para cá, pois só é usada
    # para criar os dados dos exemplos neste bloco de teste.
    import datetime

    kfc = Cafe("KFC")

    # Exemplo 1 do PDF: Todos podem entrar
    compliant_friends = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(f"Resultado 1: {go_to_cafe(compliant_friends, kfc)}")

    # Exemplo 2 do PDF: Faltam máscaras
    friends_without_masks = [
        {
            "name": "Alisa",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": False,
        },
    ]
    print(f"Resultado 2: {go_to_cafe(friends_without_masks, kfc)}")

    # Exemplo 3 do PDF: Problema com vacina
    friends_with_vaccine_issue = [
        {
            "name": "Alisa",
            "wearing_a_mask": True
        },  # Não tem a chave "vaccine"
        {
            "name": "Bob",
            "vaccine": {"expiration_date": datetime.date.today()},
            "wearing_a_mask": True,
        },
    ]
    print(f"Resultado 3: {go_to_cafe(friends_with_vaccine_issue, kfc)}")
