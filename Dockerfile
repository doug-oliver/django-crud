# Usa imagem oficial do Python
FROM python:3.13.5

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta do servidor
EXPOSE 8000

# Comando padrão para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
