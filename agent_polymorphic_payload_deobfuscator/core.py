"""Core implementation of polymorphic payload deobfuscator."""
import base64
import binascii
import re

class RecursiveDeobfuscator:
    ZERO_WIDTH_CHARS = ["\u200b", "\u200c", "\u200d", "\ufeff"]

    @classmethod
    def strip_zero_width(cls, text: str) -> str:
        res = text
        for zw in cls.ZERO_WIDTH_CHARS:
            res = res.replace(zw, "")
        return res

    @classmethod
    def try_decode_base64(cls, text: str) -> str:
        text = text.strip()
        if len(text) > 4 and len(text) % 4 == 0 and re.match(r"^[A-Za-z0-9+/=]+$", text):
            try:
                decoded = base64.b64decode(text.encode("ascii")).decode("utf-8")
                if decoded.isprintable():
                    return decoded
            except Exception:
                pass
        return text

    @classmethod
    def try_decode_hex(cls, text: str) -> str:
        text = text.strip()
        if len(text) >= 4 and len(text) % 2 == 0 and re.match(r"^[0-9a-fA-F]+$", text):
            try:
                decoded = bytes.fromhex(text).decode("utf-8")
                if decoded.isprintable():
                    return decoded
            except Exception:
                pass
        return text

    @classmethod
    def deobfuscate(cls, text: str, max_depth: int = 4) -> str:
        curr = cls.strip_zero_width(text)
        for _ in range(max_depth):
            b64_attempt = cls.try_decode_base64(curr)
            if b64_attempt != curr:
                curr = b64_attempt
                continue
            hex_attempt = cls.try_decode_hex(curr)
            if hex_attempt != curr:
                curr = hex_attempt
                continue
            break
        return curr
