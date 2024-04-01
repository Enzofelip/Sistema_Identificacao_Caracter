import cv2
import pytesseract
import pandas as pd

# imagem = cv2.imread("D:/CursoPython/secao_03/desafioSenai/placa1.png")
# if imagem is None:
#     print("Erro ao carregar a imagem.")
# else:
#     # Exiba a imagem
#     cv2.imshow("Imagem do", imagem)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# pytesseract.pytesseract.tesseract_cmd=r"C:\Users\rinal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# imagem = pytesseract.image_to_string(imagem)

# print(imagem)


# Configuração do pytesseract (certifique-se de que o executável do Tesseract esteja instalado em seu sistema)
pytesseract.pytesseract.tesseract_cmd=r"C:\Users\rinal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


# Configuração do caminho para o Tesseract OCR
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rinal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    # Inicializa a captura de vídeo da webcam (0 representa a webcam padrão)
cap = cv2.VideoCapture(0)

while True:
        # Lê um frame da webcam
    ret, frame = cap.read()

        # Converte o frame para escala de cinza para melhor desempenho do OCR
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Realiza OCR usando pytesseract
    text = pytesseract.image_to_string(gray_frame)

        # Exibe o texto no console
    print("Texto detectado:", text)

        # Compara o texto com os dados do CSV
    resultados = comparar_texto_com_csv(text, dados_csv)

        # Exibe os resultado

        # Exibe o frame com a janela OpenCV (opcional)
    cv2.imshow('Webcam OCR', frame)

        # Para sair do loop pressione a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Libera os recursos
cap.release()
cv2.destroyAllWindows()
