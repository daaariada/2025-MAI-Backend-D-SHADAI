# cathub/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/cathub

# 5. Копируем все в /app/cathub
COPY . .

# 6. Копируем entrypoint.sh в корень (он будет в /app/entrypoint.sh)
COPY entrypoint.sh /app/

# 7. Делаем его исполняемым
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]