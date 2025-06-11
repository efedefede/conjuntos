from typing import Dict, List, Set

# --- FUNCIONES PARA DNIs ---
def ingresar_dnis() -> Dict[str, List[int]]:
    """Ingresa DNIs y los devuelve como diccionario de listas de dígitos."""
    dnis = {}
    contador = 1
    print('\n--- Ingreso de DNIs ---')
    while True:
        dni = input('Ingrese DNI (8 dígitos) o "fin" para terminar: ')
        if dni.lower() == 'fin':
            break
        if len(dni) == 8 and dni.isdigit():
            dnis[f'DNI_{contador}'] = [int(d) for d in dni]
            contador += 1
        else:
            print('¡DNI inválido! Debe tener 8 dígitos.')
    return dnis


# --- OPERACIONES DE CONJUNTOS ---#

def union(conjunto1:set,conjunto2:set) -> set:
    """
    Esta función recibe 2 conjuntos y devuelve la unión
    de los mismos.
    """
    return conjunto1.union(conjunto2)


def interseccion(conjunto1:set,conjunto2:set) -> set:
    """
    Esta función recibe 2 conjuntos y devuelve la intersección
    de los mismos.
    """
    return conjunto1.intersection(conjunto2)


def diferencia(conjunto1:set,conjunto2:set) -> set:
    """
    Esta función recibe 2 conjuntos y devuelve la diferencia del conjunto 1
    menos el conjunto 2.
    """
    return conjunto1.difference(conjunto2)

def diferencia_simetrica(conjunto1:set,conjunto2:set)-> set:
    """
    Esta función recibe 2 conjuntos y devuelve la diferencia
    simétrica de los mismos.
    """
    return conjunto1.symmetric_difference(conjunto2)

def generar_conjuntos(dnis: Dict[str, List[int]]) -> List[Set[int]]:
    """Convierte los DNIs a conjuntos de dígitos únicos."""
    return [set(dni) for dni in dnis.values()]


# --- OPERACIONES DE DNI ---#

def mostrar_operaciones_dnis():
    """Menú de operaciones disponibles para DNIs."""
    print('\nOperaciones disponibles:')
    print('1. Mostrar unión de todos los DNIs')
    print('2. Mostrar intersección de dígitos comunes')
    print('3. Calcular frecuencia de dígitos')
    print('4. Verificar diversidad numérica')
    print('5. Volver al menú principal')

def operar_dnis(dnis: Dict[str, List[int]], conjuntos: List[Set[int]]):
    """Ejecuta operaciones seleccionadas sobre DNIs."""
    while True:
        mostrar_operaciones_dnis()
        opcion = input('Seleccione una operación (1-5): ')
        
        if opcion == '1':
            #LLAMAR A LA FUNCIÓN DE UNION
            print('union')
        elif opcion == '2':
            #LLAMAR A LA FUNCIÓN DE INTERSECCIÓN
            print('intersección')
        
        elif opcion == '3':
            #LLAMAR A LA FUNCIÓN DE FRECUENCIA DE DÍGITOS
            print('Frecuencia de dígitos')
            
        
        elif opcion == '4':
            #LLAMAR A LA FUNCIÓN DE DIVERSIDAD NUMÉRICA
            print('Verificar diversidad numérica')
        
        elif opcion == '5':
            break
        
        else:
            print('Opción inválida. Intente nuevamente.')

# --- FUNCIONES PARA AÑOS ---
def ingresar_anios() -> List[int]:
    """Ingresa años de nacimiento válidos."""
    anios = []
    print('\n--- Ingreso de Años de Nacimiento ---')
    while True:
        anio = input('Ingrese año (1900-2023) o "fin": ')
        if anio.lower() == 'fin':
            break
        if anio.isdigit() and 1900 <= int(anio) <= 2023:
            anios.append(int(anio))
        else:
            print('¡Año inválido! Debe ser entre 1900-2023.')
    return anios

def mostrar_operaciones_anios():
    """Menú de operaciones disponibles para años."""
    print('\nOperaciones disponibles:')
    print('1. Contar años pares/impares')
    print('2. Verificar si son "Grupo Z" (nacidos después del 2000)')
    print('3. Identificar años bisiestos')
    print('4. Volver al menú principal')

def operar_anios(anios: List[int]):
    """Ejecuta operaciones seleccionadas sobre años."""
    while True:
        mostrar_operaciones_anios()
        opcion = input('Seleccione una operación (1-4): ')
        
        if opcion == '1':
            print('----------Operacion 1----------')
            
            Contar_años_par_impar(anios)
            print('-------------------------------')
        
        elif opcion == '2':
            print('----------Operacion 2----------')
            
            verificar_grupoz(anios)
            print('-------------------------------')
        
        elif opcion == '3':
            print('----------Operacion 3----------')
            for anio in anios:
                es_especial(anio)
            print('-------------------------------')
        
        elif opcion == '4':
            break
        
        else:
            print('Opción inválida. Intente nuevamente.')

# FUNCION PARA CONTAR AÑOS PARES O IMPARES

def Contar_años_par_impar(lista):
    años_par = 0
    años_impar = 0
    for a in lista:
        if a % 2 == 0:
            años_par += 1
        else:
            años_impar += 1
    print(f"{años_par} personas nacieron en años pares")
    print(f"{años_impar} personas nacieron en años impares")

        
# FUNCION GRUPO Z (NACIMIENTO 2000+)
def verificar_grupoz(lista):
    años_1900 = 0
    for a in lista:
        if a < 2000:
            años_1900 +=1
    if años_1900 == 0:
        print(f"Este es un grupo Z, todos nacieron despues del año 2000")
    else:
        print(f"Este no es un grupo Z, al menos uno nacio antes del 2000")

# FUNCION PARA DECIR SI NACIO EN AÑO BISIESTO
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# FUNCION NACIO EN AÑO ESPECIAL
def es_especial(anio):
    if (es_bisiesto(anio)):
        print("Tenemos un año especial")


# --- FUNCIÓN PRINCIPAL ---
def main():
    """Controla el flujo principal del programa."""
    print('=== PROGRAMA DE ANÁLISIS DE DATOS ===')
    
    while True:
        print('\nMenú Principal:')
        print('1. Operar con DNIs')
        print('2. Operar con años de nacimiento')
        print('3. Salir')
        
        opcion_principal = input('Seleccione una opción (1-3): ')
        
        if opcion_principal == '1':
            dnis = ingresar_dnis()
            if not dnis:
                print('No se ingresaron DNIs.')
                continue
            conjuntos = generar_conjuntos(dnis)
            operar_dnis(dnis, conjuntos)
        
        elif opcion_principal == '2':
            anios = ingresar_anios()
            if not anios:
                print('No se ingresaron años.')
                continue
            operar_anios(anios)
        
        elif opcion_principal == '3':
            print('¡Hasta luego!')
            break
        
        else:
            print('Opción inválida. Intente nuevamente.')

# PRUEBA:
main()

