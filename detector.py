def detect_algorithm(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read().lower()

    if "rsa" in content:
        return "RSA"
    elif "aes" in content:
        return "AES"
    elif "sha" in content:
        return "SHA-1"
    else:
        return "Unknown"
