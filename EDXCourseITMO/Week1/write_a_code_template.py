

class ProgramName:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value < other.value

    def __str__(self):
        return f'{self.name}\n{self.value}'


def calculate_value(keyboard, text):
    distance = 0
    for i in range(len(text)-1):
        char1 = text[i]
        char2 = text[i+1]
        xa, ya = keyboard[char1]
        xb, yb = keyboard[char2]
        distance += max(abs(xa - xb), abs(ya - yb))
    return distance


if __name__ == '__main__':
    with open('input.txt', 'r') as inp:
        w, h = list(map(int, inp.readline().split()))
        keyboard = {}
        for i in range(h, 0, -1):
            h = inp.readline()
            for j, a in enumerate(h):
                keyboard[a] = (i, j+1)
        programs = []
        for _ in range(3):
            lang_name = inp.readline().replace(' ', '').strip()
            text = []
            a = inp.readline()
            a = inp.readline().replace(' ', '').strip()
            while(a != '%TEMPLATE-END%'):
                text.append(a)
                a = inp.readline().replace(' ', '').strip()

            value = calculate_value(keyboard, ''.join(text))
            lang_info = ProgramName(lang_name, value)
            programs.append(lang_info)

        with open('output.txt', 'w') as out:
            out.write(str(min(programs)))
            out.write('\n')
