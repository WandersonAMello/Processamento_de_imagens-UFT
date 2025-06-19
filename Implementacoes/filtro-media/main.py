# Trabalho Prático - Processamento Digital de Imagens
# Discentes: Helorrayne Cristine de Alcantara Rodrigues e Wanderson Almeida de Mello
# filtro de média

from PIL import Image
import numpy as np
import os



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

def imagem_para_matriz(caminho_imagem):
    """
    Converte uma imagem em uma matriz numpy.
    
    Args:
        caminho_imagem (str): Caminho da imagem
        
    Returns:
        numpy.ndarray: Matriz de pixels em escala de cinza ou None se a imagem não for encontrada.
    """
    try:
        imagem_obj = Image.open(caminho_imagem).convert('L')  # Converte para escala de cinza
        matriz_imagem = np.array(imagem_obj, dtype=np.float32)
        return matriz_imagem
    except FileNotFoundError:
        print(f"Erro: Imagem não encontrada em '{caminho_imagem}'")
        return None
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        return None
    
def filtro_media(matriz_imagem, tamanho_filtro):
    
    
    qtd_linhas_imagem, qtd_colunas_imagem = matriz_imagem.shape
    
    ponto_central_filtro = tamanho_filtro // 2
    filtro = np.ones((tamanho_filtro, tamanho_filtro), dtype=np.float32) / (tamanho_filtro * tamanho_filtro)
    # Cria o filtro de média preenchido com 1/(tamanho_filtro*tamanho_filtro)
    matriz_filtrada = np.zeros((qtd_linhas_imagem, qtd_colunas_imagem), dtype=np.float32)
    
    for linha in range(qtd_linhas_imagem):
        for coluna in range(qtd_colunas_imagem):
            # atribui valor zero para os pixels que não podem ser calculados nas bordas
           if (linha < ponto_central_filtro or linha >= qtd_linhas_imagem - ponto_central_filtro or
               coluna < ponto_central_filtro or coluna >= qtd_colunas_imagem - ponto_central_filtro):
                matriz_filtrada[linha, coluna] = 0
           else: 
                soma = np.sum(matriz_imagem[linha - ponto_central_filtro:linha + ponto_central_filtro + 1,
                                            coluna - ponto_central_filtro:coluna + ponto_central_filtro + 1] * filtro) 
                matriz_filtrada[linha, coluna] = soma
                
    return matriz_filtrada
    
        


def main():
    # Carregar a imagem
    caminho_imagem = "imagem.png"
    matriz_imagem = imagem_para_matriz(caminho_imagem)
    
    if matriz_imagem is None:
        return
    
    # Definir o tamanho do filtro
    tamanho_filtro = 7  # Deve ser ímpar
    # Aplicar o filtro de média
    matriz_filtrada = filtro_media(matriz_imagem, tamanho_filtro)
    # Converter a matriz filtrada de volta para imagem
    matriz_filtrada_clipada = np.clip(matriz_filtrada, 0, 255)
    imagem_filtrada_obj = Image.fromarray(matriz_filtrada_clipada.astype(np.uint8), 'L') 

    # Salvar a imagem filtrada
    nome_base, extensao = os.path.splitext(os.path.basename(caminho_imagem))
    nome_arquivo_saida = f"{nome_base}_filtrada_media_{tamanho_filtro}x{tamanho_filtro}{extensao}"
    salvar(imagem_filtrada_obj, nome_arquivo_saida)

    print(f"Filtro de média {tamanho_filtro}x{tamanho_filtro} aplicado com sucesso!")

if __name__ == "__main__":
    main()