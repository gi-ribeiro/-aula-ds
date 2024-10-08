assentos = [[0 for _ in range(8)] for _ in range(5)]

def reservar_assentos(assentos, fileira, assento):
    """Reserva um assento na matriz de assentos. """
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assento[0]): 
        if assentos[fileira][assento] == 0:
            assentos[fileira][assento] = 1
            print(f"Assento ({fileira + 1}, {assento + 1}) reservado com sucesso.")
        else: 
            print(f"Assento ({fileira + 1}) já está reservado. ")
    else: 
        print("Assento inválido")

def cancelar_reserva(assentos, fileira, assento):
    if 0 <= fileira < len(assentos) and 0 <= assento < len(assentos[0]):
        if assento[fileira][assento] == 1:
            assento[fileira][assento] = 0
            print(f"reserva do assento ({fileira + 1}, {assento + 1}) cancelada com sucesso")
        else: 
            print(f"assento ({fileira + 1}, {assento + 1}) não está reservado.")
    else:
        print("assento inválido")

def exibir_mapa_assentos(assentos):
    """Exibir o mapa atual dos assento."""
    print("Mapa de asssentos:")
    for i, fileira in enumerate(assentos):
        print(f"fileira {i + 1}: "+"".join(str(assento)for assento in fileira))
