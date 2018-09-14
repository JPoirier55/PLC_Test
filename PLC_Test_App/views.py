from django.shortcuts import render
from django.shortcuts import HttpResponse
from PLC_Test_App.models import *

import json, os
from PLC_Test_App import apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    plc_type = request.GET.get('plc_type', None)
    input_name_list = ['I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14',
                       'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I26', 'I27', 'I28',
                       'I29', 'I30', 'I31']
    output_name_list = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'O10', 'O11', 'O12', 'O13', 'O14',
                        'O15', 'O16', 'O17', 'O18', 'O19', 'O20', 'O21', 'O22', 'O23', 'O24', 'O25', 'O26', 'O27',
                        'O28', 'O29', 'O30', 'O31']
    return render(request, 'main.html', {'input_name_list': input_name_list,
                                         'output_name_list': output_name_list,
                                         'plc_type': plc_type})


def testing(request):
    test_name = request.GET.get('test_name', '')
    test_case_objs = TestCase.objects.filter(test__name=test_name)
    test_obj = Test.objects.filter(name=test_name)
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


def test_results(request):
    test_name = request.GET.get('test_name', '')
    test_cases = TestCase.objects.filter(test__name=test_name)
    test_obj = Test.objects.get(name=test_name)
    input_names = eval(test_obj.input_names)
    output_names = eval(test_obj.output_names)
    overall_results = []
    i2c = apps.I2C_OBJ
    fail_count = 0
    for test_case in test_cases:
        real = i2c.run_outputs(eval(test_case.input), test_case.hold_time)
        expected = eval(test_case.result)
        compare = []
        result_arr = []
        for result_index in range(len(real)):
            if real[result_index] == expected[result_index]:
                compare.append(1)
                match = 1
            else:
                compare.append(0)
                match = 0
                fail_count += 1
            result_arr.append({'output_num': result_index,
                               'input': eval(test_case.input)[result_index],
                               'expected': expected[result_index],
                               'real': real[result_index],
                               'compare': match,
                               'test_case_name': test_case.name,
                               'input_name': input_names[result_index],
                               'output_name': output_names[result_index]})
        if fail_count > 0:
            failed = True
        else:
            failed = False
        overall_results.append({'failed': failed, 'result_dicts': result_arr, 'failed_num': fail_count})
        fail_count = 0

    return render(request, 'test_results.html', {'result': overall_results,
                                                 'test_cases': test_cases,
                                                 'test_name': test_name})


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
