from utilisateurs import Utilisateur
from quiz import Question, Reponse, Quiz
import datetime
import json

#----------------------------------------------
#Creation de la classe du createur de quiz
class createur(Utilisateur):
    def __init__(self, id:int, nom:str, email:str, mdp:str):
        super().__init__(id, nom, email, mdp)
        self.id=id
        self.nom=nom
        self.email=email
        self._mdp=mdp
           

    def creerQuiz(self, titre:str, nbr_question:int ): #le createur creer de nouveau quiz
        t=input("Entrez le nom du quiz: ")
        id=input("entrer le id: ")
        date= datetime.date.today()
        quiz=Quiz(t, id, date )

        print("Ajouter les questions dans le quiz\n")
        i=input(int("nombre de questuions :"))
        for j in range(i):
            quiz.ajoutquestion(self)
            quiz.ajoutreponse(self)
        new_quiz={
                            "id":quiz.id,
                            "date creation":quiz.date_creation,
                            "titre":quiz.titre,
                            "questions":[
                                {
                                    "question": el.p,
                                    "choix":el.choix,
                                    "reponse":quiz.getreponse(el)
                                } for el in quiz.question
                            ]
                        }    

        with open("quiz.json", r, encoding="utf-8") as f: # le quiz est ajouter dans j.son pour la sauvegarde
                data=json.load(f)
        data.append(new_quiz)
        
        with open("quiz.json", w, encoding="utf-8") as f:
             json.dump(data, f, indent=3)
            
        
    def modifierquiz(self):
        option=input(int("Vous avez plusieurs option:\n" \
        "1. ajouter des questions\n" \
        "2. supprimer une question\n" \
        "3.changer une reponse\n" \
        "Que choisissez-vous? "))

        if option==1:
            with open("quiz.json", r, encoding="utf-8") as f:
                data=json.load(f)
            id_quiz=input(int("Entrez l'id du quiz a modifier :"))
            for element in data:
                 if element["id"]==id_quiz:
                      n=input(int("nombre de questions a ajouter :"))
                      for j in range(n):
                          question=input(str("Entrez la question: "))
                          choix=input(list("Entrez les choix de reponse: "))
                          reponse=input(str("Entrez la reponse correcte: "))
                          new_question={
                              "question":question,
                              "choix":choix,
                              "reponse":reponse
                          }
                          element["questions"].append(new_question)
        if option ==2:
             id_quiz=input(int("Entrez l'id du quiz a modifier :"))
             with open("quiz.json", r, encoding="utf-8") as f:
                 data=json.load(f)
             for element in data:
                 if element["id"]==id_quiz:
                     n=input(int("nombre de questions a supprimer :"))
                     for j in range(n):
                         question=input(str("Entrez la question a supprimer: "))
                         for q in element["questions"]:
                             if q["question"]==question:
                                 element["questions"].remove(q)
        if option==3:
             id_quiz=input(int("Entrez l'id du quiz a modifier :"))
             with open("quiz.json", r, encoding="utf-8") as f:
                 data=json.load(f)
             for element in data:
                 if element["id"]==id_quiz:
                     n=input(int("nombre de reponses a changer :"))
                     for j in range(n):
                         question=input(str("Entrez la question dont vous voulez changer la reponse: "))
                         for q in element["questions"]:
                             if q["question"]==question:
                                 nouvelle_reponse=input(str("Entrez la nouvelle reponse: "))
                                 q["reponse"]=nouvelle_reponse
                                 break

    def supprimerquiz(self):
        id_quiz=input(int("Entrez l'id du quiz a supprimer :"))

        with open("quiz.json", r, encoding="utf-8") as f:
                data=json.load(f)
        for element in data:
             if element["id"]==id_quiz:
                  data.remove(element)
            