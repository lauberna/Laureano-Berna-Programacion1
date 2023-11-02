def is_mutant(dna):
    row = len(dna)
    column = len(dna[0])
    secuence_counter = 0

    # Busca cualquier secuencia vertical en cualquier lado
    for j in range(column):
        actual_counter = 1
        for i in range(1, row):
            if dna[i][j] == dna[i - 1][j]:
              #voy guardando la cantidad de veces que se encuentra la misma letra, y cuando llega a 4 se suma 1 al contador de secuencias, caso contrario el contador actual vuelve a 1 para volver a empezar, igual para todas las demas
                actual_counter += 1
                if actual_counter == 4:
                    secuence_counter += 1
                    break
            else:
                actual_counter = 1

    # Busca cualquier secuencia horizontal en cualquier lado
    for s in dna:
        actual_counter = 1
        for i in range(1, column):
            if s[i] == s[i - 1]:
                actual_counter += 1
                if actual_counter == 4:
                    secuence_counter += 1
                    break
            else:
                actual_counter = 1

    # Busca en la diagonal PRINCIPAL
    actual_counter = 1
    for j in range(1, row):
        if dna[j][j] == dna[j - 1][j - 1]:
            actual_counter += 1
            if actual_counter == 4:
                secuence_counter += 1
                break
        else:
            actual_counter = 1

    # Busca en la diagonal SECUNDARIA
    actual_counter = 1
    for j in range(1, row):
        if dna[j][len(dna[j]) - (1 + j)] == dna[j - 1][len(dna[j]) - j]:
            actual_counter += 1
            if actual_counter == 4:
                secuence_counter += 1
                break
        else:
            actual_counter = 1

    print("Cantidad de secuencias encontradas:", secuence_counter)
    return secuence_counter >= 2