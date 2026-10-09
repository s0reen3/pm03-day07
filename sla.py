"""Расчёт просрочки по учебным правилам SLA."""
return elapsed >= LIMITS[priority]

def is_overdue(elapsed_minutes, priority="normal"):
    if elapsed_minutes < 0:
        raise ValueError("Время не может быть отрицательным")
    if priority not in LIMITS:
        raise ValueError("Неизвестный приоритет")
    return elapsed_minutes > LIMITS[priority]
