from helpers import read_file

# data = read_file("inputs/day2_test.txt")
data = read_file("inputs/day2_a.txt")

def formatter(line):
    gameinfo, data = line.split(":")
    game_id = int(gameinfo.split(" ")[1])
    
    rounds = data.split(";")
    data = []
    for round in rounds:
        values = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for cubes in round.strip().split(","):
            digit, color = cubes.strip().split(" ")
            values[color] = int(digit)

        data.append(values)
    return game_id, data


def A():
    total = 0
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in data:
        game_id, round_data = formatter(line)
        add = True
        for round in round_data:
            if round["red"] > limits["red"] or round["green"] > limits["green"] or round["blue"] > limits["blue"]:
                add = False

        total += game_id if add else 0

    print(total)
    
    
def B():
    total = 0
    for line in data:
        game_id, round_data = formatter(line)
        add = True
        min_values = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in round_data:
            min_values = {
                "red": max(min_values["red"], round["red"]),
                "green": max(min_values["green"], round["green"]),
                "blue": max(min_values["blue"], round["blue"])
            }
        
        value = 1
        for color in min_values:
            value *= min_values[color] if min_values[color] > 0 else 1
            
        total += value
        
    print(total)


if __name__ == "__main__":
    # A()
    B()    
    
        
    
