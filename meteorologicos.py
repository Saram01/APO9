from typing import Tuple
import math

direcciones_viento = {
    "N": 0, "NNE": 22.5, "NE": 45, "ENE": 67.5,
    "E": 90, "ESE": 112.5, "SE": 135, "SSE": 157.5,
    "S": 180, "SSW": 202.5, "SW": 225, "WSW": 247.5,
    "W": 270, "WNW": 292.5, "NW": 315, "NNW": 337.5
}

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento_grados = []

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                partes = linea.split()
                temperatura = float(partes[10].strip(','))
                humedad = float(partes[12].strip(','))
                presion = float(partes[14].strip(','))
                viento = partes[16].split(',')
                velocidad_viento = float(viento[0])
                direccion_viento = viento[1].strip()
                grados_viento = direcciones_viento[direccion_viento]
                temperaturas.append(temperatura)
                humedades.append(humedad)
                presiones.append(presion)
                velocidades_viento.append(velocidad_viento)
                direcciones_viento_grados.append(grados_viento)

        temp_promedio = sum(temperaturas) / len(temperaturas)
        humed_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        vel_viento_promedio = sum(velocidades_viento) / len(velocidades_viento)
        x = sum(math.cos(math.radians(grados)) for grados in direcciones_viento_grados)
        y = sum(math.sin(math.radians(grados)) for grados in direcciones_viento_grados)
        promedio_direccion = math.degrees(math.atan2(y, x))
        if promedio_direccion < 0:
            promedio_direccion += 360
        direccion_predominante = min(direcciones_viento.keys(),
                                     key=lambda d: abs(direcciones_viento[d] - promedio_direccion))

        return temp_promedio, humed_promedio, presion_promedio, vel_viento_promedio, direccion_predominante
