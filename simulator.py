def simulate_attack(algorithm):
    if algorithm == "RSA":
        return "Shor's Algorithm (Factoring)"
    elif algorithm == "SHA-1":
        return "Grover's Algorithm (Hash Collision)"
    elif algorithm == "AES":
        return "Grover's Algorithm (Key Search)"
    else:
        return "No known quantum attack"
