
# Твоё одеяло

[Твоё одеяло](https://icq.im/blanket_bot) <br>
<img src="https://github.com/ICQ-BOTS/blanket_bot/blob/main/blanket.png" width="100" height="100">


# Оглавление 
 - [Описание](https://github.com/ICQ-BOTS/mailru_im_async_bot#api)
 - [Установка](https://github.com/ICQ-BOTS/mailru_im_async_bot#установка)
 - [Скриншоты работы](https://github.com/ICQ-BOTS/mailru_im_async_bot#настройка)

# Описание
Это твое одеяло. Я буду напоминать тебе каждый день, как я по тебе скучаю.

# Установка

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

# Скриншоты работы
<img src="https://github.com/ICQ-BOTS/blanket_bot/blob/main/img/1.png" width="400">
<img src="https://github.com/ICQ-BOTS/blanket_bot/blob/main/img/2.png" width="400">
<img src="https://github.com/ICQ-BOTS/blanket_bot/blob/main/img/3.png" width="400">

