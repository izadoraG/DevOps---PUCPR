# Use uma imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o restante dos arquivos do seu projeto para o contêiner
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Especifique o comando padrão a ser executado quando o contêiner for iniciado
CMD ["python", "calculadora.py"]
