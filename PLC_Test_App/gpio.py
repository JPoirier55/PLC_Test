import time
import json
import smbus


class I2CReader:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.DEVICES = [0x20, 0x21]  # Device address (A0-A2)
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
        output1 = int(bin_string[:7], 2)
        output2 = int(bin_string[7:], 2)
        self.bus.write_byte_data(self.DEVICES[0], self.OLATB, output1)
        self.bus.write_byte_data(self.DEVICES[1], self.OLATB, output2)

    def clear_outputs(self):
        self.bus.write_byte_data(self.DEVICE, self.OLATB, 0xFF)

    def fetch_test_file(self, test_number):
        with open('testdata_'+str(test_number)+'.json') as f:
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

    # in_arr = ['0', '1', '0', '1', '0', '1', '1', '1']
    # bin_string = ''
    # for bn in in_arr:
    #     bin_string += bn
    # print(bin_string)
    # output = bin(int(bin_string, 2))
    # print(output)
    # setup()
    # filedata = fetch_test_file(3)
    # run_outputs(filedata)
    # # try:
    # #     while True:
    # #         read_inputs()
    # # except KeyboardInterrupt:
    # #     print('interrupted!')
    # cleanup()
    # Set output all 7 output bits to 0
    # bus.write_byte_data(DEVICE, OLATA, 0)

    # time.sleep(1)
    # bus.write_byte_data(DEVICE, OLATA, 1)
    # bus = smbus.SMBus(1)
    # bus.write_byte_data(0x20, 0x00, 0xF0)
    # while True:
    #
    #     # Read state of GPIOA register
    #     MySwitch = bus.read_byte_data(0x20, 0x12)
    #     t = bin(MySwitch)
    #     for b in t:
    #         print(b)
    #     print(MySwitch)
    #     time.sleep(1)
