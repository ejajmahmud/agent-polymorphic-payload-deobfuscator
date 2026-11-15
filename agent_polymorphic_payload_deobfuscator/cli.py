"""CLI for Polymorphic Payload Deobfuscator."""
import argparse
import base64
from .core import RecursiveDeobfuscator

def main():
    parser = argparse.ArgumentParser(description="Polymorphic Payload Deobfuscator CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate recursive payload unwrapping")
    args = parser.parse_args()

    inner = "malicious_command"
    hex_str = inner.encode("utf-8").hex()
    b64_str = base64.b64encode(hex_str.encode("utf-8")).decode("utf-8")
    obfuscated = "\u200b" + b64_str + "\u200b"

    cleaned = RecursiveDeobfuscator.deobfuscate(obfuscated)
    print(f"Obfuscated input: '{obfuscated}'")
    print(f"Deobfuscated result: '{cleaned}'")

if __name__ == "__main__":
    main()
