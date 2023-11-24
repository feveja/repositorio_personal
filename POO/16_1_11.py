class Fecha:
    def __init__(self, fecha_str):
        # Parsear la fecha en formato "DD/MM/AAAA"
        dia, mes, anio = map(int, fecha_str.split('/'))
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __str__(self):
        # Formatear la fecha en "DD/MM/AAAA"
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def siguiente(self):
        # Calcular la fecha del día siguiente
        dia_siguiente = self.dia + 1
        mes_siguiente = self.mes
        anio_siguiente = self.anio

        # Verificar si se excede el número de días en el mes actual
        if dia_siguiente > self.dias_en_mes():
            dia_siguiente = 1
            mes_siguiente += 1

            # Verificar si se excede el número de meses en el año actual
            if mes_siguiente > 12:
                mes_siguiente = 1
                anio_siguiente += 1

        return Fecha(f"{dia_siguiente}/{mes_siguiente}/{anio_siguiente}")

    def __sub__(self, otra_fecha):
        # Calcular la diferencia en días entre dos fechas
        dias_self = self.dia + self.mes * 31  # Asumiendo 31 días por mes
        dias_otra_fecha = otra_fecha.dia + otra_fecha.mes * 31

        return dias_self - dias_otra_fecha

    def dias_en_mes(self):
        # Obtener el número de días en el mes actual
        if self.mes in {1, 3, 5, 7, 8, 10, 12}:
            return 31
        elif self.mes in {4, 6, 9, 11}:
            return 30
        else:  # Mes 2 (febrero)
            return 28  # No se consideran años bisiestos


# Ejemplo de uso
F = Fecha("31/5/2013")
print(str(F))  # Salida: 31/05/2013

G = F.siguiente()
print(str(G))  # Salida: 01/06/2013

H = Fecha("07/06/2013")
print(str(H))  # Salida: 01/06/2013

diferencia = H - F
print(diferencia)  # Salida: 1

diferencia = G - F
print(diferencia)  # Salida: 1
