class Quiz:
    def __init__(self, titre:str, id:int, date_creation:str):
        self.titre=titre
        self.id=id
        self.date_creation=date_creation
        self.question=[]
        self.reponse=[]
    
    def ajoutquestion(self, question):
        question=input("Ecrire ta question ici :\n")
        a=Question(question)
        choix=[]
        for i in range(4):
             b=input("choix :")
             choix.append(a)
        self.question.append(question, choix)
    
    def ajoutreponse(self, reponse):
        reponse=input("Ecrire la reponse ici:\n")
        b=Reponse(reponse)
        self.reponse.append(reponse)

class Question:
    def __init__(self, p:str, choix):
        self.p=p
        self.choix=choix

class Reponse:
    def __init__(self, r:str):
        self.r=r