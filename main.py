import pyscreeze
import datetime
import pyautogui
import time
import cv2

boot = True

while boot == True: #inicia o loop do boot

    procurar = "sim"
    while procurar == "sim": #inicia o loop de procura
    img = pyautogui.locateCenterOnScreen('capturar.png', confidence=0.7) #especifica a imagem que está sendo procurada 



    # recebe a hora e o munuto do pc
    h = datetime.datetime.now() 
    m = datetime.datetime.now() 

    hora = int(h.strftime("%H")) 
    minuto = int(m.strftime("%M"))

    if hora == 12 and minuto == 10: #inicia a procura do boot caso o horario recebido for o da condição

        procurar = "sim"

        while procurar == "sim": #inicia o loop de procura 
            try:
                img = pyautogui.locateCenterOnScreen('capturar.png', confidence=0.7) #especifica a imagem que está sendo procurada 
                pyautogui.click(img.x, img.y) #realiza o click nas cordenadas imagem encontrada
                procurar = "não" #ao realizar o click ele finaliza a procura
            #enquanto a imagem não for enconatrara ele emitirá uma mensagem informando que ainda não foi encontrado
            except: 
                time.sleep(1)
                print("não encontrei")
                procurar = "sim" #caso não encontrou ele volta a repitir a procura

        boot = False #ao finalizar a procura ele atribui o valor Falso a variavel boot, finalizando assim o loop
    elif hora > 12: #caso a hora for maior que 12 não fará sentindo realizar a busca pois a aula já foi encerrada
        print("Volte amanhã")
        boot = False

