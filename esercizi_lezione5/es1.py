class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono",self.ruolo+",",self.nome,self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome,corsi):
        super().__init__(nome, cognome)
        self.corsi = corsi
    def saluta(self):
        Persona.saluta(self)
        print("frequento i corsi:", self.corsi)

class Docente(Persona):
    def __init__(self,nome, cognome,corsi):
        super().__init__(nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        print("Docente dei corsi:",self.corsi)
    
    def insegnamento(self,studente):
        for i in studente.corsi:
            if i not in self.corsi:
                print("il docente non insegna tutti i corsi ")
                return False
        
                
        print("il docente insegna tutti i corsi")
        return True


def verifica_copertura(studenti, docenti):
    for studente in studenti:
        trovato = False

        for docente in docenti:
            if docente.insegnamento(studente): 
                trovato = True
                print(f"{docente.nome} {docente.cognome} copre {studente.nome} {studente.cognome}")
                break

        if not trovato:
            print(f"nessun docente copre tutti i corsi di  {studente.nome} {studente.cognome}")

