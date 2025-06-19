import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def gerar_imagem_exemplo(largura=256, altura=256):
    """
    Gera uma imagem de exemplo em escala de cinza com duas regiões de intensidade distintas.

    Args:
        largura (int): Largura da imagem.
        altura (int): Altura da imagem.

    Returns:
        PIL.Image.Image: A imagem de exemplo gerada.
    """
    # Cria uma matriz de zeros para o fundo da imagem (preto)
    imagem_array = np.zeros((altura, largura), dtype=np.uint8)

    # Adiciona um retângulo mais claro
    # Os valores de intensidade vão de 0 (preto) a 255 (branco)
    intensidade_fundo = 50
    intensidade_objeto1 = 150
    intensidade_objeto2 = 220

    imagem_array.fill(intensidade_fundo) # Define o fundo

    # Primeiro objeto: um retângulo com intensidade 150
    imagem_array[50:150, 50:150] = intensidade_objeto1

    # Segundo objeto: outro retângulo com intensidade 220
    imagem_array[100:200, 100:200] = intensidade_objeto2

    # Converte o array NumPy para uma imagem Pillow
    imagem_pil = Image.fromarray(imagem_array, mode='L') # 'L' para escala de cinza

    return imagem_pil

# --- Implementação e Visualização ---
if __name__ == "__main__":
    imagem_exemplo = gerar_imagem_exemplo()

    # Salva a imagem gerada
    nome_arquivo_imagem_exemplo = "imagem.png"
    imagem_exemplo.save(nome_arquivo_imagem_exemplo)
    print(f"Imagem de exemplo salva como '{nome_arquivo_imagem_exemplo}'")

    # Exibe a imagem
    plt.figure(figsize=(6, 6))
    plt.imshow(imagem_exemplo, cmap='gray')
    plt.title("Imagem de Exemplo Gerada")
    plt.axis('off')
    plt.show()

    # Opcional: Mostra os valores únicos de intensidade na imagem para verificar
    print("Valores de intensidade únicos na imagem:", np.unique(np.array(imagem_exemplo)))