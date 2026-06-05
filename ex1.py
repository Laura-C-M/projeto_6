import cv2 #importar a biblioteca

#Carrega a imagem do disco
#Certifique-se de que o caminho da imagem está correto
img = cv2.imread("image.jpg")

#Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro:Não foi possível carregar a imagem. Verifique o caminho do ficheiro.")
else:
    #Exibe a imagem numa janela chamada 'Janela'
    cv2.imshow("Janela",img)

    #Espera indefinidamente por uma tecla pressionada
    #O valor 0 significa que espera para sempre
    cv2.waitKey(0)

    #Destrói todas as janelas criadas pelo CV2
    cv2.destroyAllWindows()
