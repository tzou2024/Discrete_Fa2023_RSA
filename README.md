# RSA Encryption

#### An Grocki, Trinity Lee, Trevor Zou


## RSA

#####As part of this project we have written a report on the proof of correctness of our RSA enryption viewable [here](Proof_of_RSA.pdf), as well as a slideshow with a high level overview of RSA encryption [here](https://docs.google.com/presentation/d/1KGHfXNhAheroX9nkbQGTQ6GJr7s40qyXcX0OL20XZtc/edit?usp=sharing).

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

To generate the public key and private key update values for the minium and maximum prime number for prime number generation `rsa.py`. The `euler` argument in the `rsa` function can ether be `True` for using the Euler's totient function or `False` to use Carmichael's totient function.

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
"prime*[min_size]-[max_size]\_[step]-[step_size].csv"


## Attacks

There are two attacks implemented as part of the project: The Hastad Broadcast Attack and the Wiener's Attack. These two are one of the most well-known RSA attacks that have been proven to work due to specific conditions usually reliant on poorly chosen values for the algorithm. For implementation, we created a file called `attacks.py` which stores functions that implement and solve these attacks, dependent on functions created in `rsa.py`.

### Hastad BroadCast Attack

The Hastad Broadcast Attack is an attack which allows us to bypass the need for a private key and unencrypt ciphertext given these specific conditions:

1. We need to have multiple different ciphertexts (C) generated from the same plaintext (M). Specifically, because Hastad's Broadcast works, once the number of ciphertexts > public key, this attack will work work. 

2. These different ciphertexts used multiple different p & q (to generate n1, n2, n3, etc), but the public key (e) is the same.
3. The public key is a small value (small public exponent). 

This allows us to use the Chinese Remainder Theorem and decipher what the plaintext is given multiple encryptions of it. The function `hastad_ciphertexts`automatically generates multiple different ciphertexts for the inputted message given a set public key and then proceeds to crack the encryption. 

To run this, just input the message (which is an integer) which you'd like to encrypt and the public key of your choice for to run the function. For example, if we want to encrypt `1234` with a public encryption key of `3`, it will look like this:

```
hastad_ciphertexts(1234, 3)
```

The function outputs:

```

Actual Plaintext: 1234
CipherText 0 : 10783  | Calculating Modular Inverse of N:  6432
CipherText 1 : 819  | Calculating Modular Inverse of N:  562
CipherText 2 : 30735  | Calculating Modular Inverse of N:  14422
Plaintext Approximated from ciphertexts via CRT:  1233.9999999999995

```

### Wiener's Attack

This attack utilizes Weiner's Theorem (in the context of RSA) where given the public key (e, n), if  q < p < 2q and d < 1/3(n)^1/4 then k/d is amongst the convergences of e/n. 

Wiener's Attack finds `d` from the list of potential `d`'s calculated by convergence. 
    
1. Use the d value to calculate a phi(n) via 
        phi(n) = ed -1/k
2. Use phi(n) to calculate a the roots for the solution for  
        x^2 - (n - phi(n)+1)x + n = 0
3. The roots are p & q, and if they match the chosen n, then we have found the correct private key d
    
There are multiple functions that make up Wiener's attack, with the function `wiener()` tying all of the functions together. 


wiener_n()` is a function that brute force calculates a public and private key that is useable for Wiener's attack. However, due to the nature of finding a public and private key that meet these conditions, it takes an extremely long time to calculate with these values

`continued_frac()` is a function that calculates a list of continued fractions for e/N and calculates all possible convergents for k/d

`solve_d`is a function that calculates the correct private key from the list of all possible private keys generated from the convergents for k/d. 

Below is a proof of concept that these functions work as intended given a public key that is known to be vulnerable to this attack. 

```
    #Proof of concept that functions work
     n = 90581
     e = 17993
     k, d = continued_frac(e, n)
     print(k)
     #[0, 1, 29, 117, 146, 555, 1256, 5579, 17993]
     print(d)
    #[1, 5, 146, 589, 735, 2794, 6323, 28086, 90581]

     x = solve_d(e,n, k, d)
     print (x)
     #(239, 379, 5)
```


## Time Complexity

We compared multiple variations of RSA with a timing analysis. We ran each function 5 times and averaged the time together to gain an accurate understanding of the difference.

There was a significant difference between Euler's totient and Carmichael's totient especially as the bit size increased.

![Euler vs. Carmichael's](images/Prime%20Number%20Bit%20Size%20Range%20vs%20Key%20Generation%20Time.png)

There was not as significant difference between Chinese Reminder Theorem and the using the inverse modulo of e. We suspected that due to the small message and key sizes, the time decreases between CRT and the original decrypting method is not as noticeable. Due to the difficulty creating key's larger than 18 bits, we were not able to test our hypothesis, but average prime number sizes is from 1024 bits to 2024 bits.

![Euler vs. Carmichael's](images/Prime%20Number%20Bit%20Size%20Range%20vs%20Decryption%20Time.png)

Based on our time analysis, we learned that they are multiple ways to decrease the run time. With algorithms and math, we can use Carmichael's totient function and Chinese Reminder Theorem. With code we can use specific libraries to find prime numbers and greatest common divisor. Moreover, choices on caching prime numbers and using optimized code or different coding languages like C can help decrease the run time, and allow larger and more secure keys to be generated.

# Citations

[Annotated Bibliography](https://docs.google.com/document/d/1IC5fMH0H-vLdntmfxGZIAFUJ5LVe8GBnTvu4SENAZ6E/edit?usp=sharing)