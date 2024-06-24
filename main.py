import os
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.camera import Camera

class CameraScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Инициализация камеры
        self.camera = Camera(resolution=(640, 480), play=True)
        self.add_widget(self.camera)

        # Добавляем кнопки
        button_layout = BoxLayout(size_hint_y=None, height='48dp')

        self.capture_button = Button(text="Сделать фото")
        self.capture_button.bind(on_press=self.capture_photo)
        button_layout.add_widget(self.capture_button)

        self.switch_button = Button(text="Перейти на основной экран")
        self.switch_button.bind(on_press=self.switch_screen)
        button_layout.add_widget(self.switch_button)

        self.add_widget(button_layout)

        # Для отображения последнего фото
        self.img = Image()
        self.add_widget(self.img)

    def capture_photo(self, instance):
        date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"photo_{date_time}.png"
        self.camera.export_to_png(file_name)
        self.img.source = file_name
        print(f"Фото сохранено: {file_name}")

    def switch_screen(self, instance):
        # Здесь можно реализовать переход на основной экран
        print("Переход на основной экран")


class CameraApp(App):
    def build(self):
        return CameraScreen()

if __name__ == '__main__':
    CameraApp().run()