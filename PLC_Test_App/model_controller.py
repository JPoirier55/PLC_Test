from PLC_Test_App.models import *
import xlrd

input_names = ['Input 0', 'Input 1', 'Input 2', 'Input 3', 'Input 4', 'Input 5', 'Input 6', 'Input 7', 'Input 8',
               'Input 9', 'Input 10', 'Input 11', 'Input 12', 'Input 13', 'Input 14', 'Input 15', 'Input 16',
               'Input 17', 'Input 18', 'Input 19', 'Input 20', 'Input 21', 'Input 22', 'Input 23', 'Input 24',
               'Input 25', 'Input 26', 'Input 27', 'Input 28', 'Input 29', 'Input 30', 'Input 31']
output_names = ['Output 0', 'Output 1', 'Output 2', 'Output 3', 'Output 4', 'Output 5', 'Output 6', 'Output 7',
                'Output 8',
                'Output 9', 'Output 10', 'Output 11', 'Output 12', 'Output 13', 'Output 14', 'Output 15', 'Output 16',
                'Output 17', 'Output 18', 'Output 19', 'Output 20', 'Output 21', 'Output 22', 'Output 23', 'Output 24',
                'Output 25', 'Output 26', 'Output 27', 'Output 28', 'Output 29', 'Output 30', 'Output 31']


def new_test(name, input_names, output_names):
    p = Test.objects.create(name='automate', input_names=input_names, output_names=output_names)
    p.save()
    return Test.objects.values_list('name', flat=True)


def new_test_xlsx(name, file_name):
    book = xlrd.open_workbook('test_1.xlsx')

    header = []

    sheet = book.sheets()[0]
    for row_num, row in enumerate(sheet.get_rows()):
        if row_num <= 0:
            print(row)  # Print out the header

    p = Test.objects.create(name=name, input_names=input_names, output_names=output_names)
    p.save()
    return Test.objects.values_list('name', flat=True)
