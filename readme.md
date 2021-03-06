# Gestures Recognition - Eng. Unificada I

> Esse repositório contém os códigos e arquivos para o treinamento, execução do reconhecimento de gestos aplicados a uma interface gráfica. 

---

## Treino

O treino consiste de uma série de comandos para a execução do treinamento utilizando o TensorFlow. Note que é necessário a pasta com as imagens do [Jester](https://20bn.com/datasets/jester). O treinamento pode ser rodado tanto na pasta compactada (muito ineficiente) quanto na pasta descompactada, contudo deve ser modificado no arquivo `train.py`. Demais modificações devem ser feitas no arquivo `config.json`.

### Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1S3rzcHJ5_0XAPc_M9x8-HB4DkScFk1vc?usp=sharing)

Uma maneira fácil de rodar é utilizando o google colab. Mas, para treinar de forma agradável, salve uma cópia do dataset reduzindo com os labels que você quer dentro do seu drive. Em seguida, arrume os caminhos no dicionário no início que melhor satisfaçam o seu interesse. Fique a vontade para rodar os arquivos `.py` disponibilizados também. 

## Modelo

O modelo consiste numa rede com um série de camadas convolucionais e uma camada final de Global Average Pooling. Essas camadas convolucional são então distribuída no tempo e passam por uma camada GRU para extrair a informação temporal das imagens. Por fim, as útimas camadas densas finalizam numa camada com 8 classes e função de ativação softmax.

### Modelo de Convolução

|Layer (type)               |  Output Shape           |   Param #   |
|:-------------------------:|:-----------------------:|:-----------:|
| (Conv2D)          | (None, 100, 100, 64)    |  1792       |
| (Dropout)        | (None, 100, 100, 64)    |  0          |
| (Conv2D)          | (None, 100, 100, 64)    |  36928      |
| (Dropout)        | (None, 100, 100, 64)    |  0          |
| (BatchNormalization)| (None, 100, 100, 64)    |  256        |
| (MaxPooling 2D) | (None, 50, 50, 64)      |  0          |
| (Conv2D)          | (None, 50, 50, 128)     |  73856      |
| (Dropout)        | (None, 50, 50, 128)     |  0          |
| (Conv2D)          | (None, 50, 50, 128)     |  147584     |
| (Dropout)        | (None, 50, 50, 128)     |  0          |
| (BatchNormalization)| (None, 50, 50, 128)     |  512        |
| (MaxPooling 2D)  | (None, 25, 25, 128)     |  0          |
| (Conv2D)          | (None, 25, 25, 256)     |  295168     |
| (Dropout)        | (None, 25, 25, 256)     |  0          |
| (Conv2D)          | (None, 25, 25, 256)     |  590080     |
| (Dropout)        | (None, 25, 25, 256)     |  0          |
| (BatchNormalization)| (None, 25, 25, 256)     |  1024       |
| (MaxPooling 2D)| (None, 12, 12, 256)     |  0          |
| (Conv2D)          | (None, 12, 12, 512)     |  1180160    |
| (Dropout)        | (None, 12, 12, 512)     |  0          |
| (Conv2D)          | (None, 12, 12, 512)     |  2359808    |
| (Dropout)        | (None, 12, 12, 512)     |  0          |
| (BatchNormalization)| (None, 12, 12, 512)     |  2048       |
| (GlobalAveragePooling2D)| (None, 512)             |  0          |

### Modelo de Classificação

| Layer (type) |                Output Shape     |         Param # |  
|:------------:|:-------------------------------:|:---------------:|
| (TimeDistributed)  | (None, 20, 512) |          4689216 |  
| (GRU) |                   (None, 120) |              228240   | 
| (Dropout) |         (None, 120) |              0        | 
| (Dense) |               (None, 60) |               7260     | 
| (Dropout) |         (None, 60) |               0        | 
| (Dense) |             (None, 30) |               1830     |
| (Dropout) |        (None, 30) |               0        | 
| (Dense) |             (None, 8) |                248      | 

## Gerador

O intuito de utilzar o gerador foi alimentar o modelo on-the-fly sem sobrecarregar a memória RAM uma vez que o dataset era bem grande. Além disso, um benefíio do gerador é possibilitar Data Augmentation, i.e., as imagens são invertidas horizontalmente, sofrem zoom, são escalonadas e até levemente rotaciondas. Mesmo com um dataset grande, esse tipo de manobra reduz os possíveis viéses e ainda mitiga, até certo ponto, o efeito do overfitting.

---

## Interface

A interface depende da biblioteca Vedo bem como dos arquivos na pasta `mesh`. Os comandos para sua utilização são:

- ↑: Análise de slices / Volta para exame de gordura
- ←: Volta nos exames passados
- →: Avança nos exames futuros
- s: Seleciona para comparar/compara
- r: Rotaciona modelo 3d (direira) / Avança slices (cima)
- l: Rotaciona modelo 3d (esquerda) / Volta slices (baixo)
