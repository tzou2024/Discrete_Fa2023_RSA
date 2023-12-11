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


<<<<<<< Updated upstream
M^e = C1 mod n1

2. These different ciphertexts used multiple different p & q (to generate n1, n2, n3, etc), 
but the public key (e) is the same.
=======
2. These different ciphertexts used multiple different p & q (to generate n1, n2, n3, etc), but the public key (e) is the same
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
    keys = []

    pub1, priv1 = rsa(min_range, max_range, e=e)
    pub2, priv2 = rsa(min_range, max_range, e=e)
    pub3, priv3 = rsa(min_range, max_range, e=e)

    # Make sure the private keys are all different & exist
    while type(priv1["d"]) == ValueError:
        pub1, priv1 = rsa(min_range, max_range, e=e)
    while (
        type(priv2["d"]) == ValueError
        or (priv2["d"] == priv1["d"])
        or (priv2["d"] == priv3["d"])
    ):
        pub2, priv2 = rsa(min_range, max_range, e=e)
    while (
        type(priv3["d"]) == ValueError
        or (priv3["d"] == priv2["d"])
        or (priv3["d"] == priv1["d"])
    ):
        pub3, priv3 = rsa(min_range, max_range, e=e)

    # check that all public keys are the same
    if pub1["e"] == pub2["e"] == pub3["e"] == e:
        print("All public keys are true")
=======
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
>>>>>>> Stashed changes

        private_keys.append(priv1)
        public_keys.append(pub1)


<<<<<<< Updated upstream
    # Generate 3 different ciphertexts of the same message
    c1 = encrypt(message, pub1)
    c2 = encrypt(message, pub2)
    c3 = encrypt(message, pub3)
=======

    ciphertexts = []
    for key in public_keys:
        ciphertexts.append(encrypt(message, key))
>>>>>>> Stashed changes

    # Given only ciphertexts, e, and n, we can work back what our original message was

    # CRT
    N = pub1["n"] * pub2["n"] * pub3["n"]
    N1 = N / pub1["n"]
    N2 = N / pub2["n"]
    N3 = N / pub3["n"]

<<<<<<< Updated upstream
    u1 = mod_inverse(N1, pub1["n"])
    u2 = mod_inverse(N2, pub2["n"])
    u3 = mod_inverse(N3, pub3["n"])
    M = (c1 * u1 * N1 + c2 * u2 * N2 + c3 * u3 * N3) % N
    print(M)
    m = M ** (1.0 / 3.0)
    print(m)
=======


    #CRT
    N=1
>>>>>>> Stashed changes

    for key in public_keys:
        N = N* key["n"]

<<<<<<< Updated upstream
# Weiner's Attack
=======

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
def weiner(message,):
    """ Weiner's Theorem (in the context of RSA): Given the public key (e, n), 
    if  q < p < 2q and d < 1/3(n)^1/4 then k/d is amongst the convergences of e/n"""
    


>>>>>>> Stashed changes


if __name__ == "__main__":
    hastad_ciphertexts(1234, 3)
