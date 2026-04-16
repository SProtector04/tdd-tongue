from metal_tongue import Personaje

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange (Preparar)
    heroe = Personaje()
    
    # Assert (Verificar)
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True

def test_personaje_recibe_dano():
    heroe = Personaje()
    enemigo = Personaje()
    
    # Act (Actuar)
    enemigo.atacar(heroe, dano=200)
    
    # Assert
    assert heroe.hp == 800
    
def test_personaje_muere_si_hp_llega_a_cero():
    heroe = Personaje()
    enemigo = Personaje()
    
    enemigo.atacar(heroe, dano=1500)
    
    assert heroe.hp == 0  # El HP no debe quedar en -500
    assert heroe.esta_vivo == False

def test_curar_personaje():
    heroe = Personaje()
    enemigo = Personaje()
    
    enemigo.atacar(heroe, dano=200)
    heroe.curar(heroe, cura=100)
    
    assert heroe.hp == 900   #Debe tener 900
    
def test_no_curar_mas_del_maximo():
    heroe = Personaje()
    enemigo = Personaje()
    
    enemigo.atacar(heroe, dano=100)
    heroe.curar(heroe, cura=200)
    
    assert heroe.hp == 1000   #Debe tener 1000

def test_los_muertos_no_se_curan():
    heroe = Personaje()
    heroe.esta_vivo = False
    heroe.hp = 0
    
    heroe.curar(heroe, cura=500)
    
    assert heroe.hp == 0 #Sigue muerto
    assert heroe.esta_vivo == False #Bien muerto