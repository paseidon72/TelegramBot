"""
Модуль зчитує індикатори завантаження процесора та оперативної пам'яті.
Якщо psutil не встановлено, введіть команду в командному рядку:
pip install psutil
"""

import psutil as pt


class CpuBar():
    """Read CPU and RAM usage."""

    def __init__(self):
        """Число фізичне і логічне CPU cores."""
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def cpu_percent_return(self):
        """Читає навантаження CPU cores."""
        return pt.cpu_percent(percpu=True)

    def cpu_one_return(self):
        """Читає total CPU usage."""
        return pt.cpu_percent()

    def ram_usage(self):
        """Читає навантаження RAM."""
        return pt.virtual_memory()
