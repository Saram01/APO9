from meteorologicos import DatosMeteorologicos

def main():
    nombre_archivo = "datos_meteorologicos.txt"
    datos = DatosMeteorologicos(nombre_archivo)
    resultados = datos.procesar_datos()

    print(f"Temperatura promedio: {resultados[0]:.2f}°C")
    print(f"Humedad promedio: {resultados[1]:.2f}%")
    print(f"Presion promedio: {resultados[2]:.2f} hPa")
    print(f"Velocidad del viento promedio: {resultados[3]:.2f} m/s")
    print(f"Direccion del viento predominante: {resultados[4]}")

if __name__ == "__main__":
    main()