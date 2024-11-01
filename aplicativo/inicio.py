import cv2
# Capturar a camêra
cap = cv2.VideoCapture(0)
# Enquanto a camera estiver aberta
while cap.isOpened():
    # Sucesso é booleano-0 e 1
    sucesso, frame = cap.read()
    if not sucesso:
        print('ignorando o frame vazio da camera')
        continue
    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('c'):
        break
    # fecha a captura
    cap.release()
    cv2.destroyAllWindows()