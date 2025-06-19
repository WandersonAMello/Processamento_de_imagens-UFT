# 🏷️ Algoritmo de Rotulação de Imagens Binárias

Este repositório apresenta a implementação de um algoritmo para **rotulação de componentes conectados** em imagens binárias. É uma técnica fundamental em processamento de imagens, usada para identificar objetos ou regiões distintas em uma imagem onde os pixels são representados apenas como 0 (fundo) ou 1/255 (objeto).

---

## 🧠 Como funciona o algoritmo?

### 📌 1. Entrada
- Imagem binária (valores de pixels: 0 = fundo, 1 ou 255 = objeto).

### 🔁 2. Passagens do algoritmo

O algoritmo é composto por **duas passagens principais**:

#### 🔹 Primeira Passagem
- Varre a imagem linha por linha.
- Para cada pixel "ativo":
  - Verifica os vizinhos já processados (normalmente à esquerda e acima).
  - Se nenhum vizinho ativo → novo rótulo.
  - Se houver vizinhos com rótulos → usa o menor rótulo e registra equivalências.

#### 🔹 Segunda Passagem
- Substitui os rótulos por seus representantes finais, resolvendo as equivalências.
- Garante que todos os pixels de um mesmo componente compartilhem o mesmo rótulo.

---

## 🔗 Tipos de Conectividade

- **4-conectividade**: considera os vizinhos à esquerda e acima.
- **8-conectividade** (extensão): considera todos os vizinhos ao redor do pixel (em cruz e diagonal).

---

## 🎨 Saída

- Imagem com regiões rotuladas usando valores inteiros únicos.
- Pode ser colorida (falsa cor) para facilitar a visualização.

---
