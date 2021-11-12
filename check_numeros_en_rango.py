### Comprueba que cada numero del sudoku no sea mayor a su tañamo, empezando por 1
def check_numeros_en_rango(sudoku):

    assert isinstance(sudoku, list), "el sudoku tiene que ser una lista"

    numeros_posibles = range(1, len(sudoku) + 1)

    for sublista in sudoku:

        for elemento in sublista:

            if not isinstance(elemento, int) or elemento not in numeros_posibles:
                return False

    return True
            

if __name__ == '__main__':

    import casos_test_sudoku

    assert check_numeros_en_rango("1, 2, 3") == True
    assert check_numeros_en_rango(casos_test_sudoku.correct) == True
    assert check_numeros_en_rango(casos_test_sudoku.incorrect) == True
    assert check_numeros_en_rango(casos_test_sudoku.incorrect2) == True
    assert check_numeros_en_rango(casos_test_sudoku.incorrect3) == False
    assert check_numeros_en_rango(casos_test_sudoku.incorrect4) == False
    assert check_numeros_en_rango(casos_test_sudoku.incorrect5) == False
    
    # assert check_cuadrado(casos_test_sudoku.irregular) == False
    # assert check_cuadrado(casos_test_sudoku.irregular2) == False