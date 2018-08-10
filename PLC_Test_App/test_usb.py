import json
import

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

plc_expected_outputs = [{"output_0": 0,
                         "output_1": 0,
                         "output_2": 0,
                         "output_3": 0},
                        {"output_0": 0,
                         "output_1": 0,
                         "output_2": 1,
                         "output_3": 0},
                        {"output_0": 0,
                         "output_1": 0,
                         "output_2": 1,
                         "output_3": 0},
                        {"output_0": 1,
                         "output_1": 0,
                         "output_2": 0,
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
    d = {}
    for i in range(20):
        # if i < 10:
        #     print('\'O'+str(i)+'\',', end="")
        # else:
        #     print('\'O'+str(i) + '\',', end="")
        d['output_'+str(i)] = 0
    print(json.dumps(d))