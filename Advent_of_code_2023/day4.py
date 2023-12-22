from helpers import read_file

# data = read_file("inputs/day4_test.txt")
data = read_file("inputs/day4.txt")

def formatter(line):
    cardinfo, data = line.split(":")
    
    winning_no, ticket_no = data.split("|")
    return set(map(lambda x: int(x), winning_no.strip().split())), list(map(lambda x: int(x), ticket_no.strip().split()))


def A():
    total = 0
    for line in data:
        winning_no, ticket_no = formatter(line)

        wins = 0
        for number in ticket_no:
            if number in winning_no:
                wins += 1
        total += 2**(wins - 1) if wins > 0 else 0
                

    print(total)
    
def B():
    total = 0
    final_value = [1 for _ in range(len(data))]
    for i, line in enumerate(data):
        winning_no, ticket_no = formatter(line)

        wins = 0
        for number in ticket_no:
            if number in winning_no:
                wins += 1
        for _ in range(final_value[i]):
            for j in range(1, wins+1):
                final_value[i + j] += 1
    
    print(final_value)
    
    print(sum(final_value)) 

if __name__ == "__main__":
    # A()
    B()




