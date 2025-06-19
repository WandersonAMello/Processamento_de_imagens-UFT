from PIL import Image
import numpy as np
import os

#funções auxiliares para manipulação de imagens
def salvar(imagem_obj, nome_saida):
    """
    Salva a imagem na pasta 'output'
    
    Args:
        imagem_obj (PIL.Image): Objeto de imagem a ser salvo
        nome_saida (str): Nome do arquivo de saída
    """
    os.makedirs("output", exist_ok=True)
    caminho_saida = os.path.join("output", nome_saida)
    imagem_obj.save(caminho_saida)
    print(f"Imagem salva em: {caminho_saida}")
    print(f"Matriz resultante: {imagem_obj.size}")

def imagem_para_matriz(caminho_imagem):
    """
    Converte uma imagem em uma matriz numpy.
    
    Args:
        caminho_imagem (str): Caminho da imagem
        
    Returns:
        numpy.ndarray: Matriz de pixels em escala de cinza
    """
    try:
        imagem = Image.open(caminho_imagem).convert("L")
        matriz = np.array(imagem)
        return matriz
    except Exception as erro:
        print("Erro ao carregar a imagem:", erro)
        return None

def reescalar_imagem_para_0_255(matriz):
    """
    Normaliza os valores da matriz para o intervalo 0-255.
    
    Args:
        matriz (numpy.ndarray): Matriz de entrada
        
    Returns:
        numpy.ndarray: Matriz normalizada
    """
    valor_minimo = np.min(matriz)
    valor_maximo = np.max(matriz)
    
    if valor_maximo == valor_minimo:
        return np.zeros(matriz.shape, dtype=np.uint8)
    
    matriz_escalonada = 255 * (matriz - valor_minimo) / (valor_maximo - valor_minimo)
    return matriz_escalonada.astype(np.uint8)


#funções de operações locais

def mapeamento_valores_imagens_para_0_1(matriz):
    """
    Mapeia os valores da matriz para o intervalo [0, 1].
    
    Args:
        matriz (numpy.ndarray): Matriz de entrada
        
    Returns:
        numpy.ndarray: Matriz mapeada
    """
    
    matriz_mapeada = np.zeros(matriz.shape, dtype=np.float32)
    
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            matriz_mapeada[i,j] = (matriz[i, j]/255)
            
    return matriz_mapeada.astype(np.float32)

def power_law(matriz, gamma):
    """
    Aplica a transformação de potência à matriz.
    
    Args:
        matriz (numpy.ndarray): Matriz de entrada
        gamma (float): Valor de gamma
        
    Returns:
        numpy.ndarray: Matriz transformada
    """
    matriz_normalizada = mapeamento_valores_imagens_para_0_1(matriz)
    matriz_transformada = 255 * (matriz_normalizada ** gamma)
    return reescalar_imagem_para_0_255(matriz_transformada)

def main():
    caminho_imagem = "imagem.jpg"
    matriz_imagem1 = imagem_para_matriz(caminho_imagem)

    img = power_law(matriz_imagem1, 0.4)
    imagem_obj = Image.fromarray(img, mode="L")
    salvar(imagem_obj, "imagem_transformada.jpg")

if __name__ == "__main__":
    main()