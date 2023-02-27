## Запуск приложения


#### 1. Необходимо заполнить 3 .env файла:
-- .env файл в папке project - он нужен для docker-compose

-- .env файл в папке app - он нужен для поднятия django проекта из второго спринта

-- .env файл в папке postgres_to_es - он нужен для поднятия ETL сервиса

#### 2. Запустить docker-compose

```bash
docker-compose up --build
```
После этого автоматически поднимутся все сервисы из второго спринта и сервис ETL.
Они работают независимо друг от друга, добавил сервисы из прошлого спринта для удобства
и тестирования цельной системы.

#### 3. Тестирование 

Для удобства тестирования пробросил порт 9200 для Elasticsearch в docker-compose.

В папке postgres_to_es лежит test.json файл. После поднятия сервисов можно импортровать
файл в Postman и тестировать.