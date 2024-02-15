### Описание проекта:

Проект api_final_yatube - это REST API для создания публикаций и комментариев к ним и управления ими в соцсети Yatube.

Проект api_final_yatube является более проработанной версией проекта api_yatube. В нем реализованы:
1. авторизация по JWT-токену;
2. возможность аутентифицированных пользователей создавать и просмотривать публикации и комментарии к ним;
3. возможность авторизированных пользователей изменять и удалять свои публикации и комментарии;
4. возможность просмотра списка существующих групп и информации о них;
5. возможность подписки пользователей друг на друга, а также просмотра своих подписок и поиска по ним;
6. возможность пользовательского ограничения количества выводимых публикаций в ответе API;
7. возможность незарегестрированных пользователей просматривать информацию о группах, публикациях и оставленных к ним комментариях;


### Как развернуть и запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RedCloverfield/api_final_yatube
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


### Примеры запросов к API и ответов:

**Получение JWT-токена**: `POST /api/v1/jwt/create/`

Тело запроса:

```
{
  "username": "string",
  "password": "string"
}
```

Ответ:

```
{
  "refresh": "string",
  "access": "string"
}
```

**Обновление JWT-токена**: `POST /api/v1/jwt/refresh/`

Тело запроса:
```
{
  "refresh": "string"
}
```

Ответ:

```
{
  "access": "string"
}
```

**Получение списка публикаций**: `GET /api/v1/posts/`

Ответ:

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
  }
]
```

**Получение списка публикаций с пагинацией**: `GET /api/v1/posts/?offset=1&limit=4`

Ответ:

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=0&limit=1",
  "previous": "http://api.example.org/accounts/?offset=5&limit=4",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

**Создание комментария к публикации**: `POST /api/v1/posts/{post_id}/comments/`

Тело запроса:

```
{
  "text": "string"
}
```

Ответ:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**Обновление комментария по id**: `PUT /api/v1/posts/{post_id}/comments/{id}/`

Тело запроса:

```
{
  "text": "new string"
}
```

Ответ:

```
{
  "id": 0,
  "author": "new string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**Получение информации о сообществе по id**: `GET /api/v1/groups/{id}/`

Ответ:

```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

**Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса**: `POST /api/v1/follow/`

Тело запроса:
```
{
  "following": "string"
}
```

Ответ:

```
{
  "user": "string",
  "following": "string"
}
```
