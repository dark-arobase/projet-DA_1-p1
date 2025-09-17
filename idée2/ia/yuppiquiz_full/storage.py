
# storage.py
import json
import os
from models.utilisateur import Utilisateur
from models.quiz import Quiz, Question, Score, gen_pin

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
QUIZZES_FILE = os.path.join(DATA_DIR, "quizzes.json")
SCORES_FILE = os.path.join(DATA_DIR, "scores.json")

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    for f in [USERS_FILE, QUIZZES_FILE, SCORES_FILE]:
        if not os.path.exists(f):
            with open(f, "w") as fh:
                json.dump({}, fh)

def load_users():
    ensure_data_dir()
    with open(USERS_FILE, "r") as f:
        raw = json.load(f)
    users = {}
    for email, d in raw.items():
        users[email] = Utilisateur.from_dict(d)
    return users

def save_users(users: dict):
    ensure_data_dir()
    ser = {email: user.to_dict() for email, user in users.items()}
    with open(USERS_FILE, "w") as f:
        json.dump(ser, f, indent=2)

def load_quizzes():
    ensure_data_dir()
    with open(QUIZZES_FILE, "r") as f:
        raw = json.load(f)
    quizzes = {}
    for qid, d in raw.items():
        quizzes[qid] = Quiz.from_dict(d)
    return quizzes

def save_quizzes(quizzes: dict):
    ensure_data_dir()
    ser = {qid: quiz.to_dict() for qid, quiz in quizzes.items()}
    with open(QUIZZES_FILE, "w") as f:
        json.dump(ser, f, indent=2)

def load_scores():
    ensure_data_dir()
    with open(SCORES_FILE, "r") as f:
        raw = json.load(f)
    return raw

def save_scores(scores: dict):
    ensure_data_dir()
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def make_unique_pin():
    quizzes = load_quizzes()
    existing = set(quizzes.keys())
    return gen_pin(existing)
