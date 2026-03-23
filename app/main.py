from app.cafe import Cafe
from app.errors import VaccineError
from datetime import date, timedelta


def main():
    cafe = Cafe()

    visitor = {
        "name": "Alice",
        "vaccine": {
            "name": "Pfizer",
            "expiration_date": date.today() + timedelta(days=30),
        },
    }

    try:
        cafe.do_work()
        message = cafe.visit_cafe(visitor)
        print(message)
    except VaccineError as error:
        print(error)
    finally:
        cafe.stop_work()


if __name__ == "__main__":
    main()
