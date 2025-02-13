class KlasaC:
    def __init__(self,msg):
        self.msg = msg

    def info(self):
        print(f"wadomość z klasy: {self.__class__.__name__} -> {self.msg}")
