<img src="https://github.com/ICQ-BOTS/blanket_bot/blob/main/blanket.png" width="100" height="100">

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
# Твоё одеяло

[Твоё одеяло](https://icq.im/blanket_bot)

Старт:
1. Установка всех зависимостей 
```bash
pip3 install -r requirements.txt
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
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
