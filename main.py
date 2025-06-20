from typing import Dict, List, Set

# --- FUNCIONES PARA DNIs ---
def ingresar_dnis() -> Dict[str, Set[int]]:
    """Ingresa DNIs y los devuelve como diccionario de listas de dígitos."""
    dnis = {}
    contador = 1
    print('\n--- Ingreso de DNIs ---')
    while True:
        dni = input('Ingrese DNI (8 dígitos) o "fin" para terminar: ')
        if dni.lower() == 'fin':
            break
        if len(dni) == 8 and dni.isdigit():
            dnis[f'DNI_{contador}'] = {int(d) for d in dni}
            contador += 1
        else:
            print('¡DNI inválido! Debe tener 8 dígitos.')
    return dnis

def mostrar_conjuntos_dni(dnis:Set):
    """
    Muestra de forma prolija los conjuntos de DNI
    """
    for clave,valor in dnis.items():
        print(f"{clave}= {valor}")



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


# --- OPERACIONES DE DNI ---#

def mostrar_operaciones_dnis():
    """Menú de operaciones disponibles para DNIs."""
    print('\nOperaciones disponibles:')
    print('1. Unión de 2 conjuntos de DNIs')
    print('2. Intersección de 2 conjuntos de DNIs')
    print('3. Diferencia de 2 conjuntos de DNIss')
    print('4. Diferencia simétrica de 2 conjuntos de DNIs')
    print('5. Calcular frecuencia de dígitos')
    print('6. Verificar diversidad numérica')
    print('7. Volver al menú principal')

def operar_dnis(dnis: Dict[str, List[int]]):
    """Ejecuta operaciones seleccionadas sobre DNIs."""
    while True:
        mostrar_operaciones_dnis()
        mostrar_conjuntos_dni(dnis)
        opcion = input('Seleccione una operación (1-7): ')
        
        if opcion in {'1', '2', '3', '4'}:
            print("Elija 2 claves válidas del listado para realizar la operación:")
            mostrar_conjuntos_dni(dnis)

            clave1 = input("Ingrese el nombre del primer conjunto (ej: DNI_1): ").strip()
            clave2 = input("Ingrese el nombre del segundo conjunto (ej: DNI_2): ").strip()

            if clave1 in dnis and clave2 in dnis:
                conjunto1 = set(dnis[clave1])
                conjunto2 = set(dnis[clave2])
                print("RESULTADO:")

            if opcion == '1':
                #LLAMAR A LA FUNCIÓN DE UNION
                print(f"Union de {conjunto1} y {conjunto2} = {union(conjunto1,conjunto2)}")
            elif opcion == '2':
                #LLAMAR A LA FUNCIÓN DE INTERSECCIÓN
                print(f"Intersección de {conjunto1} y {conjunto2} = {interseccion(conjunto1,conjunto2)}")

            elif opcion == '3':
                #LLAMAR A LA FUNCIÓN DE DIFERENCIA
                print(f"Diferencia de {conjunto1} y {conjunto2} = {diferencia(conjunto1,conjunto2)}")

            elif opcion == '4':
                #LLAMAR A LA FUNCIÓN DE DIFERENCIA SIMETRICA
                print(f"Diferencia simétrica de {conjunto1} y {conjunto2} = {diferencia_simetrica(conjunto1,conjunto2)}")
        elif opcion == '5':
            #LLAMAR A LA FUNCIÓN DE FRECUENCIA DE DÍGITOS
                frecuencia_digitos(dnis)
                suma_digitos_dni(dnis)           
        elif opcion == '6':
            #LLAMAR A LA FUNCIÓN DE DIVERSIDAD NUMÉRICA
            evaluar_condiciones(dnis)        

        elif opcion == '7':
            break
        
        else:
            print('Opción inválida. Intente nuevamente.')

# CONTEO DE FRECUENCIA DE CADA DIGITO #

def frecuencia_digitos(dnis: Dict[str, List[int]]):
    """Cuenta la frecuencia de cada dígito en todos los DNIs."""
    frecuencia = {i: 0 for i in range(10)}
    for lista_digitos in dnis.values():
        for digito in lista_digitos:
            frecuencia[digito] += 1

    print('\nFrecuencia de dígitos en todos los DNIs:')
    for digito, cantidad in frecuencia.items():
        print(f'Dígito {digito}: {cantidad} veces')

# SUMA TOTAL DE LOS DIGITOS DE CADA DNI #

def suma_digitos_dni(dnis: Dict[str, List[int]]):
    """Calcula la suma de los dígitos de cada DNI."""
    print('\nSuma de dígitos por DNI:')
    for clave, lista_digitos in dnis.items():
        suma = sum(lista_digitos)
        print(f'{clave}: suma = {suma}')

# EVALUACIÓN DE CONDICIONES LÓGICAS # 

def evaluar_condiciones(conjuntos: Dict[str, Set[int]] ):
    """Evalúa condiciones lógicas sobre los conjuntos de dígitos."""
    if not conjuntos:
        return
    # Convertir los valores (los conjuntos) en una lista
    conjuntos_lista = list(conjuntos.values())


    # Comprobar si hay dígitos que aparecen en todos los DNIs
    interseccion_total = conjuntos_lista[0].copy()
    for conjunto in conjuntos_lista[1:]:
        interseccion_total = interseccion_total.intersection(conjunto)
    
    if interseccion_total:
        print(f'\nDígitos compartidos por todos los DNIs: {interseccion_total}')
    else:
        print('\nNo hay dígitos compartidos por todos los DNIs.')



    # Condición 2: Diversidad numérica alta (> 6 dígitos únicos)
    for i, (clave, conjunto) in enumerate(conjuntos.items(), 1):
        if len(conjunto) > 6:
            print(f"DNI_{i} tiene diversidad numérica alta (dígitos únicos: {len(conjunto)}/8)")

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
            operar_dnis(dnis)
        
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

