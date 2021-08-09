from math import sin, cos, radians
from pygame         import init, Color
from pygame.display import set_mode, update
from pygame.event   import get
from pygame.gfxdraw import pixel

def posPlano(PTO_CAM):
    '''OBJ: Calcula la pos del plano a partir del pto de la camara
    '''
    res = [0, 0, 0]
    
    POS_CAM, ROT_CAM = PTO_CAM
    POS_CAM_X, POS_CAM_Y, POS_CAM_Z = POS_CAM

    ALFA, BETA, GAMMA = ROT_CAM    
    ALFA, BETA, GAMMA = radians(ALFA),\
                        radians(BETA),\
                        radians(GAMMA)
       
    if 0 <= ALFA <= 90: # ++ 1er cuad [0, 90]
        res = [cos(ALFA), sin(ALFA), POS_CAM_Z]

    elif 90 < ALFA <= 180: # -+ 2o cuad (90, 180]
        res = [-cos(ALFA), sin(ALFA), POS_CAM_Z]

    elif 180 < ALFA <= 270: # -- 3er cuad (180, 270]    
        res = [-cos(ALFA), -sin(ALFA), POS_CAM_Z]

    elif 270 < ALFA < 360: # +- 4o cuad (270, 360)
        res = [cos(ALFA), -sin(ALFA), POS_CAM_Z]
 
    return res

ESCALA = 150
def getPixel():
    SEPARACION_LATERAL = ESCALA # 30 # ESCALA // 10
    SEPARACION_ALTURA = 0

    return (int(ESCALA * POS_PLANO_X) +\
            SEPARACION_LATERAL,\
            int(ESCALA * (1 - POS_PLANO_Y)) +\
            SEPARACION_ALTURA)

def pintaTabla(POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z):
    POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z = round(POS_PLANO_X, 2),\
                        round(POS_PLANO_Y, 2),\
                        round(POS_PLANO_Z, 2)
    POS_PLANO = [POS_PLANO_X, POS_PLANO_Y,\
                 POS_PLANO_Z]

    ANCHURA_PIXEL, ALTURA_PIXEL = getPixel()
    print("\npinto pixel en (",\
          ANCHURA_PIXEL, ",", ALTURA_PIXEL,\
          ")\n\nrotCam =", rotCam,\
          "\nposPlano =", POS_PLANO)

def pintaPixel():
    ANCHURA_PIXEL, ALTURA_PIXEL = getPixel()
    
    pixel(PANTALLA, ANCHURA_PIXEL, ALTURA_PIXEL,\
          BLANCO)

ANCHURA, ALTURA, NEGRO, BLANCO = 400, 400,\
                                Color(0, 0, 0),\
                                Color(255, 255, 255)

rotCam, v = [0, 0, 0], 5 # º

POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z = posPlano([[0,0,0],\
                                          rotCam])

PANTALLA = set_mode((ANCHURA, ALTURA))

init()
pintaPixel()
update()

pintaTabla(POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z)

while True: 
    ent = input("\n-/+ q/e alfa, a/d beta, z/c gamma:\n").lower()

    if ent in ("qeadzc"):
        alfa, beta, gamma = rotCam

        if ent == "q":
            alfa -= v

        elif ent == "e":
            alfa += v

        elif ent == "a":
            beta -= v

        elif ent == "d":
            beta += v

        elif ent == "z":
            gamma -= v

        elif ent == "c":
            gamma += v

        if alfa < 0 or alfa >= 360: # [0, 360)
            alfa %= 360
            print("\nalfa fue normalizado") 

        rotCam = [alfa, beta, gamma]

        POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z = posPlano([[0,0,0],\
                                        rotCam])

        PANTALLA.fill(NEGRO)
        pintaPixel()
        update()

        pintaTabla(POS_PLANO_X, POS_PLANO_Y,\
                   POS_PLANO_Z)

    for evento in get():
        pass
        
   
    
      

