import random
import string
import requests

def generate_random_code():
    """Generate a random Minecraft redeem code."""
    valid_characters = ''.join(c for c in string.ascii_uppercase + string.digits if c not in "AEIOULS015")
    parts = []
    for _ in range(5):
        part = ''.join(random.choices(valid_characters, k=5))
        parts.append(part)
    return '-'.join(parts)

def check_code_validity_with_api(code):
    """Check code validity using an actual API call."""
    # Replace the following URL and parameters with actual API details
    api_url = "https://api.minecraftservices.com/redeem"  # Placeholder URL
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with actual authorization token
        "Content-Type": "application/json"
    }
    data = {
        "code": code
    }

    try:
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error checking code: {e}")
        return False

def write_codes_to_file(file_name, codes):
    """Write the list of codes to the specified file."""
    with open(file_name, "w") as file:
        for code in codes:
            file.write(code + "\n")
    print(f"Codes written to {file_name}")

def main():
    print("""
    ██████╗  ██████╗ ███╗   ███╗██████╗ ██╗     ███████╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║     ██╔════╝
    ██████╔╝██║   ██║██╔████╔██║██████╔╝██║     █████╗  
    ██╔═══╝ ██║   ██║██║╚██╔╝██║██╔══██╗██║     ██╔══╝  
    ██║     ╚██████╔╝██║ ╚═╝ ██║██║  ██║███████╗███████╗
    ╚═╝      ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
    """)

    try:
        num_codes = int(input("How many codes do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    valid_codes = []
    invalid_codes = []

    for _ in range(num_codes):
        code = generate_random_code()
        print(f"Generated code: {code}")  # Debug print statement
        if check_code_validity_with_api(code):
            valid_codes.append(code)
            print(f"Valid code found: {code}")
        else:
            invalid_codes.append(code)
            print(f"Invalid code found: {code}")

    write_codes_to_file("valid.txt", valid_codes)
    write_codes_to_file("invalid.txt", invalid_codes)

    print(f"Total valid codes: {len(valid_codes)}")
    print(f"Total invalid codes: {len(invalid_codes)}")

if __name__ == "__main__":
    main()
