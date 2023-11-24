class Fecha:
    def __init__(self, fechaStr):
        dia, mes, anio = fechaStr.split("/")
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"


    def siguiente(self):
        #inicializar d, m y a:
        d = self.dia; m = self.mes; a = self.anio

        #caso 1: cambio de dia dentro del mes: 0.6
        diasMes=[31,28,31,30,31,30,31,31,30,31,30,31]
        if d<diasMes[m-1]:
            d=d+1
        #caso 2: cambio de mes: 0.5
        else:           #0.1
            d=1         #0.1
            if m<12:    #0.2
                m = m+1   #0.1
            #caso 3: cambio de anio:
            else:
                m = 1
                a = a + 1

        #devolver fecha de siguiente dia:
        return Fecha(str(d)+"/"+str(m)+"/"+str(a))


    def __sub__(self, otra_fecha):
        # Calcular la diferencia en días entre dos fechas
        dias_self = self.dia + self.mes * 31  # Asumiendo 31 días por mes
        dias_otra_fecha = otra_fecha.dia + otra_fecha.mes * 31

        return dias_self - dias_otra_fecha


F = Fecha("17/11/2023")
print(str(F))

G = Fecha("9/2/2023")
print(str(G))

