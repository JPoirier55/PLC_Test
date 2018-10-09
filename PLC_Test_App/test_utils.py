import xlrd
import json


def validate_import(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheets()[0]
    num_test_cases = 0
    end_of_tests = False
    test_dict = {'input_names': [],
                 'output_names': [],
                 'test_cases': []
                 }
    row_num = 0
    try:
        for row_num, row in enumerate(sheet.get_rows()):
            if row_num == 0:
                try:
                    num_test_cases = int(row[0].value)
                except Exception as e:
                    return "Error: number of test cases failure: " + str(e), None
                if num_test_cases <= 0:
                    return "Error: number of test cases <= 0", None
            elif row_num == 1:
                for header_index in range(len(row)):
                    if 1 <= header_index < 33:
                        test_dict['input_names'].append(row[header_index].value)
                    elif 33 <= header_index < 65:
                        test_dict['output_names'].append(row[header_index].value)
            elif row_num >= 2 and not end_of_tests:
                temp_dict = {'inputs': [],
                             'outputs': [],
                             'name': "",
                             'hold_time': 0}
                for input_output_index in range(len(row)):
                    if input_output_index == 0:
                        temp_dict['name'] = str(row[input_output_index].value)
                    elif 1 <= input_output_index < 33:
                        temp_dict['inputs'].append(int(row[input_output_index].value))
                    elif 33 <= input_output_index < 65:
                        temp_dict['outputs'].append(int(row[input_output_index].value))
                    elif input_output_index == 65:
                        temp_dict['hold_time'] = float(row[input_output_index].value)
                test_dict['test_cases'].append(temp_dict)
    except Exception as e:
        return "Validation Error: " + str(e) + " at row number: " + str(row_num), None

    return 'OK', test_dict
