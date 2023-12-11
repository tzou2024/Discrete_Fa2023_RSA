"""
Implementation of RSA attacks (Coppersmith & Weiner)
"""
from rsa import rsa, encrypt, mod_inverse

# Hastad's BroadCast Attack
"""
How Hastad's Attack Works
Basically, we can decipher what M is without needing to know what d is if the following conditions are true

Conditions: 

1. We need to have multiple different ciphertexts (C) generated from the same plaintext (M). Specifically, 
because Hastad's Broadcast works,once the number of ciphertexts > public key, this attack will work work. 

C1 = M^e mod n1
C2 = M^e mod n2
C3 = M^e mod n3


2. These different ciphertexts used multiple different p & q (to generate n1, n2, n3, etc), but the public key (e) is the same
3. The public key is a small value (small public exponent). 


According to CRT, if we calculate n1 * n2 * n3 and divide all of n1, n2, and n3, but this value and subistitute 
"""


def hastad_ciphertexts(message, e):
    """
    Hastad BroadCast Attack ciphertext generators. Will try to implement the Hastad Broadcast 
    Attack given the plaintext & the public key

    message: our plaintext message
    e: our public key

    """

    # generate our public & privates keys, given that public will stay the same for all 3 ciphertexts

    min_range = 2**2
    max_range = 2**8

    #Stores Private Keys
    private_keys= []
    public_keys = []

    for i in range(e):
        pub1, priv1 = rsa(min_range, max_range, e=e)
        inKeys = False


        #If private key is already been generated
        for private in private_keys:
            if priv1["d"] == private["d"]:
                inKeys = True


        while priv1["d"] == ValueError or inKeys:
            inKeys = False
            pub1, priv1 = rsa(min_range, max_range, e=e)

            for private in private_keys:
                if priv1["d"] == private["d"]:
                    inKeys = True

        private_keys.append(priv1)
        public_keys.append(pub1)



    ciphertexts = []
    for key in public_keys:
        ciphertexts.append(encrypt(message, key))

    # Given only ciphertexts, e, and n, we can work back what our original message was

    # CRT
    N = pub1["n"] * pub2["n"] * pub3["n"]
    N1 = N / pub1["n"]
    N2 = N / pub2["n"]
    N3 = N / pub3["n"]



    #CRT
    N=1

    for key in public_keys:
        N = N* key["n"]


    M =0

    print("Actual Plaintext:", message)
    for count, key in enumerate(public_keys):

        inversed = mod_inverse(N/key["n"], key["n"]) #50-50 chance of giving us a ValueError because there isn't a 

        print("CipherText", count, ":",  ciphertexts[count], " | Calculating Modular Inverse of N: ", inversed)

        M += ciphertexts[count] * inversed * N/key["n"]


    M = M % N

    m = M**(1.0/e)
    print("Plaintext Approximated from ciphertexts via CRT: ", m)


#Weiner's Attack

def wiener_n(q):
    """Generates random values p, q, and d where q < p < 2q and d < 1/3(n)^1/4"""

    min_range = q
    max_range = 2*q

    pub, priv = rsa(min_range, max_range)

    #Fulfill initial conditions
    while priv["d"] >= ((1/3)*(priv["n"])**1/4):
        pub, priv = rsa(min_range, max_range)

    return pub, priv




def weiner(message,):
    """ Weiner's Theorem (in the context of RSA): Given the public key (e, n), 
    if  q < p < 2q and d < 1/3(n)^1/4 then k/d is amongst the convergences of e/n"""
    




if __name__ == "__main__":
    hastad_ciphertexts(1234, 3)
