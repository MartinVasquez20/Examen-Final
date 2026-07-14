peliculas = {
    }
cartelera = {
    }
def leer_opcion():
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    return opcion

def cupos_genero(genero, peliculas, cartelera):
    genero_buscado = genero.strip().lower()
    total_cupos = 0
    for codigo in peliculas:
        genero_pelicula = peliculas[codigo][1]
        if genero_pelicula.lower() == genero_buscado:
            cupos = cartelera[codigo][1]
            total_cupos = total_cupos + cupos
    print("El total de cupos disponibles es:", total_cupos)

def busqueda_precio(p_min, p_max, cartelera, peliculas):
    resultados = []
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(titulo + "--" + codigo)
    resultados.sort()
    if len(resultados) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print("Las películas encontradas son:", resultados)

def buscar_codigo(codigo, diccionario):
    codigo_normalizado = codigo.strip().upper()
    for clave in diccionario:
        if clave.upper() == codigo_normalizado:
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, cartelera):
    codigo_normalizado = codigo.strip().upper()
    if buscar_codigo(codigo_normalizado, cartelera):
        cartelera[codigo_normalizado][0] = nuevo_precio
        return True
    else:
        return False

def validar_codigo(codigo):
    return codigo.strip() != ""
def validar_titulo(titulo):
    return titulo.strip() != ""
def validar_genero(genero):
    return genero.strip() != ""
def validar_duracion(duracion):
    try:
        valor = int(duracion)
        return valor > 0
    except ValueError:
        return False
def validar_clasificacion(clasificacion):
    return clasificacion.strip() in ("A", "B", "C")
def validar_idioma(idioma): 
    return idioma.strip() != ""
def validar_es_3d(es_3d):
    return es_3d.strip().lower() in ("s", "n")
def validar_precio(precio):
    try:
        valor = int(precio)
        return valor > 0
    except ValueError:
        return False
def validar_cupos(cupos):
    try:
        valor = int(cupos)
        return valor >= 0
    except ValueError:
        return False

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma,
                      es_3d, precio, cupos, peliculas, cartelera):
    codigo_normalizado = codigo.strip().upper()
    if buscar_codigo(codigo_normalizado, peliculas):
        return False
    peliculas[codigo_normalizado] = [
        titulo.strip(), genero.strip(), duracion,
        clasificacion.strip(), idioma.strip(), es_3d,
    ]
    cartelera[codigo_normalizado] = [precio, cupos]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    codigo_normalizado = codigo.strip().upper()
    if buscar_codigo(codigo_normalizado, peliculas):
        del peliculas[codigo_normalizado]
        del cartelera[codigo_normalizado]
        return True
    else:
        return False


def menu():
    opc = 0
    while opc != 6:
        print("========== MENÚ PRINCIPAL ==========\n1. Cupos por género\n2. Búsqueda de películas por rango de precio\n3. Actualizar precio de película\n4. Agregar película\n5. Eliminar película\n6. Salir\n=====================================")
        opc = leer_opcion()

        if opc == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero, peliculas, cartelera)

        elif opc == 2:
            valores_validos = False
            while not valores_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    valores_validos = True
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, cartelera, peliculas)

        elif opc == 3:
            continuar = "s"
            while continuar == "s":
                codigo = input("Ingrese código de película: ")

                precio_valido = False
                while not precio_valido:
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                        if nuevo_precio > 0:
                            precio_valido = True
                        else:
                            print("El precio debe ser un entero positivo")
                    except ValueError:
                        print("El precio debe ser un entero positivo")

                actualizado = actualizar_precio(codigo, nuevo_precio, cartelera)
                if actualizado:
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                continuar = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()

        elif opc == 4:
            codigo = input("Ingrese código de película: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")
            duracion = input("Ingrese duración (minutos): ")
            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d = input("¿Es 3D? (s/n): ")
            precio = input("Ingrese precio: ")
            cupos = input("Ingrese cupos: ")

            if not validar_codigo(codigo):
                print("El código no puede estar vacío")
            elif not validar_titulo(titulo):
                print("El título no puede estar vacío")
            elif not validar_genero(genero):
                print("El género no puede estar vacío")
            elif not validar_duracion(duracion):
                print("La duración debe ser un número entero mayor que cero")
            elif not validar_clasificacion(clasificacion):
                print("La clasificación debe ser 'A', 'B' o 'C'")
            elif not validar_idioma(idioma):
                print("El idioma no puede estar vacío")
            elif not validar_es_3d(es_3d):
                print("Debe ingresar 's' o 'n'")
            elif not validar_precio(precio):
                print("El precio debe ser un número entero mayor que cero")
            elif not validar_cupos(cupos):
                print("Los cupos deben ser un número entero mayor o igual a cero")
            else:
                es_3d_bool = (es_3d.strip().lower() == "s")
                agregada = agregar_pelicula(
                    codigo, titulo, genero, int(duracion), clasificacion,
                    idioma, es_3d_bool, int(precio), int(cupos),
                    peliculas, cartelera,
                )
                if agregada:
                    print("Película agregada")
                else:
                    print("El código ya existe")

        elif opc == 5:
            codigo = input("Ingrese código de película: ")
            eliminada = eliminar_pelicula(codigo, peliculas, cartelera)
            if eliminada:
                print("Película eliminada")
            else:
                print("El código no existe")

        elif opc == 6:
            print("Programa finalizado.")

menu()