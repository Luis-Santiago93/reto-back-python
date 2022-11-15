import functools

class MatematicoRepository():
    def __init__(self, app):
        super(MatematicoRepository, self).__init__()

    def get_minimo_multiplo(self,numbers_list):
        try:
            numbers=[]
            for x in numbers_list:
                r=x.split(',')
                for i in r:
                    numbers.append(int(i))
                    
            lista_numeros = [int(i) for i in numbers]
            numeros_prueba = [1]*len(lista_numeros)
            segui_numero = lista_numeros
            bucle = lista_numeros == numeros_prueba
            mcmList = list()
            principal = [2, 3, 5, 7, 11, 13, 17, 19]
            count = 0

            while(not bucle):
                lista_numeros = [i/principal[count] if i%principal[count] == 0 else i for i in lista_numeros]
                if lista_numeros == segui_numero:
                    count += 1
                else:
                    mcmList.append(principal[count])
                if lista_numeros == numeros_prueba:
                    bucle = False
                    break
                segui_numero = lista_numeros
                if count >= len(principal):
                    break
            resultado={
                'minimo_comun_multipo':functools.reduce(lambda a, b: a*b, mcmList)
            }
            return resultado
        except Exception as e:
            print(e)
            return None
    
    def sum(self,number):
        try:
            sumatoria=int(number)+1
            resultado={
                'suma':sumatoria
            }
            return resultado
        except Exception as e:
            print(e)
            return None
