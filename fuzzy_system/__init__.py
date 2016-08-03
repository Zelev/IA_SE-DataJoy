# el nombre "__init__.py" me permite importar desde otros scripts de python tomando a
# la carpeta como si fuera un paquete

__all__ = ["generar_hora", "generar_actividad",
           "generar_clase", "generar_calorico",
           "rule_hora", "rule_actividad"]
           
from generar_fm import (generar_hora, generar_actividad, 
                        generar_clase, generar_calorico,
                        rule_hora, rule_actividad)