"""
Пакет vernadsky_lab — цифровий архів науково-дослідної лабораторії.

Назовні виставлено лише публічний інтерфейс: реєстрація мінералів,
запис спостережень та формування звітів. Решта — внутрішні деталі
реалізації окремих модулів.
"""

from minerals import register_mineral
from observations import record
from reports import summary, mineral_report

__all__ = ["register_mineral", "record", "summary", "mineral_report"]