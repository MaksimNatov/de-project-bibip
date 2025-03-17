# de-project-bibip


## Настройка среды разработки

Рекомендуем использовать редактор [Visual Studio Code](https://code.visualstudio.com/).

vscode при запуске импортируем переменные среды из файла `.env` и запускаем отладку.

Чтобы в редакторе работала подсветка импортов, а при запуске все зависимости корректно подтягивались, создайте файл `.env` в корне проекта и добавьте в него следующие строки:
```bash
PYTHONPATH="$PYTHONPATH:full_path_to_src_folder_in_project"
```
где full_path_to_src_folder_in_project - полный путь до каталога src.

Этой командой вы добавляете каталог src в переменную окружения PYTHONPATH, чтобы python мог найти все модули в проекте.

После того, как вы создали файл `.env`, перезапустите vscode. Все импорты должны подсвечиваться корректно.


## Запуск тестов в консоли

Если вы хотите запустить тесты в консоли, вам так же нужно добавить переменную окружения PYTHONPATH. Для этого выполните следующие команды:
```bash
export PYTHONPATH=$PYTHONPATH:full_path_to_src_folder_in_project
```
где full_path_to_src_folder_in_project - полный путь до каталога src.

После этого вы можете запустить тесты:
```bash
cd de-project-bibip # переходим в каталог проекта
pytest tests # запускаем тесты
```

## Запуск проекта в докере

Если вы не сталкивались с докером, просто проигнорируйте файлы `Dockerfile` и `docker-compose.yml`. Вы еще познакомитесь с докером, дальше на курсе.

Если вы предпочитаете разрабатывать в докере, то вам нужно выполнить следующие команды:
```bash
cd de-project-bibip
docker compose up -d --build
```

После завершения работы остановите контейнер:
```bash
docker compose down -v
```

