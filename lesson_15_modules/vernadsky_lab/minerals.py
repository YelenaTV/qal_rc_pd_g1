MINERAL_CATALOG = {
    "Кварц": {
        "formula": "SiO2",
        "hardness": 7,
        "origin": "Україна",
        "discovered": 1845,
    },
    "Сіль": {
        "formula": "NaCl",
        "hardness": 2.5,
        "origin": "Донбас",
        "discovered": 1760,
    },
    "Гіпс": {
        "formula": "CaSO4·2H2O",
        "hardness": 2,
        "origin": "Крим",
        "discovered": 1790,
    },
    "Крейда": {
        "formula": "CaCO3",
        "hardness": 1,
        "origin": "Поділля",
        "discovered": 1800,
    },
    "Пірит": {
        "formula": "FeS2",
        "hardness": 6,
        "origin": "Карпати",
        "discovered": 1825,
    },
}
def get_mineral(name):  #* повертає словник із даними про мінерал
                        #* якщо не знайдено — повертає `None`
    return MINERAL_CATALOG.get(name)

def register_mineral(name, formula, hardness, origin, discovered):
    #* додає новий мінерал до каталогу
    #* якщо такий вже є — повертає `"Мінерал '<name>' вже зареєстровано в каталозі"`
    #* якщо `hardness` поза межами 1–10 — повертає `"Некоректна твердість: має бути від 1 до 10"`
    #* інакше — повертає `"Мінерал '<name>' додано до каталогу"`
    if name in MINERAL_CATALOG:
        return f"Мінерал '{name}' вже зареєстровано в каталозі"
    if hardness < 1 or hardness >10:
        return "Некоректна твердість: має бути від 1 до 10"

    MINERAL_CATALOG[name] = {
        "formula": formula,
        "hardness": hardness,
        "origin": origin,
        "discovered": discovered,
    }
    return f"Мінерал '{name}' додано до каталогу"


result = register_mineral(
    name="Кварц",
    formula="SiO2",
    hardness=7,
    origin="Україна",
    discovered=1845
)

print(result)  # тепер OK