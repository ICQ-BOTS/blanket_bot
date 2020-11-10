# Твоё одеяло

Старт:
1. Установка всех зависимостей 
```bash
pip install -r requirements.txt
```

2. Запуск space tarantool.
```bash
tarantoolctl start blanket.lua
```
> Файл из папки scheme нужно перекинуть в /etc/tarantool/instances.available

3. Запуск скрипта push_tarantool.py
```bash
python3 push_tarantool.py
```

4. Вставляем свои данные в config.ini - токен

5. Запуск бота!
```bash
python3 blanket_bot.py
```
