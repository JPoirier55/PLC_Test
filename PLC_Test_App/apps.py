from django.apps import AppConfig
from PLC_Test_App import gpio


class PlcTestAppConfig(AppConfig):
    name = 'PLC_Test_App'

    def ready(self):
        # gpio.setup()
        print("GPIO setting up...")
