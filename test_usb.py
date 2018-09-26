import json
# import smbus

plc_outputs = [{"output_0": 0,
                "output_1": 0,
                "output_2": 0,
                "output_3": 0},
               {"output_0": 0,
                "output_1": 1,
                "output_2": 1,
                "output_3": 0},
               {"output_0": 0,
                "output_1": 0,
                "output_2": 1,
                "output_3": 1},
               {"output_0": 1,
                "output_1": 0,
                "output_2": 1,
                "output_3": 0},
               {"output_0": 1,
                "output_1": 1,
                "output_2": 1,
                "output_3": 0}]


def run_test():
    with open('testdata_3.json') as f:
        data = json.load(f)
    for test_run in data:
        print(test_run)


if __name__ == "__main__":
    import xlrd
    book = xlrd.open_workbook('PLC_Test_App/test_1.xlsx')

    header = []

    sheet = book.sheets()[0]
    num_test_cases = 0
    hold_times = []
    input_names = []
    output_names = []
    inputs = []
    expected_outputs = []
    for row_num, row in enumerate(sheet.get_rows()):
        if row_num <= 0:
            print(row)  # Print out the header
        elif row_num == 1:
            test_name = row[0].value
            plc_type = row[1].value
            num_test_cases = int(row[2].value)
            for test_case_index in range(num_test_cases):
                hold_times.append(row[test_case_index + 3].value)
            print(test_name)
            print(plc_type)
            print(hold_times)
        elif row_num == 2:
            print(row)
        elif row_num > 2:
            input_names.append(row[0].value)
            output_names.append(row[1].value)
            input_case = []
            output_case = []
            for test_case_index in range(len(hold_times)):
                input_case.append(row[test_case_index + 2].value)
                output_case.append(row[test_case_index + 2].value)
            inputs.append(input_case)
            expected_outputs.append(output_case)
    print(input_names)
    print(output_names)
    print(inputs)
    print(expected_outputs)

    # t = [0, 0, 0, 0, 2, 0, 0, 4,
    #      9, 0, 0, 0, 0, 0, 0, 6,
    #      89, 0, 0, 0, 0, 0, 0, 7,
    #      78, 0, 0, 0, 0, 0, 0, 8]
    #
    # print(t[0:8])
    # print(t[8:16])
    # print(t[16:24])
    # print(t[24:32])
    # import time
    # bus = smbus.SMBus(1)
    # DEVICE = 0x20  # Device address (A0-A2)
    # IODIRA = 0x00  # Pin direction register
    # OLATA = 0x14  # Register for outputs
    # GPIOA = 0x12  # Register for inputs
    #
    # # Set all GPA pins as outputs by setting
    # # all bits of IODIRA register to 0
    # bus.write_byte_data(DEVICE, IODIRA, 0x80)
    #
    # # Set output all 7 output bits to 0
    # # bus.write_byte_data(DEVICE, OLATA, 0)
    #
    # # time.sleep(1)
    # # bus.write_byte_data(DEVICE, OLATA, 1)
    # while True:
    #
    #     # Read state of GPIOA register
    #     MySwitch = bus.read_byte_data(DEVICE, GPIOA)
    #     print(MySwitch)
    #     if MySwitch & 0b10000000 == 0b10000000:
    #         print("Switch was pressed!")
    #     time.sleep(1)


    # d = {}
    # for i in range(35):
    #     if i < 10:
    #         print('\'Output '+str(i)+'\',', end="")
    #     else:
    #         print('\'Output '+str(i) + '\',', end="")
        # d['output_'+str(i)] = 0
    # print(json.dumps(d))