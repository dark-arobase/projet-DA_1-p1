
# models/quiz.py
from dataclasses import dataclass, asdict
import random
import time

def gen_pin(existing=None):
    existing = existing or set()
    while True:
        pin = str(random.randint(1000, 9999))
        if pin not in existing:
            return pin

@dataclass
class Question:
    texte: str
    reponses: list
    indice_bonne: int

    def to_dict(self):
        return {"texte": self.texte, "reponses": self.reponses, "indice_bonne": self.indice_bonne}

    @classmethod
    def from_dict(cls, d):
        return cls(texte=d["texte"], reponses=d["reponses"], indice_bonne=d["indice_bonne"])

@dataclass
class Quiz:
    id: str
    titre: str
    createur_email: str
    questions: list
    date_creation: float

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "createur_email": self.createur_email,
            "date_creation": self.date_creation,
            "questions": [q.to_dict() for q in self.questions]
        }

    @classmethod
    def from_dict(cls, d):
        qs = [Question.from_dict(qd) for qd in d.get("questions",[])]
        return cls(id=d["id"], titre=d["titre"], createur_email=d["createur_email"], questions=qs, date_creation=d.get("date_creation", 0))

@dataclass
class Score:
    quiz_id: str
    joueur_email: str
    points: int
    total: int
    date: float

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        return cls(quiz_id=d["quiz_id"], joueur_email=d["joueur_email"], points=d["points"], total=d["total"], date=d["date"])
