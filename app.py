import gtts # Módulo do Google que converte texto para fala
from playsound import playsound # Será usado para tocar o som gerado através do GTTS.


with open('frase.txt','r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha,lang='pt-br')
        frase.save('frase.mp3')
        playsound('frase.mp3')