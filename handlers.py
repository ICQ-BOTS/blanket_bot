from random import choice, randint
from tarantool_utils import space_photo, space_message, space_user, User
from config import *
import json
import os
import asyncio
import datetime
import datetime as DT
import time

async def start(bot, event):
	if event.type.value == 'callbackQuery':
		await bot.answer_callback_query(query_id=event.data['queryId'])
		await bot.edit_text(
			msg_id=event.data['message']['msgId'],
			chat_id=event.data['message']['chat']['chatId'],
			text='Привет.\nЭто твое одеяло. Я буду напоминать тебе каждый день, как я по тебе скучаю.',
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Подписаться на уведомления", "callbackData": "subscription"}],
				[{"text": "Отписаться от уведомлений", "callbackData": "formal_reply"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}]
			]))
		)
	else:			
		await bot.send_text(
			chat_id=event.data['chat']['chatId'],
			text='Привет.\nЭто твое одеяло. Я буду напоминать тебе каждый день, как я по тебе скучаю.',
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Подписаться на уведомления", "callbackData": "subscription"}],
				[{"text": "Отписаться от уведомлений", "callbackData": "formal_reply"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}]
			]))
		)


async def subscription(bot, event):
	await bot.answer_callback_query(query_id=event.data['queryId'])
	user = User(user_id=event.data['from']['userId'])
	if user.user[0][3]:
		await bot.edit_text(
			msg_id=event.data['message']['msgId'],
			chat_id=event.data['message']['chat']['chatId'],
			text="Вы уже подписались на уведомления от одеялка!",
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Отписаться от уведомлений", "callbackData": "formal_reply"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}],
				[{"text": "Главная", "callbackData": "main"}]
			]))
		)		
	else:
		await bot.edit_text(
			msg_id=event.data['message']['msgId'],
			chat_id=event.data['message']['chat']['chatId'],
			text="Вы подписались на уведомления от одеялка!",
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Отписаться от уведомлений", "callbackData": "formal_reply"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}],
				[{"text": "Главная", "callbackData": "main"}]
			]))
		)		
		d = datetime.datetime.today()
		if 10 <= d.hour <= 15:
			user.user[0][2] = random_time("%Y-%m-%d {}.{}.{}", hour=(int(d.hour) + 1, 17))
		else:
			user.user[0][2] = random_time("%Y-%m-%d {}.{}.{}", d=True)
		user.user[0][3] = True
		user.user[0][1] = True
		user.save()
			

def random_time(format_time, d=False, hour=(10, 17)):
	today = datetime.date.today()
	if d:
		today += datetime.timedelta(days=1)
	return today.strftime(format_time.format(randint(hour[0], hour[1]), randint(0, 59), randint(0, 59)))


async def rand_photo(bot, event):
	user = User(user_id=event.data['from']['userId'])
	await bot.answer_callback_query(query_id=event.data['queryId'])
	await bot.edit_text(
		msg_id=event.data['message']['msgId'],
		chat_id=event.data['message']['chat']['chatId'],
		text='https://files.icq.net/get/' + choice(space_photo.select())[1],
		inline_keyboard_markup="{}".format(json.dumps([
			[{"text": "Еще кровати", "callbackData": "rand_photo"}],
			[{"text": "Главная", "callbackData": "main"}]
		]))
	)


async def formal_reply(bot, event):
	await bot.answer_callback_query(query_id=event.data['queryId'])
	user = User(user_id=event.data['from']['userId'])
	if user.user[0][3]:
		await bot.edit_text(
			msg_id=event.data['message']['msgId'],
			chat_id=event.data['message']['chat']['chatId'],
			text="Вы были отписаны от уведомлений от одеялка!",
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Подписаться на уведомления", "callbackData": "subscription"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}],
				[{"text": "Главная", "callbackData": "main"}]
			]))
		)		
		user.user[0][3] = False
		user.user[0][1] = True
		user.save()
	else:
		await bot.edit_text(
			msg_id=event.data['message']['msgId'],
			chat_id=event.data['message']['chat']['chatId'],
			text="Вы до сих пор не подписаны на уведомлений от одеялка!",
			inline_keyboard_markup="{}".format(json.dumps([
				[{"text": "Подписаться на уведомления", "callbackData": "subscription"}],
				[{"text": "Посмотреть на кровати", "callbackData": "rand_photo"}],
				[{"text": "Главная", "callbackData": "main"}]
			]))
		)		
	

async def send_subscription(bot):
	try:
		while True:
			users = space_user.select()
			for user in users:
				if user[3]:
					# Переводим время в UNIX время.
					dt = DT.datetime.strptime(user[2], '%Y-%m-%d %H.%M.%S')
					if time.time() >= dt.timestamp():
						# Если будний день.
						if not int(datetime.datetime.today().isoweekday()) in [6, 7]:
							mes = space_message.select()
							rend_list = choice(mes)
							c = 0
							# Выбираем текст, который ещё не отправляли.
							while rend_list[0] in user[4]:
								rend_list = choice(mes)
								if c == len(mes):
									# Если отправили все текста из шаблона, то забываем что отправляли.
									user[4].clear()
									rend_list = choice(mes)
									break
								else:
									c += 1
							# Новая рандомное время.
							user[2] = random_time("%Y-%m-%d {}.{}.{}", d=True)
							user[4].append(rend_list[0])
							space_user.replace(user)
							await bot.send_text(
								chat_id=user[0],
								text=rend_list[1]
							)
							# Ждём, что бы не попасть под лимит, из за ограничение BOT ICQ API.
							await asyncio.sleep(1)
						else:
							user[2] = random_time("%Y-%m-%d {}.{}.{}", d=True)
							space_user.replace(user)
			# Ждём - что бы не мучать процессор.
			await asyncio.sleep(10)
	except Exception as e:
		raise e