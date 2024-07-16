# Активация

1. Переходим по ссылке [jetbra.in](https://jetbra.in/s)
1. Скачиваем архив с именем `jetbra.zip`
1. Распакуем в любой каталог, но путь недолжен содержать пробелы и кириллицу. Например `~/system/jetbrains/ja-netfilter-all/` 
1. Выполним генерацию конфигурации `~/system/jetbrains/ja-netfilter-all/scripts/install.sh`
1. Выйдем из системы и снова залогинимся
1. Скопируем обновленную необходимую конфигурацию (например для Intellij Idea Ultimate) из каталога
   `~/system/jetbrains/ja-netfilter-all/vmoptions/idea.vmoptions` в каталоги:
   * `~/.config/JetBrains/IntelliJIdea20xx.x/idea.vmoptions`
   * `~/.config/JetBrains/IntelliJIdea20xx.x/idea64.vmoptions` (с последующим переименованием)
1. Снова открываем [jetbra.in](https://jetbra.in/s) и копируем ключь продукта (кликнуть на нужной карточке)
1. Открываем продукт JetBrains (например Intellij Idea Ultimate) и вставляем ключ в поле Active Code

```{warning}
Для работы таблекти требуется установленная JVM на хосте
```
Таким же образом активируем и плагины