# Шаблоны

## Общее форматирование

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/typography.html#typography
:color: primary
:outline:
Полное описание
```

### Разрыв

**Пример:**

```{myst-example}

Текст до разделителя
***
Текст после разделителя

```

### Конец строки

```{myst-example}

**Fleas** \
Adam \
Had 'em.

```

### Лист задач

```{myst-example}

- [ ] An item that needs doing
- [x] An item that is complete

```

### Лист полей

````{myst-example}

:param arg1: A description of arg1
:param arg2: A longer description,
    with multiple lines.

    - And bullet points
:return: A description of the return value

````

## Изображения

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html#images-and-figures
:color: primary
:outline:
Полное описание
```
**Примеры:**


````{myst-example}

```{image} ../assets/images/logo.png
:alt: fishy
:class: bg-primary
:width: 200px
:align: center
```
````

## Замечания

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html#admonitions
:color: primary
:outline:
Полное описание
```
Возможные типы: 

* `attention`
* `danger`
* `error`
* `hint`
* `important` (важно)
* `note`
* `seealso` (смотрите также)
* `tip`
* `warning`

**Примеры:**

````{myst-example}

```{tip}
:class: dropdown
:name: a-tip-reference

Текст бокса
```

[Reference to my tip](#a-tip-reference)

````

````{myst-example}

```{note}
:name: a-tip-reference

Текст бокса
```

[Reference to my tip](#a-tip-reference)

````

````{myst-example}

```{versionadded} 1.2.3
Explanation of the new feature.
```

```{versionchanged} 1.2.3
Explanation of the change.
```

```{deprecated} 1.2.3
Explanation of the deprecation.
```

````

## Таблицы

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/tables.html#tables
:color: primary
:outline:
Полное описание
```
**Примеры:**


````{myst-example}

```{table} Table caption
:widths: auto
:align: center

| foo | bar |
| --- | --- |
| baz | bim |
```

````

## Исходный код

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html#source-code-and-apis
:color: primary
:outline:
Полное описание
```
**Примеры:**


````{myst-example}

```{code-block} python
:caption: Тут подпись
:emphasize-lines: 2,3
:lineno-start: 1

a = 1
b = 2
c = 3
```

````

## Кросс-ссылки

```{button-link} https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#cross-references
:color: primary
:outline:
Полное описание
```
**Примеры:**


````{myst-example}

(heading-target)=
### Heading

{#paragraph-target}
This is a paragraph, with an `id` attribute.

This is a [span with an `id` attribute]{#span-target}.

:::{note}
:name: directive-target

This is a directive with a `name` option
:::

[reference1](#heading-target), [reference2](#paragraph-target),
[reference3](#span-target), [reference4](#directive-target)

````

Неявные цели 

````{myst-example}

## A heading with slug

## A heading with slug

<project:#a-heading-with-slug>

[Explicit title](#a-heading-with-slug-1)

````


## Значки

```{button-link} https://sphinx-design.readthedocs.io/en/sbt-theme/badges_buttons.html#badges
:color: primary
:outline:
Полное описание
```
**Примеры:**

```{myst-example}

{bdg-link-primary-line}`Пример ссылки <https://sphinx-design.readthedocs.io/en/sbt-theme/badges_buttons.html#badges>`

{bdg-primary}`primary`, {bdg-primary-line}`primary-line`

{bdg-warning}`warning`, {bdg-warning-line}`warning-line`

```

## Кнопки

```{button-link} https://sphinx-design.readthedocs.io/en/sbt-theme/badges_buttons.html#buttons
:color: primary
:outline:
Полное описание
```
**Примеры:**

````{myst-example}

```{button-link} https://example.com
:color: primary
:outline:
```

```{button-link} https://example.com
:color: primary
:shadow:
```

```{button-link} https://example.com
:color: secondary
:expand:
**Текст кнопки жирный**
```

````

## Скрывающийся контент

```{button-link} https://sphinx-design.readthedocs.io/en/sbt-theme/dropdowns.html#dropdowns
:color: primary
:outline:
Полное описание
```
**Примеры:**

````{myst-example}

```{dropdown} Имя заголовка
:open:
:color: primary
:icon: megaphone

Dropdown content
```

````

## Вкладки

```{button-link} https://sphinx-design.readthedocs.io/en/sbt-theme/tabs.html#tabs
:color: primary
:outline:
Полное описание
```
**Примеры:**

`````{myst-example}


````{tab-set}

```{tab-item} Label2
Content 1
```

```{tab-item} Label2
Content 2
```

````

`````
Вкладки только со вставкой кода

`````{myst-example}

````{tab-set-code}

```{code-block} bash
if [ -z $logged_on ]
then
echo "$1 is not logged on."
echo "Exit"
exit
fi
```

```{code-block} javascript
a = 1;
```

````

`````
