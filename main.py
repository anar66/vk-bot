import vk_api, requests, sys
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from token2 import token
from util import *
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if "text" in dir(event):
        text = event.text.split()
        try:
            zapros = text[0].lower()
        except IndexError:
            continue
            ConnectionError
        if zapros == "калькулятор":
            calc(vk, text, event)
        elif zapros == "погода":
            weather(vk, text, event)
        elif zapros == "привет" or zapros == "ку" or zapros == "споки":
            answer(vk, text,  event)
        elif zapros == "off" and event.user_id == 367919273:
            vk.messages.send(chat_id=event.chat_id, random_id=get_random_id(),
                             message="*выдернул свой шнур из розетки* Пааааака....~")
            sys.exit()
