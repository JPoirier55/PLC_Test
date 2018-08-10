import RPi.GPIO as GPIO
import time
import json

gpio_input_pinlist = [22, 24, 25]
gpio_output_pinlist = [23, 18, 17, 27]


def setup():
    """
    Sets up gpios, only happens at start up
    of django app once, or if called manually
    :return: None
    """
    GPIO.setmode(GPIO.BCM)

    for pin in gpio_input_pinlist:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    for pin in gpio_output_pinlist:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)


def read_input(pin_num):
    return GPIO.input(pin_num)


def send_output(pin_num, value):
    GPIO.output(pin_num, value)


def cleanup():
    GPIO.cleanup()


def fetch_test_file(test_number):
    with open('testdata_'+str(test_number)+'.json') as f:
        file_data = json.load(f)
    return file_data


def run_outputs(file_data):
    for test, input_arr in file_data.items():
        for i in range(len(input_arr)):
            input_value = input_arr[i]
            input_num = gpio_output_pinlist[i]
            send_output(input_num, input_value)
            time.sleep(.2)
        for i in range(len(input_arr)):
            input_num = gpio_output_pinlist[i]
            send_output(input_num, 1)


def read_inputs():
    input_status_arr = []
    for input_num in gpio_input_pinlist:
        input_status_arr.append(read_input(input_num))
        time.sleep(.1)
    print(input_status_arr)


if __name__ == '__main__':
    setup()
    filedata = fetch_test_file(3)
    run_outputs(filedata)
    # try:
    #     while True:
    #         read_inputs()
    # except KeyboardInterrupt:
    #     print('interrupted!')
    cleanup()



