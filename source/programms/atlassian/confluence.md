# Confluence

## Установка

Пример установки на Ubuntu 24.04 версии Confluence 8.9.3

### Подготовка системы

```{code-block} bash
# Установим вспомогательные пакеты
sudo apt update
sudo apt upgrade
sudo apt install mc wget
sudo ufw disable

# Скачаем актуальный пакет Confluence
wget https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-X.X.X-x64.bin

# Установим поддерживаемую Confluence версию PostgreSQL (в данном случае 15)
sudo apt install -y wget gnupg2
wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
sudo apt update
sudo apt install -y postgresql-15

# Установим поддерживаемую Confluence версию JDK (необходима для таблетки)
sudo apt install openjdk-17-jdk -y
```
### Подготовка БД

Изменить метод авотризации для локальных пользователей

1. Отредактировать `sudo nano /etc/postgresql/15/main/pg_hba.conf` установив метод авторизации для локальных подключений md5

   ```{code-block} bash
   # IPv4 local connections:
   host    all             all             127.0.0.1/32            md5
   # IPv6 local connections:
   host    all             all             ::1/128                 md5
   ```
1. Создать БД и пользователя

   ```{code-block} bash
   su - postgres

   # Создаем пользователя с паролем
   psql -c "CREATE ROLE confluence_user LOGIN SUPERUSER PASSWORD '<Задать пароль>';"

   # Создаем БД
   psql -c "CREATE DATABASE confluence_db WITH ENCODING 'UNICODE' LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0;"
   exit
   ```
### Установка пакета

```{code-block} bash
# Сделать файл исполняемым
sudo sudo chmod a+x ~/atlassian-confluence-X.X.X-x64.bin

# Запуск установки
sudo ~/atlassian-confluence-X.X.X-x64.bin
```
В процессе будут выходить вопросы на которые нужно ответить. Можно смело выбирать **default mode** но на вопросе об
установке сервиса желательно ответить Yes тогда будет создан сервис systemctl через который удобно управлять приложением.

Каталоги по умолчанию это:
* `/opt/atlassian/confluence`
* `/var/atlassian/application-data/confluence`

Настроим службу systemctl

```{code-block} bash
# Добавим в автозапуск
sudo systemctl enable confluence.service

# Остановим приложение
sudo systemctl stop confluence.service
```
(confluence-activation)=
### Активация

Существуют различные форки таблетки Atlassian Agent  продуктов Atlassian. на момент инструкции самая свежая
находится в репозитории [haxqer](https://github.com/haxqer/confluence/tree/master).

```{code-block} bash
# Скачиваем таблетку
wget https://github.com/haxqer/confluence/releases/download/vX.X.X/atlassian-agent.jar

sudo mkdir /opt/atlassian/atlassian-agent
sudo chown -R confluence:confluence /opt/atlassian/atlassian-agent
cp ./atlassian-agent.jar /opt/atlassian/atlassian-agent
```
Добавить в файл `/opt/atlassian/confluence/bin/setenv.sh` в самое начало строку:

```{code-block} bash
export JAVA_OPTS="-javaagent:/opt/atlassian/atlassian-agent/atlassian-agent.jar ${JAVA_OPTS}"
```

Запускаем приложение `sudo systemctl start confluence.service`

### Первичная настройка

После запуска открываем в браузере сервис (адрес вида `http://{IP}:8090`). Выбираем **Промышленная установка**.
Копируем значение Индентификатор сервера (вида `BZEK-UFBL-7CKO-I9IJ`). Генерируем ключ лицензии подставив индентификатор сервера:

```{code-block} bash
# Значения полей my@email.com, User, Company можно установтиь по желанию свои
java -jar /opt/atlassian/atlassian-agent/atlassian-agent.jar -d -mail 'my@email.com' -n User -o Company -p conf -s BZEK-UFBL-7CKO-I9IJ
```

Пример вывода

```{code-block} bash
====================================================
=======     Atlassian Crack Agent v1.3.1     =======
=======           https://zhile.io           =======
=======          QQ Group: 30347511          =======
====================================================

Your license code(Dont copy this line!!!): 

AAABsw0ODAoPeJyVkk2P2jAQhu/5FZF6TjYmuwmLZKlggoDw2UCrcqmcMBBvEyf1R7bZX18TQJWqX
jhYsiz5mXeemU87DfZcFzYKbK8/QP7gBdn7HbF7Xu/ZIgKoYhUfUwX48uJ4oYMCa8Ey4BJ2bQ0rW
gIm6+Uy+kJmw4UVNbTQ3Sd8ooUEawwyE6zuXva8YCVTcLSLK8FOWztXqpaDp6ePnBXgsspaizPlT
F4hpCpryluLg3Ib4ExpAW5W8VOhgWfgHiudGpgJ+KOmZ1BMFSBd4ApELZgErIQGi1Rc0UxFS8oKX
LafoTQXgymtW5AplTlekncyiV484aO3b8NErLzvweYYjxp6WE63+jDMt4lKx6Pzr+lbIw+xn4bxd
rLYzD8O0j9jbBm8KcypCRb9rplob+L6rxdxXvhgF4miwvRxE5mAaEDMxnh0iGJnPxktnJDEa2f2O
ps/CDaxKOkcXfX8hPYrCHnxjQLPC72+76MHmUYva266V7pMQaxPe2mo2EH3hfm/lI0WWU4l/Ltlt
9Hck/WsRKd/d6krlEQrbI6zQGEPIRQGPgqC5/u4u928ZPgDcLQBdTAsAhR9jtxbYQvCXwB0kxN+N
yGeNvZlGwIUdhWTcUwryd9a0lCb/AiME+2e4iM=X02ks
```
Копируем сгенерированный ключ и вставляем в браузере в поле Confluence. Далее настраиваем
подключение к БД которая ранее была подготовлена. Ожидаем инициализации системы - Готово

## Расширения

### Активация

Активировать можно любое расширение с помощью таблетки Atlassian Agent установленной в [этом разделе](#confluence-activation).
Для этого необходимо получить ключ приложения (например в панели администратора в свойствах самого расширения). Ключ приложения имеет вид
`com.mxgraph.confluence.plugins.diagramly` 

```{image} assets/img/conf_1.png
:class: bg-primary
:width: 500px
:align: center
```
далее использовать команду вида:

```{code-block} bash
# ID сервера BZEK-UFBL-7CKO-I9IJ установить свой а так же установить имя раширения (в примере это com.mxgraph.confluence.plugins.diagramly)
java -jar /opt/atlassian/atlassian-agent/atlassian-agent.jar -d -mail 'my@email.com' -n User -o Company -p com.mxgraph.confluence.plugins.diagramly -s BZEK-UFBL-7CKO-I9IJ
```
Полученный код активвации вставить в свойствах расширения в поле Ключ лицензии