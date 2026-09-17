#from . import register_mineral, record, summary, mineral_report
from minerals import register_mineral
from observations import record
from reports import summary, mineral_report

print("=== Лабораторія Вернадського ===\n")

print("Реєстрація мінералів:")
print(register_mineral("Берил", "Be3Al2(SiO3)6", 7.5, "Волинь", 1798))
print(register_mineral("Кварц", "SiO₂", 7, "Урал", 1845))
print(register_mineral("Кварц", "SiO₂", 7, "Урал", 1845))

print("\nЗапис спостережень:")
print(record("Вернадський", "Берил", "прозорий кристал з чіткими гранями"))
print(record("Ферсман", "Кварц", "прозорий, без включень"))
print(record("Вернадський", "Кварц", "виражена кристалічна решітка"))
print(record("Ферсман", "Малахіт", "яскраво-зелений, шаруватий"))

print("\n=== Загальне зведення ===")
print(summary())

print("\n=== Звіт: Кварц ===")
print(mineral_report("Кварц"))
