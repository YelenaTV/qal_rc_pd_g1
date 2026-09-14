"""
Журнал наукових спостережень.


**Список `_journal`** — внутрішній, 
не доступний напряму ззовні (починається з `_`). 
Спочатку порожній.
"""

import datetime
from datetime import datetime
from minerals import get_mineral

_journal = []
def record(researcher, mineral_name, note):
    #* імпортує `get_mineral` із `minerals.py`
    #* якщо мінерал не знайдено в каталозі — повертає `"Мінерал '<mineral_name>' "
    #"не зареєстровано. Спочатку додайте його до каталогу"`
    #* інакше — додає запис до журналу у вигляді словника з полями: 
    # дослідник, мінерал, нотатка, та дата (використай `datetime.date.today()`)
    #* повертає `"Спостереження записано: <researcher> → <mineral_name>"`
    if get_mineral(mineral_name) is None:
        return f"Мінерал {mineral_name} не зареєстровано.  Спочатку додайте його до каталогу"
    _journal.append({"researcher": researcher, "mineral": mineral_name, "note": note, "date": datetime.today(),})  
    return f"Спостереження записано: {researcher} -> {mineral_name}"  

def get_observations(mineral_name=None):
    #* якщо `mineral_name` передано — повертає лише записи про цей мінерал
    #* якщо не передано — повертає всі записи журналу
    #* якщо журнал порожній або записів не знайдено — повертає порожній список
    if mineral_name is None:
        return list(_journal)
    result = []
    for mineral in _journal:
        if mineral["mineral"] == mineral_name:
            result.append(mineral)
    return result 