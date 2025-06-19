# Segmentação de Imagens por Limiarização usando Método do Vale

Este projeto implementa uma técnica de segmentação de imagens baseada em limiarização automática utilizando o **método do vale** no histograma da imagem. O método identifica pontos baixos (vales) no histograma suavizado para sugerir limiares de segmentação.

---

## Como funciona

1. Carrega a imagem em escala de cinza.
2. Calcula o histograma dos níveis de cinza.
3. Suaviza o histograma usando filtro Gaussiano para facilitar a detecção de vales.
4. Encontra os vales no histograma suavizado, que representam potenciais limiares de segmentação.
5. Aplica cada limiar para segmentar a imagem em regiões binárias.
6. Exibe os resultados de segmentação para cada limiar sugerido.

---