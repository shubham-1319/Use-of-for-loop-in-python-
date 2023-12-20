#by shubh
def print_numbers():
    for i in range(1, 11):
        print(i)

def repeat_sequence(num_times):
    for _ in range(num_times):
        print_numbers()

# Repeat the sequence 3 times (you can change the value as needed)
repeat_sequence(3)
