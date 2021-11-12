### Comprueba que en cada una de las filas del sudoku no se repitan los numeros
def check_filas(sudoku):
    
    assert isinstance(sudoku, list), "el sudoku tiene que ser una lista"

    for sublista in sudoku:
        
        for (posicion, numero) in enumerate(sublista):

            if numero in sublista[posicion + 1: ]:
                return False

    return True

if __name__ == '__main__':

    import casos_test_sudoku

    assert check_filas(casos_test_sudoku.correct) == True
    assert check_filas(casos_test_sudoku.incorrect) == False
    assert check_filas(casos_test_sudoku.incorrect2) == False
    assert check_filas(casos_test_sudoku.incorrect3) == True

    # assert check_filas(casos_test_sudoku.incorrect4) == False
    # assert check_filas(casos_test_sudoku.incorrect5) == False
    # assert check_cuadrado(casos_test_sudoku.irregular) == False
    # assert check_cuadrado(casos_test_sudoku.irregular2) == False