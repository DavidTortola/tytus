from Instrucciones.Expresiones.Primitivo import Primitivo
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion

class Abs(Instruccion):
    def __init__(self, valor, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if isinstance(resultado, Excepcion):
            return resultado
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función abs("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            self.tipo = Tipo(Tipo_Dato.INTEGER)
            return int(abs(resultado))
        else:
            self.tipo = Tipo(Tipo_Dato.NUMERIC)
            return abs(resultado)
    
    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        
        if isinstance(self.valor, Primitivo):
            return f"ABS({self.valor.traducir(tabla,arbol).temporalAnterior})"

        return f"ABS({self.valor.concatenar(tabla,arbol)})"