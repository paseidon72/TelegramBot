
"""Модуль налаштовує та оновлює графічний інтерфейс і події програми."""


class Configure_widjets:
    """
    Клас налаштовує та оновлює графічний інтерфейс і
    події програми.
    """

    def configure_cpu_bar(self):
        """
        Оновіть віджети завантаження процесора та оперативної пам’яті
        головне вікно.
        """
        r = self.cpu.cpu_percent_return()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i + 1} usage: {r[i]}%')
            self.list_pbar[i].configure(value=r[i])

        r2 = self.cpu.ram_usage()
        self.ram_lab.configure(text=f'RAM usage: {r2[2]}%, used: {round(r2[3]/1048576)} Mb,\
         \n available: {round(r2[1]/1048576)} Mb')
        self.ram_bar.configure(value=r2[2])
        self.wheel = self.after(1000, self.configure_cpu_bar)

    def configure_win(self):
        """Відновлює або приховує віконну раму."""
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()

    def clear_win(self):
        """Видалення віджетів."""
        for i in self.winfo_children():
            i.destroy()

    def configure_minimal_win(self):
        """Оновлення невеликого вікна віджетів завантаження процесора та оперативної пам’яті."""
        self.bar_one.configure(value=self.cpu.cpu_one_return())
        self.ram_bar.configure(value=self.cpu.ram_usage()[2])
        self.wheel = self.after(1000, self.configure_minimal_win)
