
def get_number():
    numbers = []
    for i in range(5):
        number = int(input(f"Write your {i+1} number down"))
        numbers.append(number)
    return numbers

def the_lowest_number(q):
    return min(q)

q = get_number()

print(the_lowest_number(q))