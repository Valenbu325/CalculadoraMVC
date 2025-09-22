class CalculadoraView:
    def pedir_datos(self):
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        return a, b
    
    def pedir_operacion(self):
        return input("Operacion (+, -, *, /): ")
    
    def mostrar_resultados(self, resultado):
        print (f"Resultado:  {resultado}")

    def mostrar_error(self, mensaje):
        print(f"Error {mensaje}")