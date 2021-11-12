### Comprueba que en cada una de las columnas del sudoku no se repitan los numeros
def check_columnas(sudoku):

    assert isinstance(sudoku, list), "el sudoku tiene que ser una lista"

    largo = range(len(sudoku))

    for i in largo:

        columna_i = [fila[i] for fila in sudoku]

        for (posicion, numero) in enumerate(columna_i):

            if numero in columna_i[posicion + 1: ]:
                return False

    return True

if __name__ == '__main__':

    import casos_test_sudoku

    assert check_columnas(casos_test_sudoku.correct) == True
    assert check_columnas(casos_test_sudoku.incorrect) == False
    assert check_columnas(casos_test_sudoku.incorrect2) == False
    assert check_columnas(casos_test_sudoku.incorrect3) == True

    # assert check_filas(casos_test_sudoku.incorrect4) == False
    # assert check_filas(casos_test_sudoku.incorrect5) == False
    # assert check_cuadrado(casos_test_sudoku.irregular) == False
    # assert check_cuadrado(casos_test_sudoku.irregular2) == False