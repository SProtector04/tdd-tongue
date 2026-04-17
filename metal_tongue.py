class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True
        self.position = (0, 0)
        
    def atacar(self, objetivo, dano):
        objetivo.hp -= dano
        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False
    def curar(self, objetivo, cura):
        if not objetivo.esta_vivo:
            return  # Regla: Los muertos no se curan
        objetivo.hp += cura
        if objetivo.hp > 1000:
            objetivo.hp = 1000  # Regla: Límite de HP máximo
            
    def move(self, x, y):
        self.position = (x, y)
    
    def say(self, mensaje):
        return mensaje