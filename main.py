#
# Importação de bibliotecas básicas para o funcionamento do app
# cv2: Computer Vision (visão computacional)
# CVZone: biblioteca com funções específicas relativas à visão computacional
# time: usada para cálculo aproximado dos frames por segundo (fps)
#
import cv2, cvzone, time
from cvzone.FaceMeshModule import FaceMeshDetector # (dertecção de rostos)
from cvzone.HandTrackingModule import HandDetector # (detector de mãos)

# Cria um objeto que captura os frames lidos pela webcam
# 0 (zero) é a webcam do meo notebook. Valores maiores indicam outras webcams conetcadas
cap = cv2.VideoCapture(0)

# variável que armazena a úmica face detectada, pois maxFaces = 1
detector = FaceMeshDetector(maxFaces=1)

# variável que armazena as mãos detectadas
hd = HandDetector(detectionCon=0.8,maxHands=2)

# inicia o cálculo dos frames por segundo (fps)
tempo_anterior = 0

# loop principal de leitura dos frames individuais
while True:

    # atribui à variável "img" os frames lidos
    # "retorno" é outro dado retornado por read()
    retorno, img = cap.read()

    # inverte (espelha) cada um dos frames lidos
    # facilita a compreensão da identificação das mãos
    img = cv2.flip(img, 1)

    # captura o tempo atual para calcular fps
    tempo_atual = time.time()

    # calcula o fps
    # em tempo: há um outro método específico para isso,
    # não ficou como eu esparava
    fps = 1/(tempo_atual-tempo_anterior)

    # atualiza o tempo para o cálculo do fps posterior
    tempo_anterior = tempo_atual

    # escreve, no frame lido, o valor do fps calculado
    # fps: calculado acima
    # 20,70: posição no frame
    # cv2.FONT...: fonte escolhida (há muitas outras)
    # 3: tamanho da fonte
    # (255,0,0): cor da fonte, no formato BGR (blue, green, red)
    # 3: espessura da fonte
    cv2.putText(img, f'fps: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # detecta e armazena as mãos presentes em cada frame
    # flipType = False usado porque a imagem foi invertida antes da detecção
    hands, img = hd.findHands(img, flipType=False)

    # detecta e armazena os rostos, em cada frame
    # draw = false esconde as centenas de pontos detectados em cada frame
    img, faces = detector.findFaceMesh(img, draw=False)

    # para cada rosto detectado...
    if faces:
        face = faces[0]
        
        # centro do olho esquerdo, presente no conjunto de landmarks
        OlhoEsquerdo = face[145]

        # centro do olho direito, presente no conjunto de landmarks
        OlhoDireito = face[374]

        # distância entre os centros dos olhos (em pixels)
        w, _ = detector.findDistance(OlhoEsquerdo, OlhoDireito)

        # distância média entre os centrods dos olhos,
        # estatisticamente determinados (em cm)
        W = 6.3

        # distância focal determinada experimentalmente (em pixels)
        f = 840

        # cálculo da distância do rosto à câmera
        d = (W*f)/w

        # escreva a distância calculada
        cvzone.putTextRect(img, f'Dist: {int(d)} cm', (face[10][0]-95, face[10][1]-50), scale=2)

    # mostra o frame
    cv2.imshow("Face and hands",img)

    # aguarda o pressionar de uma tecla
    key = cv2.waitKey(1)

    # encerra o loop quando a tecla ESC é pressionada
    if key == 27:
        break

# libera a captura de frames
cap.release()

# fecha tudo
cv2.destroyAllWindows()
