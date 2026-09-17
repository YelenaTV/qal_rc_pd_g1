"""
Формування наукових звітів на основі каталогу мінералів
та журналу спостережень.
"""
from minerals import MINERAL_CATALOG
from observations import get_observations

def summary():
    observations = get_observations()

    minerals_in_count = len(MINERAL_CATALOG) #* кількість мінералів у каталозі
    observations_count = len(observations)   #* кількість спостережень у журналі
    if not observations:
        no_observation = "Спостережень ще немає"
    else:
        counts = {} # Створюємо порожній словник для підрахунку кількості записів кожного дослідника
        for i in observations:
            researcher = i["researcher"]
            counts[researcher] = counts.get(researcher,0) + 1
        
        max_researcher = max(counts, key=counts.get)   #Знаходимо дослідника з максимальною кількістю записів
        max_count = counts[max_researcher]
        no_observation = f"Найактивніший дослідник: {max_researcher} ({max_count} записи)"
    return ( 
        f"Мінералів у каталозі: {minerals_in_count}\n"
        f"Спостережень у журналі: {observations_count}\n"
        f"{no_observation}"
    )
def mineral_report(name):
    #"Повертає повний звіт по одному мінералу."
    data = MINERAL_CATALOG.get(name)
    if data is None:
        return f"Мінерад {name} відсутній у каталозі"
    lines = [
        f"Формула: {data['formula']} | Твердість: {data['hardness']} | "
        f"Походження: {data['origin']} | Відкрито: {data['discovered']}",
        "Спостереження:",
    ]
    observation = get_observations(name)
    if not observation:
        lines.append("   (спостережень немає)")
    else:
        for obs in observation:
            lines.append(f"  [{obs['date']}] {obs['researcher']}: {obs['note']}")
    return "\n".join(lines)