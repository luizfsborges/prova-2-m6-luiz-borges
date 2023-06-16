# prova-2-m6-luiz-borges

# Parte prática da prova 2 do módulo 6 de Engenharia de Computação

## Enunciado

Desenvolva um código em Python capaz de utilizar o openCV para a leitura de um vídeo (frame a frame) e, para cada frame, o seu código deve identificar e marcar na imagem os retângulos correspondentes a cada uma das faces encontradas. Ao final do código, um novo vídeo deve ser salvo com a(s) face(s) identificada(s).

Para a detecção das faces, pode-se utilizar a abordagem que quiser (haar cascade, filtro de correlação, YOLO). Não há a necessidade de fazer o fine tuning da detecção. Se o código é capaz de identificar faces corretamente na maior parte do tempo, considera-se como uma aplicação aceitável para esta etapa da prova.

## **Documentação da resolução da atividade prática**

A partir dos exemplos fornecidos pelo professor, um vídeo cujo conteúdo é de alta qualidade é lido frame a frame por meio da função VideoCapture do OpenCV. Como medida de gerenciamento de possiveis erros de leitura do arquivo, é feita uma checagem para verificar se o arquivo foi aberto corretamente. Caso não tenha sido, uma mensagem de erro é exibida e o programa é encerrado.

Uma vez que o objetivo da atividade proposta é a detecção de faces, foi implementado um modelo pré-treinado para este fim que, inclusive, foi sugerido no enunciado: O Haar Cascade. Este modelo é carregado por meio da função CascadeClassifier do OpenCV.

Ainda como objetivo do exercício, temos a o requisito de salvar o vídeo com as faces detectadas. Para isso, é criado um objeto do tipo VideoWriter, que recebe como parâmetros o nome do arquivo de saída, o codec utilizado, o FPS do vídeo e o tamanho do vídeo. O codec utilizado foi o DIVX, O FPS do vídeo de saída foi definido como 24, e tamanho do vídeo de saída foi mantido o mesmo do vídeo de entrada.

Na função principal do script o vídeo carregado e lido frame a frame. Para que as faces contidas nesses frames possam ser reconhecidas pelo modelo Haar Cascade, cada frame é convertido para uma escala de cinza. Em seguida, o modelo pré-treinado é utilizado para detectar as faces presentes no frame. Uma vez que as faces são detectadas, um retângulo é desenhado em volta de cada uma delas, uma vez que a variável passa a armazenar as coordenadas das faces que encontrou. Além do requisitado no enunciado, fez-se necessário exibir um texto contendo obviedades acima de cada retângulo desenhado. Por fim, cada frame do vídeo com as faces detectadas e seu respectivo texto é exibido em uma janela.

Atendendo ao último requisito do enunciado, o vídeo de saída é registrado por meio do método write do objeto output_video. Ao término da leitura dos frames do vídeo de entrada, o objeto output_video é liberado, assim como o objeto video_capture. Por fim, todas as janelas são fechadas.

O vídeo contendo as faces detectadas com o texto pode ser encontrado no diretório ./saida/out.avi, bem como abaixo:

https://github.com/luizfsborges/prova-2-m6-luiz-borges/assets/40524905/2c4a3bb0-f375-4cf6-a243-8e5cf70f6eb4

