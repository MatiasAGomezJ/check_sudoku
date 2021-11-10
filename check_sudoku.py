def checkSudoku(sudoku):

    assert isinstance(sudoku, list)

    from check_columnas         import check_columnas
    from check_cuadrado         import check_cuadrado
    from check_filas            import check_filas
    from check_numeros_en_rango import check_numeros_en_rango
    
    sudokuSano = check_columnas(sudoku) and check_cuadrado(sudoku) and check_filas(sudoku) and check_numeros_en_rango(sudoku)

    assert isinstance(sudokuSano, bool)
    return sudokuSano


if __name__ == '__main__':
  
    import casos_test_sudoku

    for attr in sorted(casos_test_sudoku.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr)
            print(attr, " => ", checkSudoku(casos_test_sudoku.__dict__[attr]))
