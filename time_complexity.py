"""
Testing time complexity of RSA implementations
"""
import time
import rsa
import pandas
import random

REPETITION = 5


# Testing different bit length numbers
def prime_bit_length_complexity(min, max, step):
    """
    Find the time complexity between different bit ranges for prime numbers

    min : The minium bit size.
    max : The maximum bit size.
    rep : Bit size step.

    Return:
    A CSV with the saved bit size and time.
    """
    data = pandas.DataFrame(
        {
            "Prime Number Range": [],
            "Prime number generation": [],
            "Euler Key Generation Time": [],
            "Euler Encryption Time": [],
            "Euler Decryption Time": [],
            "Euler CRT Decryption Time": [],
            "Carmichael Key Generation Time": [],
            "Carmichael Encryption Time": [],
            "Carmichael Decryption Time": [],
            "Carmichael CRT Decryption Time": [],
        }
    )

    min_value = 2**min
    max_value = 2**max

    for size in range(min, max, step):
        # Set up range for prime numbers
        prime_range = f"{size}-{size+step}"
        row = [prime_range]
        min_value = 2**size
        max_value = 2 ** (size + step)
        print(f"Times from prime numbers {size} bits to {size+step} bits\n")
        print("Prime Number generation")
        start_time = time.time()
        p, q = rsa.generate_pq(min_value, max_value)
        end_time = time.time()
        prime_generation_time = end_time - start_time
        print(f"Prime Generation Time: {prime_generation_time}\n")
        row.append(prime_generation_time)
        # EULER
        # Key generation and time
        print("EULER\n")
        print("Key Generation\n")
        avg_time_key = get_average_RSA(p, q, True, REPETITION)
        row.append(avg_time_key)
        print(f"Key Generation Time: {avg_time_key}\n")
        public_key, private_key = rsa.rsa(min_value, max_value)
        # generate a radndom message less than n (in this case less than p)
        message = random.randint(0, min_value)

        # Encryption
        print("Encryption\n")
        avg_time_encryption = get_average_encryption(message, public_key, REPETITION)
        row.append(avg_time_encryption)
        print(f"Encryption Time: {avg_time_key}\n")
        c = rsa.encrypt(message, public_key)

        # Decryption
        print("Decryption\n")
        avg_time_decryption = get_average_decryption(
            c, private_key, REPETITION, message
        )
        row.append(avg_time_decryption)
        avg_time_decryption_crt = get_average_decryption_crt(
            c, private_key, REPETITION, message
        )
        row.append(avg_time_decryption_crt)
        print(f"Decryption Time: {avg_time_decryption}\n")
        print(f"Decryption CRT Time: {avg_time_decryption_crt}\n")

        # CARMICHAELS
        print("CARMICHAELS")
        print("Key Generation\n")
        avg_time_key = get_average_RSA(p, q, False, REPETITION)
        row.append(avg_time_key)
        print(f"Key Generation Time: {avg_time_key}\n")
        public_key, private_key = rsa.rsa(min_value, max_value)
        # generate a radndom message less than n (in this case less than p)
        message = random.randint(0, min_value)

        # Encryption
        print("Encryption\n")
        avg_time_encryption = get_average_encryption(message, public_key, REPETITION)
        row.append(avg_time_encryption)
        print(f"Encryption Time: {avg_time_key}\n")
        c = rsa.encrypt(message, public_key)

        # Decryption
        print("Decryption\n")
        avg_time_decryption = get_average_decryption(
            c, private_key, REPETITION, message
        )
        row.append(avg_time_decryption)
        avg_time_decryption_crt = get_average_decryption_crt(
            c, private_key, REPETITION, message
        )
        row.append(avg_time_decryption_crt)
        print(f"Decryption Time: {avg_time_decryption}\n")
        print(f"Decryption CRT Time: {avg_time_decryption_crt}\n")
        data.loc[len(data)] = row
    # save data to csv
    data.to_csv(f"prime_{min}-{max}_step-{step}.csv")


# Finding average time
def get_average_RSA(p, q, euler, rep):
    """
    Get the average time for RSA given the minium, maximum prime and repetition.

    min : The minium prime number.
    max : The maximum prime number.
    rep : The total amount of repetition.

    Return:
    The average time for RSA key generation to run.
    """
    time_sum = 0
    for _ in range(rep):
        start_time = time.time()
        pub, priv = rsa.rsa_time_complexity(p, q, euler)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / rep
    return average


def get_average_encryption(m, public_key, rep):
    time_sum = 0
    for _ in range(rep):
        start_time = time.time()
        c = rsa.encrypt(m, public_key)
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / rep
    return average


def get_average_decryption(c, private_key, rep, message):
    time_sum = 0
    for _ in range(rep):
        start_time = time.time()
        m = rsa.decrypt(c, private_key)
        if m != message:
            print("BROKEN DECRYPTION\n")
            print(f"Got {m}, expected {message}\n")
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / rep
    return average


def get_average_decryption_crt(c, private_key, rep, message):
    time_sum = 0
    for _ in range(rep):
        start_time = time.time()
        m = rsa.decrypt(c, private_key)
        if m != message:
            print("BROKEN DECRYPTION CRT\n")
            print(f"Got {m}, expected {message}\n")
        end_time = time.time()
        total_time = end_time - start_time
        time_sum = total_time + time_sum
    average = time_sum / rep
    return average


prime_bit_length_complexity(4, 16, 1)
