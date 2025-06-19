# 🔍 Interpolação Bilinear e Vizinho Mais Próximo

Este projeto implementa dois algoritmos de interpolação espacial de imagens:

* **Vizinho Mais Próximo**
* **Interpolador Bilinear**

Ambos os métodos são aplicados para **ampliação e redução** de imagens em tons de cinza, utilizando como base uma imagem original fornecida pelo usuário.

---

## 📌 Como funciona

* A imagem é carregada e convertida para escala de cinza.
* Cada algoritmo executa duas operações:

  * **Redução**: diminui as dimensões da imagem.
  * **Ampliação**: aumenta as dimensões da imagem.
* As imagens resultantes são salvas automaticamente na pasta `output/`.

---

## 🧠 Detalhes dos Algoritmos

### 🔹 Vizinho Mais Próximo

* Escolhe o valor do pixel mais próximo ao novo ponto escalado.
* Mais simples e rápido, mas pode causar efeitos de serrilhamento.

### 🔹 Interpolação Bilinear

* Calcula o valor do novo pixel com base em uma média ponderada dos 4 vizinhos mais próximos.
* Gera resultados mais suaves e naturais que o vizinho mais próximo.

---

## 🖼️ Exemplo de uso

1. Certifique-se de ter uma imagem chamada `imagem.jpg` na raiz do projeto.

2. Execute o script:

```bash
python main.py
```

3. As imagens resultantes serão salvas automaticamente:

```
output/imagem_vizinho_reduzida.jpg
output/imagem_vizinho_ampliada.jpg
output/imagem_bilinear_reduzida.jpg
output/imagem_bilinear_ampliada.jpg
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
interpolacao/
├── main.py                  # Script principal
├── Class_vizinho.py         # Classe Vizinho Mais Próximo
├── Class_bilinear.py        # Classe Bilinear
├── imagem.jpg               # Imagem de entrada (escala de cinza)
└── output/                  # Imagens geradas
```

---

## 👨‍💻 Autoria

Desenvolvido por:

* Helorrayne Cristine de Alcantara Rodrigues
* Wanderson Almeida de Mello
  📧 [wandersonalmeidamello@gmail.com](mailto:wandersonalmeidamello@gmail.com)
  🔗 [LinkedIn](https://www.linkedin.com/in/wandersonamello/)

---

> Este trabalho foi desenvolvido como parte da disciplina de **Processamento Digital de Imagens**.
