from multiprocessing import Process
import os
import time

class Vocal1():
    def __init__(self,direccion):
        self.direccion=direccion
    def vocala(self):
        a=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
            char=archivo.read(1)
            if char.lower()=="a":
                    a=a+1
            else:
                if not char:
                    break
        archivo.close()
        return a

    def vocale(self):
        e=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="e":
                    e=e+1
                else:
                    if not char:
                        break
        archivo.close()
        return e

    def vocali(self):
        i=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="i":
                    i=i+1
                else:
                    if not char:
                        break
        archivo.close()
        return i

    def vocalo(self):
        o=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="o":
                    o=o+1
                else:
                    if not char:
                        break
        archivo.close()
        return o

    def vocalu(self):
        u=0
        archivo=open(self.direccion,"r",encoding="utf-8")
        while archivo:
                char=archivo.read(1)
                if char.lower()=="u":
                    u=u+1
                else:
                    if not char:
                        break
        archivo.close()
        return u



class Vocal2(Process):
    def __init__(self,direccion,voca):
        Process.__init__(self)
        self.direccion=direccion
        self.voca=voca

    def run(self):
        print("El numero de vocales " + self.voca + " es:" + str(self.contarvocal()))

    def contarvocal(self):
        vocal=0
        archivo=open(self.direccion, "r", encoding='utf-8')
        while archivo:
                char=archivo.read(1)
                if char.lower()==self.voca:
                    vocal=vocal+1
                else:
                    if not char:
                        break
        archivo.close()
        return vocal

if __name__ == "__main__":
    direccionarchivo=input("Diga ruta")
    if os.path.exists(direccionarchivo):
        if os.path.isfile(direccionarchivo):
            inicioEjecucionS = time.perf_counter()
            vocaluno=Vocal1(direccionarchivo)
            print("a= "+str(vocaluno.vocala()))
            print("e= " + str(vocaluno.vocale()))
            print("i= " + str(vocaluno.vocali()))
            print("o= " + str(vocaluno.vocalo()))
            print("u= " + str(vocaluno.vocalu()))

            finalEjecucionS = time.perf_counter() - inicioEjecucionS
            print("Tiempo de ejection vocal1 es:" + str(round(finalEjecucionS, 2)))
        inicioEjecucion = time.perf_counter()
        vocala = Vocal2(direccionarchivo,"a")
        vocale = Vocal2(direccionarchivo,"e")
        vocali = Vocal2(direccionarchivo,"i")
        vocalo = Vocal2(direccionarchivo,"o")
        vocalu = Vocal2(direccionarchivo,"u")
        vocala.start()
        vocale.start()
        vocali.start()
        vocalo.start()
        vocalu.start()
        vocala.join()
        vocale.join()
        vocali.join()
        vocalo.join()
        vocalu.join()
        finalEjecucion = time.perf_counter() - inicioEjecucion
        print("El tiempo de ejecucion del proceso contar vocales en paralelo es:" + str(round(finalEjecucion, 2)))
    else:
        print("No es archivo")

#Se observa que el primer programa es más rápido en contar las vocales además de que no satura el procesador,
#mientras que el de los procesos tarda más tiempo en contar las vocales y además podemos comprobar que mientras
#dura la creacion de los subprocesos el procesador está saturado y una vez finalizan(los subprocesos) el procesador deja de estar saturado y vuelve a su estado habitual