# RSA Encryption
#### An Grocki, Trinity Lee, Trevor Zou
## Introduction
Rivest Shamir Adleman (RSA) is a popular cryptographic encryption algorithm. It is asymmetric, which means that each user is assigned a public and private key. Anyone can access and use another person’s public key to encode a message to them. Only the recipient can decrypt the message easily using their private key. RSA is based around the product of two large prime numbers. While the product is public, it is extremely hard to figure out what its factors are. These factors are used to encrypt and decrypt such that it is each computed on every input, but hard to invert given just an output.
## Project Description: 
Our project implements an RSA cryptosystem designed for encoding integer-based messages. After researching various adaptations of the RSA algorithm, our objective was to assess and compare the differences in coding methodologies and computational timings.
Within the key generation phase, we have incorporated two distinct methods for generating keys: employing Euler’s totient function and Carmichael's Totient function. Moreover, in the decryption process, we have integrated two different approaches—utilizing the Chinese remainder theorem and an inverse module function.
To explore the differences between RSA adaptations, we have developed a timing analysis function that calculates the average duration of each computational step.
Furthermore, we explored potential vulnerabilities and implemented known RSA attacks including Weiner’s attack and the Hastad Broadcast attacks.
## Dependencies 
In order to run the algorithm and timing analysis, you need to install the following libraries and a python environment:
- primePy 
- random
- math
- functools
- gmpy
= time
- pandas
## How to Run: 
#### Generating a Public and Private Key: 

#### Encrypting a Message:

#### Decrypting a message:

#### Running a Timing Analysis:

#### Running Attacks:

## RSA

## Attacks

## Time Complexity 
We compared multiple variations of RSA with a timing analysis. We ran each function 5 times and averaged the time together to gain an accurate understanding of the difference.


## Results 

# Citations 
[Annotated Bibliography](https://docs.google.com/document/d/1IC5fMH0H-vLdntmfxGZIAFUJ5LVe8GBnTvu4SENAZ6E/edit?usp=sharing)

