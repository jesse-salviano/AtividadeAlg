def inserir(raiz, valor):
    if raiz is None:
        return {"valor": valor, "esq": None, "dir": None}
    
    if valor < raiz["valor"]:
        raiz["esq"] = inserir(raiz["esq"], valor)
    elif valor > raiz["valor"]:
        raiz["dir"] = inserir(raiz["dir"], valor)
        
    return raiz


def buscar(raiz, valor):
    if raiz is None or raiz["valor"] == valor:
        return raiz
    
    if valor < raiz["valor"]:
        return buscar(raiz["esq"], valor)
    return buscar(raiz["dir"], valor)


def em_ordem(raiz):
    if raiz is None:
        return []
    return em_ordem(raiz["esq"]) + [raiz["valor"]] + em_ordem(raiz["dir"])


def _min_valor_no(raiz):
    atual = raiz
    while atual["esq"] is not None:
        atual = atual["esq"]
    return atual


def remover(raiz, valor):
    if raiz is None:
        return raiz

    if valor < raiz["valor"]:
        raiz["esq"] = remover(raiz["esq"], valor)
    elif valor > raiz["valor"]:
        raiz["dir"] = remover(raiz["dir"], valor)
    else:
        if raiz["esq"] is None:
            return raiz["dir"]
        elif raiz["dir"] is None:
            return raiz["esq"]

        temp = _min_valor_no(raiz["dir"])
        raiz["valor"] = temp["valor"]
        raiz["dir"] = remover(raiz["dir"], temp["valor"])

    return raiz


def altura(no):
    if no is None:
        return 0
    
    alt_esq = altura(no["esq"])
    alt_dir = altura(no["dir"])
    
    return max(alt_esq, alt_dir) + 1


if __name__ == "__main__":
    arvore = None
    valores = [50, 30, 70, 20, 40, 60, 80]
    
    for v in valores:
        arvore = inserir(arvore, v)
        
    print("Percurso In-Order inicial:", em_ordem(arvore))
    print("Altura inicial da árvore (níveis):", altura(arvore))
    
    resultado_busca = buscar(arvore, 60)
    print("Busca pelo 60:", "Encontrado!" if resultado_busca else "Não encontrado.")
    
    arvore = remover(arvore, 20)
    arvore = remover(arvore, 30)
    arvore = remover(arvore, 70)
    
    print("Percurso In-Order após remoções (20, 30, 70):", em_ordem(arvore))
    print("Altura final da árvore (níveis):", altura(arvore))