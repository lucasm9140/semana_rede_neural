# bibilioteca opencv - pip install opencv-python
import cv2
# Importando mediapipe 
import mediapipe as mp # pip install mediapipe

# Capturar a camêra
cap = cv2.VideoCapture(0)

# Desenhar os pontos
mp_drawing = mp.solutions.drawing_utils

# coletar solução do Face Mesh
mp_face_mesh = mp.solutions.face_mesh

# Wifh liberação automatica de memoria - faz um tipo de limpeza, gerenciamento de memoria - se nao tiver usando ele fecha
# Enquanto a camera estiver aberta
with mp_face_mesh.Face.mesh(min_detection_confidence=0.5,min_tracking_confidence=0.5) as facemesh:

# Enquanto a camera estiver aberta
    while cap.isOpened():
        # Sucesso é booleano-0 e 1
        sucesso, frame = cap.read()
        if not sucesso:
            print('ignorando o frame vazio da camera')
            continue

        # Transformando de BGR para RGB
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        # processar o frame (Encontro do OpenCV - MediaPipe)
        saida_facemesh = facemesh.process(frame)
        
        # Transformando de RGB PARA BGR
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        # Vamos Desenhar ???
        # 1 - Fizemos a detecção do rosto com facemesh.process(frame)
        # 2 - Mostrar essa detecção
        # 3 - for (iteração)
            # 4 - face_landmarks - conjunto das coordenadas
                    # (Coletamos as coordenadas saida_facemesh)
        # 4.1 - multi_face_landmarks: x,y,z de cada ponto que o MP encontrar no rosto
        for face_landmarks in saida_facemesh.multi_face_landmarks:
            # Desenhando
            # 1 - frame
            # 2 - face_landmarks
            # 3 - FACEMESH_CONTOURS - especificar os pontos
            mp_drawing.draw_landmarks(frame,face_landmarks,mp_face_mesh.FACEMESH_CONTOURS)


        cv2.imshow('Camera', frame)
        # bitwise - tabela ASC II
        # ord() - retorna o valor Unicode(ou ASC II)
        # 0xFF valor hexadecimal da tabela ASC II estendida
        if cv2.waitKey(10) & 0xFF == ord('c'):
            break
        # c fecha a captura - na linha 19 cap.release fecha a camera, e destroyAllWindows verifica janelas abertas.
        cap.release()
        cv2.destroyAllWindows()