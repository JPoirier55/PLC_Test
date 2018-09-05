from django.apps import AppConfig
from PLC_Test_App import gpio

I2C_OBJ = gpio.I2CReader()


class PlcTestAppConfig(AppConfig):
    name = 'PLC_Test_App'

    def ready(self):
        print("GPIO setting up...")

