# 🧪 Filtro de Média

Este projeto implementa o algoritmo de **filtro de média** para suavização de imagens em escala de cinza. O filtro de média é utilizado no processamento digital de imagens para reduzir ruídos, aplicando a média dos pixels vizinhos a cada ponto da imagem.

---

## 📌 Como funciona

O algoritmo realiza a convolução da imagem com uma matriz (máscara) de médias, de forma manual com o auxílio da biblioteca NumPy. O tamanho da máscara é configurável (ex: 3x3, 5x5, 7x7...).

### 🧠 Passos principais:

1. Carrega a imagem original em escala de cinza.
2. Cria uma máscara de média (com valores iguais a `1 / (tamanho x tamanho)`).
3. Aplica a média apenas onde a máscara encaixa completamente (ignora bordas).
4. Gera uma nova imagem com os valores suavizados.
5. Salva o resultado em uma pasta chamada `output/`.

---

## 🖼️ Exemplo de uso

1. Certifique-se de ter uma imagem chamada `imagem.png` na raiz do projeto.

2. Execute o script:

```bash
python main.py
```

3. A imagem resultante será salva automaticamente na pasta `output/` com o nome:

```
imagem_filtrada_media_7x7.png
```

---

## ⚙️ Requisitos

* Python 3.8 ou superior
* Bibliotecas necessárias:

```bash
pip install pillow numpy
```

---

## 📁 Estrutura do Projeto

```
filtro-media/
├── main.py              # Script principal com a aplicação do filtro de média
├── imagem.png           # Imagem de entrada (deve estar na raiz do projeto)
└── output/              # Pasta onde a imagem filtrada será salva automaticamente
```

---

## 👨‍💻 Autoria

Desenvolvido por:

* Helorrayne Cristine de Alcantara Rodrigues
* Wanderson Almeida de Mello
  📧 [wandersonalmeidamello@gmail.com](mailto:wandersonalmeidamello@gmail.com)
  🔗 [LinkedIn](https://www.linkedin.com/in/wandersonamello/)

---

> Este trabalho foi desenvolvido como parte da disciplina de **Processamento Digital de Imagens** e tem caráter acadêmico.
