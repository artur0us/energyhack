#! /usr/bin/env python
# -*- coding: utf-8 -*-

# unread, sort, id_more_than, id_less_than, page, per, search, updated
# @bot.message_handler(func = lambda message: message.text='All notifications')
# .encode(sys.stdout.encoding, errors='replace')

import threading
import json
import time
import os
import telebot
from telebot import types
from telebot.types import LabeledPrice
from	 telebot.types import ShippingOption
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
bot 	= telebot.AsyncTeleBot(BOT_TOKEN)

users = {0: {'stage': 0, 'login': 'a'}}
database = json.load(open('db/accounts.json', 'r'))['Users']


def logOn(login, password):
	for i in range(0, len(database)):
		if database[i][0] == login:
			if database[i][1] == password:
				print 'success'
				return True
	print 'failed'
	return False

def userCheckStage(chat_id, stage):
	result = False
	try:
		result = (users.get(chat_id).get('stage') == stage)
	except:
		print str(chat_id), str(stage)
	return result

# START
@bot.message_handler(commands=['start'])
def start_command(message):
	users[message.chat.id] = {'stage': 0, 'login': ''}
	for user in users:
		print user
	bot.send_message(message.chat.id, 'Здравствуйте! Пожалуйста, введите номер договора:')

@bot.message_handler(func = lambda message: message.text != None)
def text_handler(message):
	if userCheckStage(message.chat.id, 0):
		users[message.chat.id]['stage'] = 1
		users[message.chat.id]['login'] = message.text
		bot.send_message(message.chat.id, 'Введите пароль:')
	elif userCheckStage(message.chat.id, 1):
		if logOn(users.get(message.chat.id).get('login'), message.text):
			keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
			button1 = types.KeyboardButton(text = "Обновить")
			button2 = types.KeyboardButton(text = "Оплатить")
			keyboard.add(button1, button2)
			users[message.chat.id]['stage'] = 2
			data = None
			for i in range(len(database)):
				print database[i][0]
				print users[message.chat.id]
				if database[i][0] == users[message.chat.id]['login']:
					data = database[i][2]
					break
			print unicode(data[0])
			mess = 'ФИО\n' + str(data[0]) + '\nДата рождения\n' + str(data[1]) + '\nГород\n' + str(data[2]) + '\nАдрес\n' + str(data[3]) + '\nПотребление/месяц\n' + str(data[4]) + '\nСэкономлено\n' + str(data[5]) + '\nАвтооплата\n' + str(data[6])
			bot.send_message(chat_id = message.chat.id, text = mess, reply_markup = keyboard)
			#bot.send_message(chat_id=message.chat.id, text=currentMsg, reply_markup = keyboard)
		else:
			users[message.chat.id]['stage'] = 0
			bot.send_message(message.chat.id, 'Неверный логин или пароль')
			bot.send_message(message.chat.id, 'Здравствуйте! Пожалуйста, введите номер договора:')
	elif userCheckStage(message.chat.id, 2):
		if message.text == 'Обновить':
			keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
			button1 = types.KeyboardButton(text = "Обновить")
			button2 = types.KeyboardButton(text = "Оплатить")
			keyboard.add(button1, button2)
			users[message.chat.id]['stage'] = 2
			data = None
			for i in range(0, len(database)):
				if database[i][0] == users[message.chat.id]['login']:
					data = database[i][2]
			mess = 'ФИО\n' + str(data[0]) + '\nДата рождения\n' + str(data[1]) + '\nГород\n' + str(data[2]) + '\nАдрес\n' + str(data[3]) + '\nПотребление/месяц\n' + str(data[4]) + '\nСэкономлено\n' + str(data[5]) + '\nАвтооплата\n' + str(data[6])
			bot.send_message(chat_id = message.chat.id, text = mess, reply_markup = keyboard)
		elif message.text == 'Оплатить':
			keyboard = types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True)
			button1 = types.KeyboardButton(text = "Обновить")
			button2 = types.KeyboardButton(text = "Оплатить")
			keyboard.add(button1, button2)
			users[message.chat.id]['stage'] = 2
			data = None
			for i in range(0, len(database)):
				if database[i][0] == users[message.chat.id]['login']:
					data = database[i][2]
			global PROVIDER_TOKEN
			print int(data[7][0:-15])
			bot.send_invoice(message.chat.id, title = 'Оплатить задолженность',
				description		= data[7],
				provider_token 	= PROVIDER_TOKEN,
				currency		= 'rub',
				photo_url		= 'https://image.flaticon.com/icons/png/512/189/189093.png',
				photo_height=100,
				photo_width=100,
				photo_size=100,
				is_flexible		= False,
				prices			= [LabeledPrice(data[7], int(data[7][0:-15]))],
				start_parameter	= 'ITEM',
				invoice_payload	= 'item')

# INLINE BUTTONS
@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
	SetBotActiveStatus()
	if call.message:
		pass

print("[i] Initializing telegram-bot...")
bot.polling(none_stop = True)

