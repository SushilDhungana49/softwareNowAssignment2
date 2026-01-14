"""
This script reads 'raw_text.txt', encrypts it to 'encrypted_text.txt',
decrypts that to 'decrypted_text.txt', and verifies the result.

Encryption rules:
- Lowercase a-m: shift forward by (shift1 * shift2) positions (within the half)
- Lowercase n-z: shift backward by (shift1 + shift2) positions (within the half)
- Uppercase A-M: shift backward by shift1 positions (within the half)
- Uppercase N-Z: shift forward by shift2**2 positions (within the half)
- Other characters unchanged

"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_FILE = os.path.join(BASE_DIR, "raw_text.txt")
ENCRYPTED_FILE = os.path.join(BASE_DIR, "encrypted_text.txt")
DECRYPTED_FILE = os.path.join(BASE_DIR, "decrypted_text.txt")


def encrypt_char(char: str, shift1: int, shift2: int) -> str:
    """Encrypt a single character per the assignment rules."""
    # Lowercase
    if char.islower():
        pos = ord(char) - ord('a')  # 0..25
        if pos < 13:  # a-m
            shift = (shift1 * shift2) % 13
            new_pos = (pos + shift) % 13
            return chr(ord('a') + new_pos)
        else:  # n-z
            shift = (shift1 + shift2) % 13
            offset = pos - 13
            new_offset = (offset - shift) % 13
            return chr(ord('a') + 13 + new_offset)

    # Uppercase
    if char.isupper():
        pos = ord(char) - ord('A')  # 0..25
        if pos < 13:  # A-M
            shift = shift1 % 13
            new_pos = (pos - shift) % 13
            return chr(ord('A') + new_pos)
        else:  # N-Z
            shift = (shift2 ** 2) % 13
            offset = pos - 13
            new_offset = (offset + shift) % 13
            return chr(ord('A') + 13 + new_offset)

    # Other characters unchanged
    return char


def decrypt_char(char: str, shift1: int, shift2: int) -> str:
    """Decrypt a single character by reversing the encryption rules."""
    # Lowercase
    if char.islower():
        pos = ord(char) - ord('a')
        if pos < 13:  # a-m -> was encrypted from a-m by forward (shift1*shift2)
            shift = (shift1 * shift2) % 13
            orig_pos = (pos - shift) % 13
            return chr(ord('a') + orig_pos)
        else:  # n-z -> was encrypted from n-z by backward (shift1+shift2)
            shift = (shift1 + shift2) % 13
            offset = pos - 13
            orig_offset = (offset + shift) % 13
            return chr(ord('a') + 13 + orig_offset)

    # Uppercase
    if char.isupper():
        pos = ord(char) - ord('A')
        if pos < 13:  # A-M -> was encrypted by backward shift1
            shift = shift1 % 13
            orig_pos = (pos + shift) % 13
            return chr(ord('A') + orig_pos)
        else:  # N-Z -> was encrypted by forward shift2**2
            shift = (shift2 ** 2) % 13
            offset = pos - 13
            orig_offset = (offset - shift) % 13
            return chr(ord('A') + 13 + orig_offset)

    # Other characters unchanged
    return char


def encrypt_file(input_file: str, output_file: str, shift1: int, shift2: int) -> bool:
    """Read input_file, encrypt content, write to output_file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        return False
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        return False

    encrypted = ''.join(encrypt_char(c, shift1, shift2) for c in content)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted)
        print(f"Encryption complete: '{input_file}' → '{output_file}'")
        return True
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")
        return False


def decrypt_file(input_file: str, output_file: str, shift1: int, shift2: int) -> bool:
    """Read encrypted file, decrypt content, write to output_file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        return False
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        return False

    decrypted = ''.join(decrypt_char(c, shift1, shift2) for c in content)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted)
        print(f"Decryption complete: '{input_file}' → '{output_file}'")
        return True
    except Exception as e:
        print(f"Error writing file {output_file}: {e}")
        return False


def verify_decryption(original_file: str, decrypted_file: str) -> bool:
    """Compare original and decrypted files and report differences."""
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            orig = f.read()
        with open(decrypted_file, 'r', encoding='utf-8') as f:
            dec = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error reading files: {e}")
        return False

    if orig == dec:
        print(f"\nSUCCESS: Decryption verified! '{decrypted_file}' matches '{original_file}'")
        return True

    # Report summary if mismatch
    print(f"\nFAILURE: Decryption did not match.")
    print(f"  Original length:  {len(orig)} characters")
    print(f"  Decrypted length: {len(dec)} characters")

    diff_count = 0
    for i, (o, d) in enumerate(zip(orig, dec)):
        if o != d:
            if diff_count < 5:
                diff_count += 1
    diff_count += abs(len(orig) - len(dec))
    print(f"  Total differences: {diff_count}")
    return False


def prompt_shifts():
    """Prompt user for integer shift1 and shift2, with validation."""
    while True:
        try:
            raw1 = input("Enter shift1 value (integer): ")
            raw2 = input("Enter shift2 value (integer): ")
            s1 = int(raw1.strip())
            s2 = int(raw2.strip())
            return s1, s2
        except ValueError:
            print("Error: Please enter valid integer values for both shifts. Try again.")


def main():
    print("=" * 60)
    print("TEXT FILE ENCRYPTION/DECRYPTION PROGRAM")
    print("=" * 60)

    shift1, shift2 = prompt_shifts()

    # Step 1: Encrypt
    print("\n[1] Encrypting...")
    if not encrypt_file(RAW_FILE, ENCRYPTED_FILE, shift1, shift2):
        return

    # Step 2: Decrypt
    print("\n[2] Decrypting...")
    if not decrypt_file(ENCRYPTED_FILE, DECRYPTED_FILE, shift1, shift2):
        return

    # Step 3: Verify
    print("\n[3] Verifying...")
    verify_decryption(RAW_FILE, DECRYPTED_FILE)

    print("\n" + "=" * 60)
    print("Program complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
