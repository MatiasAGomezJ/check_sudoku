def checkSudoku(sudoku):

    assert isinstance(sudoku, list), "el sudoku tiene que ser una lista"

    from check_cuadrado         import check_cuadrado
    from check_numeros_en_rango import check_numeros_en_rango
    from check_filas            import check_filas
    from check_columnas         import check_columnas
    
    
    sudokuSano = check_cuadrado(sudoku) and check_numeros_en_rango(sudoku) and check_filas(sudoku) and check_columnas(sudoku)

    assert isinstance(sudokuSano, bool), "comprobamos que la variable sea un booleano"

    return sudokuSano


if __name__ == '__main__':
  
    import casos_test_sudoku

    assert checkSudoku(casos_test_sudoku.correct)    == True
    assert checkSudoku(casos_test_sudoku.incorrect)  == False
    assert checkSudoku(casos_test_sudoku.incorrect2) == False
    assert checkSudoku(casos_test_sudoku.incorrect3) == False
    assert checkSudoku(casos_test_sudoku.incorrect4) == False
    assert checkSudoku(casos_test_sudoku.incorrect5) == False
    assert checkSudoku(casos_test_sudoku.irregular)  == False
    assert checkSudoku(casos_test_sudoku.irregular2) == False
