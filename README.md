# RSA Encryption

#### An Grocki, Trinity Lee, Trevor Zou

## Introduction

Rivest Shamir Adleman (RSA) is a popular cryptographic encryption algorithm. It is asymmetric, which means that each user is assigned a public and private key. Anyone can access and use another person’s public key to encode a message to them. Only the recipient can decrypt the message easily using their private key. RSA is based around the product of two large prime numbers. While the product is public, it is extremely hard to figure out what its factors are. These factors are used to encrypt and decrypt such that it is each computed on every input, but hard to invert given just an output.

## Project Description:

Our project implements an RSA cryptosystem designed for encoding integer-based messages. After researching various adaptations of the RSA algorithm, our objective was to assess and compare the differences in coding methodologies and computational timings.
Within the key generation phase, we have incorporated two distinct methods for generating keys: employing Euler’s totient function and Carmichael's Totient function. Moreover, in the decryption process, we have integrated two different approaches—utilizing the Chinese remainder theorem and an inverse of e modulo function.
To explore the differences between RSA adaptations, we have developed a timing analysis function that calculates the average duration of each computational step.
Furthermore, we explored potential vulnerabilities and implemented known RSA attacks including Weiner’s attack and the Hastad Broadcast attacks.

## Dependencies

In order to run the algorithm and timing analysis, you need to install the following libraries and a python environment:

- primePy
- random
- math
- functools
- gmpy
- time
- pandas

## How to Run:

#### Running RSA Encryption

To generate the public key and private key update values for the minium and maximum prime number for prime number generation `rsa.py`. You can also switch `euler` to `True` for using the Euler's totient function or `False` to use Carmichael's totient function.

```
# Range of prime numbers for p and q
min_prime_value = 2**8
max_prime_value = 3**8
# Set the RSA to use Euler(True) or Carmichael's (False)
euler = False
# Generate public and private keys
```

To encrypt and decrypt a message, update the value for message with a different integer that is less than the minium prime number. The message encrypted, then decrypted with private key `d` as well as the Chinese Remainder Theorem(CRT).

```
# int message
message = 12
# Encrypt message
encrypted_message = encrypt(message, public_key)
print(f"Encrypted message: {encrypted_message}")
# Decrypt message
decrypted_message = decrypt(encrypted_message, private_key)
# Decrypt message with Chinese remainder theorem
decrypted_message_CRT = decrypt_CRT(encrypted_message, private_key)
```

Then run the following command in the terminal within the repository directory.

```
$ python3 rsa.py
```

#### Running a Timing Analysis:

Update values for the minium and maximum bit size for the prime number generation, and the value for the step size in `time_analysis.py`

```
min_size_prime = 4
max_size_prime = 17
step_size = 1
prime_bit_length_complexity(min_size_prime, max_size_prime, step_size)
```

Then run the following command in the terminal within the repository directory.

```
$ python3 time_complexity.py
```

The result of the time analysis should be printed in the terminal as well as saved to a csv in time*data folder with the name
"prime*`min_size`-`max_size`\_step-`step_size`.csv"

#### Running Attacks:

## RSA

As part of this project we have written a report on the proof of correctness of our RSA enryption viewable here[INSERT LINK HERE](), as well as a slideshow with a high level overview of RSA encryption [here](https://docs.google.com/presentation/d/1KGHfXNhAheroX9nkbQGTQ6GJr7s40qyXcX0OL20XZtc/edit?usp=sharing).

## Attacks

## Time Complexity

We compared multiple variations of RSA with a timing analysis. We ran each function 5 times and averaged the time together to gain an accurate understanding of the difference.

## Results

# Citations

[Annotated Bibliography](https://docs.google.com/document/d/1IC5fMH0H-vLdntmfxGZIAFUJ5LVe8GBnTvu4SENAZ6E/edit?usp=sharing)
