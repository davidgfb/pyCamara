from math import sin, cos, radians
from pygame         import init
from pygame.display import set_mode, update
from pygame.event import get

def posPlano(PTO_CAM):
    '''OBJ: Calcula la pos del plano a partir del pto de la camara
    '''
    res = [0, 0, 0]
    
    POS_CAM, ROT_CAM = PTO_CAM
    POS_CAM_X, POS_CAM_Y, POS_CAM_Z = POS_CAM

    ALFA, BETA, GAMMA = ROT_CAM    
    ALFA, BETA, GAMMA = radians(ALFA), radians(BETA),\
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
        
#PROBADOR
init()
PANTALLA = set_mode((300, 300))

rotCam, v = [0, 0, 0], 1

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
        POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z = round(POS_PLANO_X, 2),\
                        round(POS_PLANO_Y, 2),\
                        round(POS_PLANO_Z, 2)
        POS_PLANO = [POS_PLANO_X, POS_PLANO_Y, POS_PLANO_Z]

        print("\nrotCam =", rotCam, "\nposPlano =", POS_PLANO)
        
    for evento in get():
        pass
      

