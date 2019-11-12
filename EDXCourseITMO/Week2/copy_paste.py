from edx_io import edx_io

with edx_io() as io:
    n = io.next_int()
    f_vals = []
    s_mins = []
    very_bad = 2000000000
    f_min = very_bad
    
    for _ in range(n):
        cmd = io.next_token()
        if cmd == b"+":
            last = io.next_int()
            f_min = min(f_min, last)
            f_vals.append(last)
        elif cmd == b"-":
            if len(s_mins) == 0:
                s_mins.append(f_vals.pop())
                while len(f_vals) > 0:
                    s_mins.append(min(s_mins[-1], f_vals.pop()))
                f_min = very_bad
            s_mins.pop()
        else:
            res = f_min
            if len(s_mins) > 0:
                res = min(res, s_mins[-1])
            io.writeln(res)

