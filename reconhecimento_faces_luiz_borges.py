# Script desenvolvido a partir dos exemplos encontrados no repositório fornecido pelo professor no enunciado: https://github.com/rmnicola/p2-pratica

# Importação das bibliotecas necessárias para o desenvolvimento do script
import cv2

# Abre o arquivo de video
video_capture = cv2.VideoCapture('./assets/namorada_do_vampeta.mp4')

# Checa se foi possivel abrir o arquivo
if not video_capture.isOpened():
    print("Error opening video file")
    exit(1)

# Carrega o classificador de faces
faceCascade = cv2.CascadeClassifier('./assets/haarcascade_frontalface_default.xml')

# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width_output  = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height_output = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width_output, height_output))

# Funcao principal
def main():

    # Loop de leitura frame por frame
    while True:
        # Le um frame do video e, guarda o resultado da leitura
        # Se nao houver mais frames disponiveis, ret sera falso
        ret, frame = video_capture.read()

        # Se nao conseguiu ler o frame, para o laco
        if not ret:
            break

        # Converte o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detecta as faces no frame
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        # Desenha um retangulo e exibe um texto com a verdade absoluta em volta das faces detectadas
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 0), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, 'O Rei do Futebol', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        # Exibe o frame
        cv2.imshow('O melhor de todos', frame)

        # Escreve o frame no output
        output_video.write(frame)

        # Se o usuario apertar q, encerra o playback
        # O valor utilizado no waiKey define o fps do playback
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
    # Fecha tudo
    output_video.release()
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()