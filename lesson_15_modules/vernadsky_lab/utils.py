"""Допоміжні інструменти для роботи з каталогом мінералів."""

from minerals import MINERAL_CATALOG

def hardest_minerals(n=3):
    #* імпортує `MINERAL_CATALOG` із `minerals.py`
    #* повертає список назв `n` найтвердіших мінералів за шкалою Мооса (за спаданням)
    sorted_names = sorted(MINERAL_CATALOG, key =lambda name: MINERAL_CATALOG[name]['hardness'], ##сортуємо не за назвами, а за значеннями твердості.
    reverse=True,) ##сортувати за спаданням (від більшого до меншого)
    return sorted_names[:n]   #від найтвердішого до найм'якшого

def search_by_origin(origin_keyword):
    #* повертає список назв мінералів, у полі `origin` яких зустрічається `origin_keyword` (без урахування регістру)
    #* якщо нічого не знайдено — порожній список
    keyword = origin_keyword.lower()
    result = []

    for name, data in MINERAL_CATALOG.items():   
        # - перебираємо пари (name, data) у словнику MINERAL_CATALOG;
        # - для кожного мінералу перевіряємо, чи є keyword у полі origin (також у нижньому регістрі);
        # - якщо так — додаємо назву мінералу name до результуючого списку.
        if keyword in data["origin"].lower():
            result.append(name)

    return result