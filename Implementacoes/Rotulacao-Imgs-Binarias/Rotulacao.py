# Dupla: Helorrayne e Wanderson
# Disciplina: Processamento Digital de Imagens

from PIL import Image
import numpy as np
import os

def numero_para_letra(n):
    """
    Converte um número para uma letra estilo Excel (A, B, ..., Z, AA, AB, ...).
    """
    letras = ""
    while n > 0:
        n -= 1
        letras = chr(65 + n % 26) + letras
        n //= 26
    return letras

def salvar_equivalencias(equivalencias, nome_arquivo="Rotulos_Equivalentes.txt"):
    """
    Salva os pares de rótulos equivalentes em um arquivo .txt
    """
    os.makedirs("output", exist_ok=True)
    caminho = os.path.join("output", nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for menor, maior in equivalencias:
            linha = f"{numero_para_letra(menor)} = {numero_para_letra(maior)}"
            arquivo.write(linha + "\n")

def salvar_matriz_txt(matriz_letras, nome_arquivo="Matriz_Rotulada.txt"):
    """
    Salva a matriz rotulada (com letras) em um arquivo .txt
    """
    os.makedirs("output", exist_ok=True)
    caminho = os.path.join("output", nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for linha in matriz_letras:
            texto = " ".join(linha)
            arquivo.write(texto + "\n")
 
def binarizar(imagem, criterio):
    """
    Binariza a imagem com base no critério fornecido
    """
    matriz = np.array(imagem.convert("L"))
    matriz_bin = np.where(matriz >= 127, 255, 0)
    matriz_binarizada = np.where(matriz_bin >= criterio, 1, 0)  # se p = 255, p = branco, senão p = preto
    
    #salvar imagem binarizada
    imagem_binarizada = Image.fromarray(np.uint8(matriz_bin), mode='L')
    imagem_binarizada.save("output/imagem_binarizada.png")

    return matriz_binarizada

def rotulacao(matriz_binarizada):
    """
    Aplica o algoritmo de rotulação com 4-adjacência, converte para letras e salva equivalências.
    """
    linhas, colunas = matriz_binarizada.shape
    matriz_rotulada = np.zeros((linhas, colunas), dtype=int)
    rotulo_atual = 0
    equivalencias = []

    # Primeira passagem
    for i in range(linhas):
        for j in range(colunas):
            # se p = 0, não faz nada
            
            if matriz_binarizada[i, j] == 1:
                # se p = 1, analisa os vizinhos (s)uperior e (r)esquerdo
                r = matriz_rotulada[i, j - 1] if j > 0 else 0
                s = matriz_rotulada[i - 1, j] if i > 0 else 0
                    
                # Se ambos os vizinhos são 0, atribui um novo rótulo
                if r == 0 and s == 0:
                    rotulo_atual += 1
                    matriz_rotulada[i, j] = rotulo_atual
                    
                # Se apenas um vizinho é 0, atribui o rótulo do vizinho
                elif r != 0 and s == 0:
                    matriz_rotulada[i, j] = r
                elif r == 0 and s != 0:
                    matriz_rotulada[i, j] = s
                
                # Se ambos os vizinhos são diferentes de 0, atribui o menor rótulo e registra a equivalência
                else:
                    menor = min(r, s)
                    maior = max(r, s)
                    matriz_rotulada[i, j] = menor
                    if menor != maior:
                        equivalencias.append((menor, maior)) # salva numa tupla (menor, maior)

    # Segunda passagem: substituições
    substituicoes = {}
    for menor, maior in equivalencias:
        if maior in substituicoes:
            substituicoes[maior] = min(substituicoes[maior], menor)
        else:
            substituicoes[maior] = menor

    for i in range(linhas):
        for j in range(colunas):
            r = matriz_rotulada[i, j]
            while r in substituicoes:
                r = substituicoes[r]
            matriz_rotulada[i, j] = r

    # Converte os rótulos numéricos para letras
    letras_usadas = {}
    prox_letra = 1
    matriz_letras = np.full_like(matriz_rotulada, '.', dtype=object) # inicia e preenche com '.' para espaços vazios

    for i in range(linhas):
        for j in range(colunas):
            rotulo = matriz_rotulada[i, j]
            if rotulo != 0:
                if rotulo not in letras_usadas:
                    letras_usadas[rotulo] = numero_para_letra(prox_letra)
                    prox_letra += 1
                matriz_letras[i, j] = letras_usadas[rotulo]

    # Salva arquivos auxiliares
    salvar_equivalencias(equivalencias)
    salvar_matriz_txt(matriz_letras)

    return matriz_letras


def main():
    caminho_imagem = "imagem.jpg"  
    try:
        imagem = Image.open(caminho_imagem).convert("L")
    except Exception as erro:
        print("Erro ao carregar a imagem:", erro)
        return

    # Binariza a imagem com base no critério cinza = 255
    matriz_binarizada = binarizar(imagem, criterio=255)

    # Aplica o algoritmo de rotulação 
    rotulacao(matriz_binarizada)
    

if __name__ == "__main__":
    main()
