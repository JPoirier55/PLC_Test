import time
import json
import smbus


class I2CReader:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.DEVICES = [0x20, 0x21, 0x22, 0x23]  # Device address (A0-A2)
        self.IODIRA = 0x00  # Pin direction register
        self.IODIRB = 0x01  # Pin direction register
        self.OLATA = 0x14
        self.OLATB = 0x15
        self.GPIOA = 0x12
        self.GPIOB = 0x13
        self.setup()

    def setup(self):
        for device in self.DEVICES:
            self.bus.write_byte_data(device, self.IODIRA, 0x01)
            self.bus.write_byte_data(device, self.IODIRB, 0x00)
            self.bus.write_byte_data(device, self.OLATB, 1)

    def read_inputs(self):
        final_arr = []
        for device in self.DEVICES:
            input_dec = self.bus.read_byte_data(device, self.GPIOA)
            binarr = [int(d) for d in str(bin(input_dec))[2:].zfill(8)]
            final_arr += binarr
        print(final_arr)
        return final_arr

    def write_outputs(self, input_array):
        bin_string = ''
        for bn in input_array:
            bin_string += str(bn)
        outputs = [int(bin_string[0:8], 2),
                   int(bin_string[8:16], 2),
                   int(bin_string[16:24], 2),
                   int(bin_string[24:32], 2)]
        for device_index in range(len(self.DEVICES)):
            self.bus.write_byte_data(self.DEVICES[device_index], self.OLATB, outputs[device_index])

    def clear_outputs(self):
        for device_index in range(len(self.DEVICES)):
            self.bus.write_byte_data(self.DEVICES[device_index], self.OLATB, 0xFF)

    def fetch_test_file(self, test_number):
        with open('testdata_' + str(test_number) + '.json') as f:
            file_data = json.load(f)
        return file_data

    def run_outputs(self, file_data):
        for test, input_arr in file_data.items():
            print('Running Test ' + str(test))
            print(input_arr)
            self.write_outputs(input_arr)
            time.sleep(.2)
            self.clear_outputs()
            time.sleep(.2)


if __name__ == '__main__':
    i2c = I2CReader()
    file = i2c.fetch_test_file('3')
    i2c.run_outputs(file)
