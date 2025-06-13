# Imagem base
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia o código para o container
COPY app.py .

# Instala o Flask
RUN pip install flask

# Expõe a porta da aplicação
EXPOSE 5000

# Comando para rodar a API
CMD ["python", "app.py"]
