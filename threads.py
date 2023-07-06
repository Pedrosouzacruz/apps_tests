from threading import Thread
import time
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print("Piloto: {}, KM {} \n".format(trajeto, piloto))


thread_carro_1 = Thread(target=carro, args=[1, "Pedro"])
thread_carro_2 = Thread(target=carro, args=[1.5, "Luely"])

thread_carro_1.start()
thread_carro_2.start()