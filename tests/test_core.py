"""Automated test suite for Polymorphic Payload Deobfuscator."""
import unittest
import base64
from agent_polymorphic_payload_deobfuscator.core import RecursiveDeobfuscator

class TestRecursiveDeobfuscator(unittest.TestCase):
    def test_strip_zero_width_and_decode_b64(self):
        raw = "secret_code"
        b64 = base64.b64encode(raw.encode("utf-8")).decode("utf-8")
        obf = f"\u200b{b64}\u200d"
        self.assertEqual(RecursiveDeobfuscator.deobfuscate(obf), raw)
