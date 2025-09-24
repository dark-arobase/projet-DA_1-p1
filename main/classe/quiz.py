class Quiz:
    def __init__(self, titre:str, id:int, date_creation:str, question, reponse):
        self.titre=titre
        self.id=id
        self.date_creation=date_creation
        self.question=[]
        self.reponse=[]
    
    def ajoutquestion(self, question):
        question=input("Ecrire ta question ici :\n")
        choix=[]
        for i in range(4):
             b=input("choix :")
             choix.append(b)
        a=Question(question, choix)
        self.question.append(a)
    
    def ajoutreponse(self, reponse):
        reponse=input("Ecrire la reponse ici:\n")
        b=Reponse(reponse)
        self.reponse.append(b)
    
    def getreponse(self, x):
        index=self.question.index(x)
        r=self.reponse[index]
        return r


class Question:
    def __init__(self, p:str, choix):
        self.p=p
        self.choix=choix

class Reponse:
    def __init__(self, r:str):
        self.r=r