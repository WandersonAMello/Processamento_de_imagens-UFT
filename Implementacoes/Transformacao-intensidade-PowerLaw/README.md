# Transformação de Potência (Power Law)

Este projeto implementa a transformação de potência para ajuste de contraste em imagens em escala de cinza. A transformação é aplicada pixel a pixel, elevando o valor normalizado ao expoente gamma.

---

## Como funciona

- Converte a imagem para escala de cinza.
- Normaliza os valores dos pixels para o intervalo [0, 1].
- Aplica a transformação de potência: \( s = c \cdot r^\gamma \), onde:
  - \( r \) é o valor do pixel normalizado,
  - \( \gamma \) é o parâmetro de controle,
  - \( c \) é uma constante de escala (255 no código).
- Reconverte a imagem para valores entre 0 e 255.
- Salva a imagem resultante.

---

## Exemplo de uso

1. Coloque sua imagem na raiz do projeto com o nome `imagem.jpg`.
2. Execute o script:
```bash
python main.py
```
3. A imagem transformada será salva na pasta output/ com o nome imagem_transformada.jpg.

## 👨‍💻 Autoria

Desenvolvido por:

* Helorrayne Cristine de Alcantara Rodrigues
* Wanderson Almeida de Mello
  📧 [wandersonalmeidamello@gmail.com](mailto:wandersonalmeidamello@gmail.com)
  🔗 [LinkedIn](https://www.linkedin.com/in/wandersonamello/)

---

> Este trabalho foi desenvolvido como parte da disciplina de **Processamento Digital de Imagens** e tem caráter acadêmico.
