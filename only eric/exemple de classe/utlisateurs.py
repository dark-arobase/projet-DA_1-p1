class Utilisateur:
    def __init__(self, id:int, nom:str, email:str, mdp:str):
        self.id=id
        self.nom=nom
        self.email=email
        self._mdp=mdp
    
