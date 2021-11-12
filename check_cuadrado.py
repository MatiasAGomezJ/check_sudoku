### Comprueba que la cantidad de numeros horizontales sea igual a los verticales
def check_cuadrado(sudoku):
    
    assert isinstance(sudoku, list), "el sudoku tiene que ser una lista"

    lenY = len(sudoku)

    i = 0
    while i < lenY:             # Por cada sublista que hay dentro del sudoku...
        lenX = len(sudoku[i])   # ... comprobamos que el largo de esa sublista ...
        if lenX != lenY:        # ... sea igual a la cantidad de sublistas que hay, es decir, el eje Y
            return False
        i += 1

    return True

if __name__ == '__main__':
    
    import casos_test_sudoku

    assert check_cuadrado(casos_test_sudoku.correct) == True
    assert check_cuadrado(casos_test_sudoku.incorrect) == True
    assert check_cuadrado(casos_test_sudoku.incorrect2) == True
    assert check_cuadrado(casos_test_sudoku.incorrect3) == False
    assert check_cuadrado(casos_test_sudoku.incorrect4) == True
    assert check_cuadrado(casos_test_sudoku.incorrect5) == True
    assert check_cuadrado(casos_test_sudoku.irregular) == False
    assert check_cuadrado(casos_test_sudoku.irregular2) == False