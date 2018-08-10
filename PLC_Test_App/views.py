from django.shortcuts import render
from django.shortcuts import HttpResponse
import json, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    plc_type = request.GET.get('plc_type', None)
    input_list = []
    input_name_list = []
    output_list = []
    output_name_list = []
    if plc_type == 'siem':
        input_list = [0, 1, 2, 3, 4, 5, 6, 7]
        input_name_list = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9']
        output_list = [0, 1, 2, 3]
        output_name_list = ['Q1', 'Q2', 'Q3', 'Q4']
    if plc_type == 'ab':
        input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        input_name_list = ['I:100', 'I:101', 'I:102', 'I:103', 'I:104', 'I:105', 'I:106',
                           'I:107', 'I:108', 'I:109', 'I:110', 'I:111', 'I:112', 'I:113',
                           'I:114', 'I:115']
        output_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        output_name_list = ['O:100', 'O:101', 'O:102', 'O:103', 'O:104', 'O:105', 'O:106',
                            'O:107', 'O:108', 'O:109', 'O:110', 'O:111', 'O:112', 'O:113',
                            'O:114', 'O:115']
    if plc_type == 'unitr':
        input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        input_name_list = ['I0', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
                           'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19']
        output_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        output_name_list = ['O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9',
                            'O10', 'O11', 'O12', 'O13', 'O14', 'O15', 'O16']
    return render(request, 'main.html', {'input_list': input_list,
                                         'input_name_list': input_name_list,
                                         'output_list': output_list,
                                         'output_name_list': output_name_list,
                                         'plc_type': plc_type})


def get_data(request):
    plc_type = request.GET.get('plc_type', '')
    print(BASE_DIR + '/' + plc_type + '_outputs.json')
    with open(BASE_DIR + '/' + plc_type + '_outputs.json', 'r') as f:
        data = json.load(f)
    return HttpResponse(json.dumps(data), content_type="application/json")


def set_data(request):
    switch_num = request.POST.get('switch', '')
    switch_state = request.POST.get('state', '')
    plc_type = request.POST.get('plc_type', '')
    if int(switch_num) >= 0:
        print('Sw: ' + switch_num + "  State: " + switch_state)
        print(BASE_DIR + '/' + plc_type + '_testdata.json')
        with open(BASE_DIR + '/' + plc_type + '_testdata.json', 'r') as f:
            data = json.load(f)
            f.close()
        with open(BASE_DIR + '/' + plc_type + '_testdata.json', 'w') as f:
            data['input_' + str(switch_num)] = int(switch_state)
            f.write(json.dumps(data))
            f.close()
    return HttpResponse()


def run_test(request):
    return render(request, 'index.html')
