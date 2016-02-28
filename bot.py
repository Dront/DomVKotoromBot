#! /usr/bin/env python
# *- coding: utf-8 -*

import time
import random
import logging
import telepot

TOKEN = '124808497:AAHsfAEGi0bxr4c0wKRXlIbGL8wQL9rKs0k'

msgs = [
    'Самая неприятная тишина там, где много людей молчат.',
    '— Я красивый, — сказал урод и заплакал…\n'
    '— А я урод, — сказал другой урод и засмеялся…',
    'Если бы ты так не зацикливался на том, что тебя никто не понимает, может, у тебя хватило бы сил понять других.',
    '— Ладно, — сказал он. — Забудем того тебя, который живет в зеркале.\n'
    '— По-твоему, это не я?\n'
    '— Ты. Но не совсем. Это ты, искаженный собственным восприятием. В зеркалах мы все хуже, чем на самом деле, не замечал?',
    'Слова, которые сказаны, что-то означают, даже если ты ничего не имел в виду.',
    'Любовь съела тебя. Первое, что она пожирает - мозги, учти.',
    '— Он вообще никогда не смотрится в зеркало\n'
    '— Почему? Если бы я видел в зеркале то, что видит он...\n'
    '— Откуда ты знаешь, что он там видит?',
    'Музыка - прекрасный способ стирания мыслей, плохих и не очень, самый лучший и самый древний.',
    'Я знаю красивейшего человека, который шарахается от зеркал, как от чумы. \nЯ знаю девушку, которая носит на шее целую коллекцию маленьких зеркал. Она чаще глядит в них, чем вокруг, и видит все фрагментами, в перевернутом виде.\nЯ знаю незрячего, иногда настороженно замирающего перед собственным отражением. \nТак что пусть мне не говорят, что в зеркалах не прячется магия.',
    'Когда кто-то долго роет яму, потом тщательно устанавливает на дне острые колья и, наконец, с радостным воплем туда прыгает, я называю это самоубийством.',
    'Это было очень правильное слово, поймав его, я понял, что давно искал что-то в этом роде. Слово, в котором пряталась бы разгадка происходящего в Доме. Просто надо было осознать что игра — это все, что меня окружает.',
    'Нет человека счастливее, чем настоящий дурак.',
    'Свитера на случай холода. Еда на случай голода. Оружие на случай внезапностей, - объясняет Табаки. - В ночную жизнь налегке не уходят, дурачок!',
    'Бывают на свете такие люди. А может, вид у них такой. Они редко, но встречаются, люди, у которых не бывает проблем. Которые так себя ведут, как будто у них нет проблем.',
    '— Я не спиваюсь, — обижается Лорд. — Я лечусь.',
]

commands = [
    '/one',
    '/all'
]

help_text = '/help - Показать этот текст\n\
/one - Отправить случайную цитату\n\
/all - Отправить все цитаты'

shutdown = False


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    logging.info('ctype: {}, chat type: {}, id: {}'.format(content_type, chat_type, chat_id))

    try:
        command = msg['text'].strip()
    except KeyError:
        logging.info('Msg contains no text')
        return

    logging.info('Command: %s', command)
    if command == commands[0]:
        text = random.choice(msgs)
    elif command == commands[1]:
        text = '\n\n'.join(msgs)
    else:
        text = help_text

    chat_id = msg['from']['id']
    show_keyboard = {'keyboard': [['/all', '/one']]}
    bot.sendMessage(chat_id, text, reply_markup=show_keyboard)


def config_log(
        console_level=logging.DEBUG,
        console_format='%(levelname)-5s: %(asctime)s: %(message)s',
        file_level=logging.DEBUG,
        folder='logs',
        file_format='%(levelname)-5s: %(asctime)s: %(message)s',
        date_format='%X',
        filename_format="%d.%m.%y %X"):

    import time
    import os

    filename = time.strftime(filename_format, time.localtime()) + '.log'
    filename = os.path.join(folder, filename)
    logging.basicConfig(
        level=file_level,
        format=file_format,
        datefmt=date_format,
        filename=filename,
        filemode='wa')
    # Handler which writes to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(console_level)
    formatter = logging.Formatter(console_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


if __name__ == '__main__':
    config_log(console_level=logging.INFO, file_level=logging.DEBUG)
    bot = telepot.Bot(TOKEN)
    logging.info('The Bot: %s', bot.getMe())
    bot.notifyOnMessage(handle)
    logging.info('Listening ...')

    while not shutdown:
        time.sleep(1)

    logging.info('Stopped!')
