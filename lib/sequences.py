#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    # if length > 0:
    #     fibonacci_sequence.append(0)
    #     if length > 1:
    #         fibonacci_sequence.append(1)
    #         if length > 2:
    #             for i in range(2, length):
    #                 fibonacci_sequence.append(
    #                     fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    if length == 0:
        fibonacci_sequence = []
    elif length == 1:
        fibonacci_sequence = [0]
    elif length == 2:
        fibonacci_sequence = [0,1]
    elif length > 2:
        fibonacci_sequence = [0,1]
        for i in range(2, length):
            fibonacci_sequence.append(
            fibonacci_sequence[i -1] + fibonacci_sequence[i - 2])
    

    print(fibonacci_sequence)
