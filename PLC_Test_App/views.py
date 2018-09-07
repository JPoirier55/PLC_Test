from django.shortcuts import render
from django.shortcuts import HttpResponse
from PLC_Test_App.models import *

import json, os
from PLC_Test_App import apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    plc_type = request.GET.get('plc_type', None)
    input_list = []
    input_name_list = []
    output_list = []
    output_name_list = []
    # if plc_type == 'siem':
    #     input_list = [0, 1, 2, 3, 4, 5, 6, 7]
    #     input_name_list = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8']
    #     output_list = [0, 1, 2, 3]
    #     output_name_list = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']
    # if plc_type == 'ab':
    #     input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #     input_name_list = ['I:100', 'I:101', 'I:102', 'I:103', 'I:104', 'I:105', 'I:106',
    #                        'I:107', 'I:108', 'I:109', 'I:110', 'I:111', 'I:112', 'I:113',
    #                        'I:114', 'I:115']
    #     output_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #     output_name_list = ['O:100', 'O:101', 'O:102', 'O:103', 'O:104', 'O:105', 'O:106',
    #                         'O:107', 'O:108', 'O:109', 'O:110', 'O:111', 'O:112', 'O:113',
    #                         'O:114', 'O:115']
    # if plc_type == 'unitr':
    input_name_list = ['I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14',
                       'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I26', 'I27', 'I28',
                       'I29', 'I30', 'I31']
    # io_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
    #            18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    output_name_list = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14',
                        'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27',
                        'O28', 'O29', 'O30', 'O31']
    return render(request, 'main.html', {'input_name_list': input_name_list,
                                         'output_name_list': output_name_list,
                                         'plc_type': plc_type})


def testing(request):
    test_name = request.GET.get('test_name', '')
    print(test_name)
    test_case_objs = TestCase.objects.filter(test__name=test_name)
    test_obj = Test.objects.filter(name=test_name)
    print(test_obj[0].input_names)
    test_names = Test.objects.all()
    test_cases = []
    for test_case in test_case_objs:
        input_result = []
        test_case_input = eval(test_case.input)
        test_case_result = eval(test_case.result)
        for input_index in range(len(test_case_input)):
            input_result.append((eval(test_obj[0].input_names)[input_index], test_case_input[input_index],
                                 eval(test_obj[0].output_names)[input_index], test_case_result[input_index]))
        temp_dict = {'test_case_name': test_case.name,
                     'test': test_name,
                     'input_result': input_result,
                     'input_names': test_obj[0].input_names,
                     'output_names': test_obj[0].output_names}
        test_cases.append(temp_dict)

    return render(request, 'testing.html', {'test_cases': test_cases,
                                            'test_names': test_names,
                                            'chosen': test_name
                                            })


# ------------- API Methods ---------------- #


def get_data(request):
    i2c = apps.I2C_OBJ
    arr = i2c.read_inputs()
    return HttpResponse(arr)


def set_data(request):
    data = json.loads(request.POST.get('data_out', ''))
    set_arr = []
    for i in range(len(data)):
        if data[str(i)]:
            set_arr.append(0)
        else:
            set_arr.append(1)
    i2c = apps.I2C_OBJ
    i2c.write_outputs(set_arr)
    return HttpResponse(set_arr)


def run_test(request):
    i2c = apps.I2C_OBJ
    test_file = i2c.fetch_test_file('3')
    i2c.run_outputs(test_file)
    arr = i2c.read_inputs()
    return HttpResponse("complete")
