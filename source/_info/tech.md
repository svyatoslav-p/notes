# Техническая часть

## Пользовательские расширения

Документация построена на базе Sphinx генератора документации. 
Основные расширения которые используются:
*  [MyST](https://myst-parser.readthedocs.io/) - парсер markdown значительно расширяющий возможности разметки. Рекомендуется использовать совместно с расширением [MyST-Markdown](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) для VS Code
* [Sphinx design](https://sphinx-design.readthedocs.io/) - Добавляет различные элементы такие как Dropdowns, Card, Buttons и т.д.
* [Sphinx copy button](https://sphinx-copybutton.readthedocs.io/en/latest/) - Добавляет кнопку копирования кода из блока кода. Имеет настройки (например что бы исключить копирование комментариев в блоке кода)
* [Sphinx toggle button](https://sphinx-togglebutton.readthedocs.io/en/latest/) - Добавляет элемент «кнопки переключения»
* [Sphinx book theme](https://sphinx-book-theme.readthedocs.io/) - Тема оформления документации

## Пользовательские директивы

Описаны в файле `custom_directives.py`. Содержат пользовательские расширения функциональности Sphinx

* **MystExampleDirective** - директива вытащена из офф репозитория расширения **MyST**. Используется для
  удобного отображения примеров использования синтаксиса Sphinx и различных расширений Sphinx

## Ошибки, предупреждения

* {bdg-warning-line}`Warning: Pygments lexer name 'myst' is not known` - можно игнорировать
  появляется из за пользовательской директивы MystExampleDirective которая использует синтаксис MyST.
  Поэтому Pygments не может распознать этот синтаксис
