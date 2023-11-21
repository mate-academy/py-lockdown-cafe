# write your code here



import datetime

kfc = Cafe("KFC")
visitor = {
    "name": "Paul",
    "age": 23,
    "vaccine": {
        "expiration_date": datetime.date(year=2019, month=2, day=23)
    }
}
kfc.visit_cafe(visitor)     # OutdatedVaccineError