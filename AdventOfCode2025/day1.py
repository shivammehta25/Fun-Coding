from audioop import cross
from turtle import update
from utils import Input

def A():
    input = Input(1, 'a')
    # print(input.sample)
    # print(input.data)
    
    INPUT = input.data
    MAX_VAL = 99 + 1

    dial_val = 50
    zero_count = 0

    for line in INPUT:
        side, val = line[0], int(line[1:])
        if side == 'L':
            val *= -1

        dial_val = (dial_val + val) % MAX_VAL
 
        if dial_val == 0:
            zero_count += 1
        
    
    print(zero_count)
            


def B():

    input = Input(1, 'a')
    
    INPUT = input.data
    MAX_VAL = 99 + 1

    dial_val = 50
    crossed_zero = 0
    prev_val = dial_val

    for line in INPUT:
        side, val = line[0], int(line[1:])
        if side == 'L':
            val *= -1
        
        updated_val = prev_val + val
        
        if ((updated_val >= 100) or (updated_val <=0)):
            if updated_val >= 100:
                crossed_zero += updated_val // MAX_VAL
            else:
                crossed_zero += abs(updated_val) // MAX_VAL + (prev_val != 0)

        # print("--------")


        dial_val = (updated_val) % MAX_VAL

        # print(prev_val, val, updated_val, dial_val)
        # print(crossed_zero)
        prev_val = dial_val

    print(crossed_zero)

if __name__ == '__main__':
    A()
    print("-" * 50)
    B()
