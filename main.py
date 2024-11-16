from kivy.app import App
import sys
import os
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Mengatur ukuran jendela aplikasi
Window.size = (360, 640)

# Menambahkan path ke folder 'screens' agar bisa mengimpor modul-modul screen
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Screens'))

# Import file-file screen
from Screens.home_screen import HomeScreen
from Screens.login_screen import LoginScreen
from Screens.register_screen import RegistrasiScreen
from Screens.profile_screen import ProfileScreen
from Screens.edit_profile_screen import EditProfileScreen
from Screens.product_screen import ProductScreen

# Memuat file .kv untuk setiap layar
Builder.load_file('kv/home.kv')
Builder.load_file('kv/login.kv')
Builder.load_file('kv/register.kv')
Builder.load_file('kv/profile.kv')
Builder.load_file('kv/edit_profile.kv')
Builder.load_file('kv/product.kv')

class ApotekKasihApp(App):
    def build(self):
        sm = ScreenManager()

        # Menambahkan setiap layar ke ScreenManager
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegistrasiScreen(name='register'))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(EditProfileScreen(name='edit_profile'))
        sm.add_widget(ProductScreen(name='product'))

        return sm

if __name__ == '__main__':
    ApotekKasihApp().run()
