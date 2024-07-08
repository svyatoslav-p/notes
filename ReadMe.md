### Описание репозитория

Проект wiki документации на базе инструмента **sphinx** в котором описаны рекомендации, процессы настройки\конфигурирования и общие "памятки".
Описание технической части искать в `source/_info/*.md`

### Сборка

1. Необходим установленный **Python**
2. Зависимости `cd ./source` `pip install -r requirements.txt`
3. Сборка проекта `make html`, `.\make.bat html` (для windows) либо `sphinx-build -M html source build`

После сборки можно открыть файл `build/html/index.html` для просмотра итогового результата. При использовании
CI pipeline искать в артефактах аналогичный файл
