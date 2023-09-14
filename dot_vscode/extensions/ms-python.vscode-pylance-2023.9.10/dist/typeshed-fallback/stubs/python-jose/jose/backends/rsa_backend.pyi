from typing import Any
from typing_extensions import Self

from .base import Key

LEGACY_INVALID_PKCS8_RSA_HEADER: bytes
ASN1_SEQUENCE_ID: bytes
RSA_ENCRYPTION_ASN1_OID: str

# Enable when we can use stubs from installed dependencies:
# from rsa import PublicKey
def pem_to_spki(pem, fmt: str = "PKCS8"): ...

class RSAKey(Key):
    SHA256: str
    SHA384: str
    SHA512: str
    hash_alg: str
    def __init__(self, key, algorithm) -> None: ...
    def sign(self, msg: bytes) -> bytes: ...
    def verify(self, msg: bytes, sig: bytes) -> bool: ...
    def is_public(self) -> bool: ...
    def public_key(self) -> Self: ...
    def to_pem(self, pem_format: str = "PKCS8") -> bytes: ...
    def to_dict(self) -> dict[str, Any]: ...
    def wrap_key(self, key_data: bytes) -> bytes: ...
    def unwrap_key(self, wrapped_key: bytes) -> bytes: ...
