import tkinter as tk


class AnimatedCircle(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Создаем круг
        self.circle = self.create_oval(10, 10, 50, 50, fill="yellow")

        # Запускаем анимацию
        self.animate()

    def animate(self):
        # Анимация движения круга
        self.move(self.circle, 1, 0)
        self.after(20, self.animate)


# Основной класс приложения
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настраиваем окно
        self.title("Animated Circle")
        self.geometry("300x200")

        # Создаем экземпляр класса анимации
        self.animated_circle = AnimatedCircle(self)
        self.animated_circle.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()