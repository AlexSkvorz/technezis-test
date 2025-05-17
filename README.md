# Тестовое задание Технезис

## Инструкция по запуску (с docker)
### 1. Клонируйте репозиторий
```bash
git https://github.com/AlexSkvorz/technezis-test
cd technezis-test
```
### 2. Создайте файл БД
```bash
touch tehnezis.db
```
### 3. Создайте файл конфигурации
```bash
cp .env.example .env
```
BOT_TOKEN=токен от BotFather
### 4. Выполните команды
```bash
docker build -t technezis-test-bot .
```
```bash
docker run --env-file .env \        
  -v $(pwd)/tehnezis.db:/app/tehnezis.db \
  -v $(pwd)/uploads:/app/uploads \
  technezis-test-bot
```

## Инструкция по запуску (без docker)

### 1. Клонируйте репозиторий
```bash
git https://github.com/AlexSkvorz/technezis-test
cd technezis-test
```
### 2. Установите зависимости
```bash
poetry install
```
### 3. Создайте файл конфигурации
```bash
cp .env.example .env
```
BOT_TOKEN=токен от BotFather
### 4. Создайте файл БД
```bash
touch tehnezis.db
```
### 5. Примените миграции БД
```bash
alembic -c alembic/alembic.ini upgrade head
```
### 5. Запустите бота
```bash
poetry run python main.py
```
