import sys
import subprocess
i = 0


filenames = {
    'generator': 'test_generator.py',
    'brute_force': 'first_missing_positive_bf.py',
    'solution' : 'first_missing_positive.py'
    }


while True:
    print('Test Case: {}'.format(i))
    test_case = subprocess.check_output("python {} {} > inp".format(filenames['generator'], i), shell=True).decode('ascii').strip()
    out1 = subprocess.check_output("python {} < inp".format(filenames['brute_force']), shell=True).decode('ascii').strip()
    out2 = subprocess.check_output("python {} < inp".format(filenames['solution']), shell=True).decode('ascii').strip()
    if out1 != out2:
        print('Output1: {}\nOutput2: {}'.format(out1, out2))
        print('Test Case: {}'.format(test_case))
        print('check file named inp')
        print(subprocess.check_output("cat inp", shell=True).decode('ascii').strip())
        break
    i += 1

