# Calculadora con Tkinter

Una calculadora simple con interfaz gráfica implementada en Python usando Tkinter, que incluye modo oscuro/claro.

## Características

- Operaciones básicas (suma, resta, multiplicación, división)
- Operaciones avanzadas (potencia, raíz cuadrada, porcentaje)
- Interfaz gráfica responsive
- Cambio entre modo oscuro y claro
- Manejo de errores robusto
- Botón de limpieza (Clear)
- Historial de operaciones
- Teclas de acceso rápido
- Memoria (M+, M-, MR, MC)

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

## Instalación

1. Clone o descargue este repositorio
2. Asegúrese de tener Python instalado
3. Ejecute el archivo `prueba.py`

```bash
python prueba.py
```

## Uso

- Use los botones numéricos (0-9) para ingresar números
- Use los botones de operadores (+, -, *, /, ^, √, %) para realizar operaciones
- Presione '=' para calcular el resultado
- Presione 'C' para limpiar la pantalla
- Use el botón 'Modo Claro/Oscuro' para cambiar el tema
- Utilice las teclas de memoria:
  - M+ para añadir a memoria
  - M- para restar de memoria
  - MR para recuperar valor de memoria
  - MC para limpiar memoria
- Accesos rápidos:
  - ESC: Limpiar
  - Enter: Calcular
  - Delete: Borrar último dígito

## Estructura del Proyecto

```
├── prueba.py      # Archivo principal de la calculadora
└── README.md      # Documentación del proyecto
```

## Funcionalidades Avanzadas

### Memoria
La calculadora incluye funciones de memoria que permiten almacenar y recuperar resultados para cálculos posteriores.

### Historial
Mantiene un registro de las últimas operaciones realizadas, accesible mediante el panel lateral.

### Manejo de Errores
- División por cero
- Raíz cuadrada de números negativos
- Desbordamiento numérico
- Entradas inválidas

## Capturas de Pantalla

![Modo Claro](screenshots/light-mode.png)
![Modo Oscuro](screenshots/dark-mode.png)

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.