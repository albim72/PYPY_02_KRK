class KlasaB:
    def __init__(self,z):
        self.z = z**3
        
    def dziel(self,k):
        return self.z/k if k !=0 else 0
