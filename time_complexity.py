'''
Testing time complexity of RSA implementations
'''
import csv
import time 
import rsa

REPETITION = 5

# Testing different bit length numbers 
def bit_length_complexity(min, max, step): 
    """
    Find the time complexity between different bit ranges
    """
    min_value = 2**min 
    max_value = 2**max 
    data = dict()
    for size in range (min, max, step):
        min_value = 2**size 
        max_value = 2**(size+step)
        avg_time = get_average_RSA(min_value, max_value, REPETITION)
        data[f"{size}-{size+step}"] = avg_time
        print(f"Time from {size} bits to {size+step} bits: {avg_time}")

    with open(f"{min}-{max}-step{step}.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
        
# Finding average time
def get_average_RSA(min, max, rep):
    """
    Get the average time for RSA given the minium, maxium prime and repetation

    min : the minium prime number 
    max : the maximum prime number 
    rep : the total amount of repetition

    Return: the average time
    """
    time_sum = 0
    for _ in range(rep):
        start_time = time.time()
        pub, priv = rsa.rsa(min, max)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / rep
    return average


bit_length_complexity(3, 8, 1)
