# scrapy_parser_pep
Проект предназначен для сбора информации о документах PEP с сайта [https://peps.python.org/](https://peps.python.org/).
При помощи парсера можно получить в табличной форме (файлы CSV) о номерах, наименованиях и статусах всех документов PEP,
а также получить сводку по статусам PEP — сколько найдено документов в каждом статусе.
## Установка и использование пасера:
 - Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:corbuncul/scrapy_parser_pep.git
cd scrapy_parser_pep
```
- Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
- Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
- Запустить проект:
```
scrapy crawl pep
```
Собранные данные будут находиться в директории results в CSV-файлах.