from datetime import datetime

from app.cafe import Cafe
from app.errors import (VaccineError,
                        NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)

day_today = datetime.date.today()



