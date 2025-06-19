# Processamento de Imagens

Este repositório reúne implementações práticas de algoritmos fundamentais da disciplina de **Processamento Digital de Imagens**. Os trabalhos incluem operações aritméticas, filtros, segmentação, interpolação, e outras técnicas essenciais aplicadas a imagens em escala de cinza.

---

## 📚 Conteúdo

Cada pasta ou subdiretório contém um algoritmo específico, com seu respectivo código-fonte e README explicativo:

- **Filtro de Média**  
  Suavização de imagens usando filtro de média para redução de ruídos.

- **Operações Aritméticas e Geométricas**  
  Soma, subtração e escalonamento de imagens utilizando interpolação por vizinho mais próximo.

- **Segmentação por Limiarização (Método do Vale)**  
  Segmentação automática baseada em limiares sugeridos a partir de vales do histograma suavizado.

- **Transformação de Potência (Power Law)**  
  Ajuste de contraste por meio da transformação de potência com parâmetro gamma.

- **Interpolação Bilinear e Bicúbica**  
  Técnicas de redimensionamento de imagens com interpolação suave.

- **Rotulagem de Imagens Binárias**  
  Identificação e rotulagem de componentes conectados em imagens binárias.

---

## ⚙️ Como usar

Cada algoritmo possui um README próprio com detalhes de funcionamento, requisitos e instruções de execução. Recomendamos navegar nos subdiretórios para encontrar o código e as orientações de cada trabalho.

---

## Requisitos gerais

- Python 3.8 ou superior
- Bibliotecas comuns:
  
```bash
  pip install numpy pillow matplotlib opencv-python-headless scipy
```

---

## 📁 Estrutura do Projeto

```
processamento-imagens/
├── filtro-media/
├── operacoes-aritmeticas-geometricas/
├── segmentacao-metodo-vale/
├── transformacao-power-law/
├── interpolacao-bilinear-bicubica/
├── rotulacao-img-binaria/
└── README.md            # Este arquivo
```

---

## 👨‍💻 Autoria

Desenvolvido por:

* Helorrayne Cristine de Alcantara Rodrigues
* Wanderson Almeida de Mello
  📧 [wandersonalmeidamello@gmail.com](mailto:wandersonalmeidamello@gmail.com)
  🔗 [LinkedIn](https://www.linkedin.com/in/wandersonamello/)

---

> Projeto desenvolvido para a disciplina de Processamento Digital de Imagens com foco na aplicação prática dos conceitos estudados.