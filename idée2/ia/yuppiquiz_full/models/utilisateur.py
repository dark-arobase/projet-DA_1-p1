
# models/utilisateur.py
import hashlib
from dataclasses import dataclass, asdict

def hash_password(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

@dataclass
class Utilisateur:
    nom: str
    email: str
    _mot_de_passe_hash: str
    role: str = "joueur"

    @classmethod
    def create(cls, nom: str, email: str, mot_de_passe: str, role: str = "joueur"):
        return cls(nom=nom, email=email, _mot_de_passe_hash=hash_password(mot_de_passe), role=role)

    def check_password(self, mot_de_passe: str) -> bool:
        return hash_password(mot_de_passe) == self._mot_de_passe_hash

    def to_dict(self):
        d = asdict(self)
        d["mot_de_passe_hash"] = d.pop("_mot_de_passe_hash")
        return d

    @classmethod
    def from_dict(cls, d):
        pw = d.get("mot_de_passe_hash") or d.get("_mot_de_passe_hash") or ""
        return cls(nom=d["nom"], email=d["email"], _mot_de_passe_hash=pw, role=d.get("role","joueur"))
