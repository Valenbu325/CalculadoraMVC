from model import Suma, Resta, Multiplicacion, Division
from view import CalculadoraView 

class CalculadoraController:
    def __init__(self):
         self.view = CalculadoraView() 
         self.operaciones = {
            "+": Suma(),
            "-": Resta(),
            "*": Multiplicacion(),
            "/": Division()
        }

    def ejecutar(self):
        try:
            a, b = self.view.pedir_datos()
            op = self.view.pedir_operacion()
            if op not in self.operaciones:
                self.view.mostrar_error("Operación inválida")
                return
            resultado = self.operaciones[op].ejecutar(a, b)
            self.view.mostrar_resultado(resultado)
        except Exception as e:
            self.view.mostrar_error(str(e))