Проект в Docker'е [https://www.docker.com].
Внутри образа database postgrsql и зависимости.

Api's functions

Weather - Отправляет в ответ среднюю температуру и скорость ветра в Городе, список городов указан ниже.
Адрес для запросов - [Локальный адрес сервера] + /weather & пример ("http://127.0.0.1:5000/weather").
В теле запроса обязателен параметр json, туда помещается указанный город & пример  {json='Москва'}.
Принимаются только POST запросы.

[Москва, Санкт-Петербург, Новосибирск, Екатеринбург, Нижний Новгород, Казань, Челябинск, Омск, Самара, Ростов-на-Дону, Уфа, Красноярск, Воронеж, Пермь, Волгоград, Саратов, Тюмень, Барнаул, Ижевск, Ульяновск, Калуга, Тольятти, Ставрополь, Магнитогорск, Набережные Челны, Сочи, Кострома, Смоленск, Тверь, Рязань, Липецк, Чебоксары, Тула, Ярославль, Брянск, Калининград, Архангельск, Сургут, Нижний Тагил, Кемерово, Астрахань, Сыктывкар, Петрозаводск, Норильск, Салават, Таганрог, Сарапул, Златоуст, Курган, Северодвинск, Невинномысск, Кисловодск, Светлоград, Тихвин, Саранск, Сызрань]

