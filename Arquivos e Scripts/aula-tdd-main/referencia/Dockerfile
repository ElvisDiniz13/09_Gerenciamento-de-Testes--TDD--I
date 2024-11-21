# Usa a imagem oficial do Python 3.9 do Docker Hub
FROM python:3.9-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /src

# Copia todo o diretório 'src' da máquina host para dentro do container em /src
COPY ./src /src

# Copia o arquivo requirements.txt da máquina host para dentro do container em /src
COPY  requirements.txt /src

# Atualiza o pip
RUN pip3 install --upgrade pip

# Instala as dependências do Python listadas no requirements.txt
RUN pip install -r requirements.txt

# Inicializa o container e deixa ele rodando
ENTRYPOINT ["tail", "-f", "/dev/null"]