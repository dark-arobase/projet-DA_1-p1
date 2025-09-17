from utilisateurs import Utilisateur
from quiz import Question, Reponse, Quiz
import datetime

class createur(Utilisateur):
    def __init__(self, id:int, nom:str, email:str, mdp:str):
        super().__init__(id, nom, email, mdp)
        self.id=id
        self.nom=nom
        self.email=email
        self._mdp=mdp
           

    def creerQuiz(self, titre:str, nbr_question:int ):
        t=input("Entrez le nom du quiz: ")
        id=input("entrer le id: ")
        date= datetime.date.today()
        quiz=Quiz(t, id, date )

        print("Ajouter les questions dans le quiz\n")
        i=input(int("nombre de questuions :"))
        for j in range(i):
            quiz.ajoutquestion(self)
            quiz.ajoutreponse(self)

            new_quiz={"nom": {}}

            with open("quiz.json", +w, encoding="utf-8") as f:
                json.dump()
            
        



    def modifierquiz(self):
        pass


    def supprimerquiz(self):
        pass