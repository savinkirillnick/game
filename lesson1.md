# Урок 1 – Запуск окна
Начнем с того, что нам понадобится создать три файла:
- `main.py`
- `class_gui.py`
- `class_controller.py`

Теперь прописываем код:

`class_gui.py` отвечает за отображение информации на экране

    import pygame
    
    class Gui:
        def __init__(self):
            # Инициируем модуль
            pygame.init()
            # Задаем размеры окна
            pygame.display.set_mode(320, 240)
    
        def update(self):
            # Перехватываем события (нажатия клавиш)
            for e in pygame.event.get():
                # Если срабатывает событие закртытия окна, то выходим из игры
                if e.type == pygame.QUIT:
                    exit()
            # Обновляем картинку
            pygame.display.update()

`class_controller.py` отвечает за работу основного цикла.

    from class_gui import *

    class Controller:
        def __init__(self):
            self.gui = Gui()

        def run(self):
            # Запускаем бесконечный цикл и проводим обновление экрана
            while 1:
                self.gui.update()

`main.py` запускной файл

    import pygame
    
    from class_controller import *
    
    
    if __name__ == '__main__':
        
        # Создаем объект класса Controller и вызываем метод run()
        controller = Controller()
        controller.run()

Запускаем `main.py` и получаем черное окно.

![Черное окно](/images/1-0-1.jpg)

---

# Урок 1.1 – Настройки окна

Настройки окна прописываем в классе `Controller`. Переписываем функцию `__init__(self):`

    class Controller:
        def __init__(self):
            # Задаем ширину окна в тайлах
            self.width = 16
            # Задаем высоту окна в тайлах
            self.height = 9
            # Задаем ширину тайлов в пикселях
            self.tile = 24
            # Для того чтобы наш Gui видел настройки, передаем ссылку на контроллер в класс Gui
            self.gui = Gui(self)

Теперь вносим изменения в класс `Gui`

    class Gui:
        def __init__(self, controller):
            pygame.init()
            self.controller = controller
            # Задаем размеры окна, которые берем из объекта класса Controller
            display = (controller.width * controller.tile, controller.height * controller.tile)
            # Создаем переменную screen нашего объекта Gui, чтобы в дальнейшем выводить в нее изображение
            self.screen = pygame.display.set_mode(display)
    
            # Записываем название игры
            pygame.display.set_caption("Last Android")
    
            # Заливаем задний фон белым цветом: Создаем прямоугольную поверхность под размер окна закрашиваем
            self.background = pygame.Surface(display)
            self.background.fill(pygame.Color("#ffffff"))

        def update(self):
            # выводим на экран наш белый прямоугольник
            self.screen.blit(self.background, (0, 0))
    
            ...
    
            pygame.display.update()

Файл `main.py` мы больше исправлять не будем. Запускаем и получаем белое окно.

![Результат](/images/1-1-1.jpg)

---

### Работа над ошибками

В коде приведена ошибка в строке `pygame.display.set_mode(320, 240)`, нужно записать `pygame.display.set_mode((320, 240))`