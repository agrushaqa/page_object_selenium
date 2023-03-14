Тестовое задание по автоматизации тестирования.

Пожалуйста, сделайте этот тесткейс на языке python

используя паттерн PageObject и библиотеку webdriver manager. 
Скиньте ссылку на публичный репозиторий с вашим решением.


Шаг	Действие	ОР
1	Открыть в браузере ссылку https://demoqa.com/	Сайт https://demoqa.com/ открыт
2	Нажать кнопку Elements	Открыта страница Elements
3	В раскрытом меню справа кликнуть лкм Check Box	Открыта страница Check Box
4	Раскрыть директорию Home. 	Директория Home раскрыта
5	Раскрыть директорию Downloads 	Директория Downloads раскрыта
6	Выбрать чекбокс Word File.doc	"Чекбокс файла Word File.doc выбран. Появилось сообщение ""You have selected:
wordFile"""


# Настройка
# requirements.txt
## create
pip freeze > requirements.txt
## use
pip install -r requirements.txt

# code style
## isort
python -m pip install isort
### run 
isort .
## mypy
python -m pip install mypy
### run 
mypy .
## flake8
python -m pip install flake8
### run
flake8 --exclude venv,docs --ignore=F401


# Pytest - Run Tests in Parallel
## install
```pip install pytest-xdist```

also:
https://pypi.org/project/pytest-parallel/
## run
```pytest -n 2 test_common.py```

# run with allure
python -m pytest --rootdir=. tests --alluredir=reports/
- требует установки
pip install allure-pytest

# allure
allure generate report && allure open
