# IT-Code_repo-5
In [5]: models.Book.objects.all()
Out[5]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Марсианские Хроники>, <Book: Оно>, <Book: 451 Градус по Фаренгейту>]>

In [8]: models.Book.objects.order_by('publication_date')
Out[8]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Марсианские Хроники>, <Book: 451 Градус по Фаренгейту>, <Book: Оно>]>

In [9]: models.Book.objects.dates("publication_date", "year")
Out[9]: <QuerySet [datetime.date(1872, 1, 1), datetime.date(1950, 1, 1), datetime.date(1953, 1, 1), datetime.date(1986, 1, 1)]>

In [10]: models.Book.objects.exclude(author='Рэй Брэдбери')
Out[10]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Оно>]>

In [11]: models.Book.objects.filter(name__contains='Г')
Out[11]: <QuerySet [<Book: Дети капитана Гранта>, <Book: 451 Градус по Фаренгейту>]>

In [12]: models.Book.objects.filter(name__exact ="Оно")
Out[12]: <QuerySet [<Book: Оно>]>

In [13]: models.Book.objects.filter(price__gt=700)
Out[13]: <QuerySet [<Book: Оно>]>

In [14]: models.Book.objects.filter(price__lt=900)
Out[14]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Марсианские Хроники>, <Book: 451 Градус по Фаренгейту>]>

In [15]: models.Book.objects.order_by('price')
Out[15]: <QuerySet [<Book: Марсианские Хроники>, <Book: 451 Градус по Фаренгейту>, <Book: Дети капитана Гранта>, <Book: Оно>]>

In [16]: models.Book.objects.reverse()
Out[16]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Марсианские Хроники>, <Book: Оно>, <Book: 451 Градус по Фаренгейту>]>

In [17]: models.Book.objects.distinct()
Out[17]: <QuerySet [<Book: Дети капитана Гранта>, <Book: Марсианские Хроники>, <Book: Оно>, <Book: 451 Градус по Фаренгейту>]>

In [20]: models.Book.objects.filter(name__contains="Дети").dates("publication_date", "day")
Out[20]: <QuerySet [datetime.date(1872, 5, 5)]>

In [25]: models.Book.objects.filter(price__gt=900) | models.Book.objects.filter(price__lt=700)
Out[25]: <QuerySet [<Book: Марсианские Хроники>, <Book: 451 Градус по Фаренгейту>]>

In [27]: models.Book.objects.filter(price__gt=900) & models.Book.objects.filter(author__contains='С')
Out[27]: <QuerySet []>

In [28]:  models.Book.objects.filter(price__gte=900) & models.Book.objects.filter(author__contains='С')
Out[28]: <QuerySet [<Book: Оно>]>

In [29]: models.Building.objects.all()
Out[29]: <QuerySet [<Building: Колизей>, <Building: Эйфелева башня>, <Building: Сиднейский Оперный Театр>, <Building: Дом Республики>]>

In [30]: models.Building.objects.order_by('height')
Out[30]: <QuerySet [<Building: Дом Республики>, <Building: Колизей>, <Building: Сиднейский Оперный Театр>, <Building: Эйфелева башня>]>

In [31]: models.Building.objects.filter(is_world_heritage=True)
Out[31]: <QuerySet [<Building: Колизей>, <Building: Эйфелева башня>, <Building: Сиднейский Оперный Театр>]>

In [32]: models.Building.objects.filter(is_world_heritage=True) & models.Building.objects.filter(height__gte=100)
Out[32]: <QuerySet [<Building: Эйфелева башня>]>

In [33]: models.Building.objects.filter(height__exact=330)
Out[33]: <QuerySet [<Building: Эйфелева башня>]>

In [36]:  models.Building.objects.exclude(is_world_heritage=False) & models.Building.objects.filter(foundation_date__range=['1900-01-01', '1999-01-31'])
Out[36]: <QuerySet [<Building: Сиднейский Оперный Театр>]>

In [37]: models.Building.objects.values('name', 'architector')
Out[37]: <QuerySet [{'name': 'Колизей', 'architector': 'Неизвестно'}, {'name': 'Эйфелева башня', 'architector': 'Стефан Совестр'}, {'name': 'Сиднейский Оперный Театр', 'architector': 'Йорн Утзон'}, {'name': 'Дом Республики', 'architector': 'Залегаллер'}]>

In [39]: models.Building.objects.order_by('foundation_date')
Out[39]: <QuerySet [<Building: Колизей>, <Building: Эйфелева башня>, <Building: Сиднейский Оперный Театр>, <Building: Дом Республики>]>

In [41]: models.Building.objects.dates("foundation_date", "month")
Out[41]: <QuerySet [datetime.date(1072, 5, 1), datetime.date(1887, 1, 1), datetime.date(1973, 10, 1), datetime.date(1979, 5, 1)]>

In [43]: models.Building.objects.exclude(is_world_heritage=True)
Out[43]: <QuerySet [<Building: Дом Республики>]>
