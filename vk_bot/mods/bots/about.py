from vk_bot.core.modules.basicplug import BasicPlug
from vk_bot import mods
from boltons import iterutils
class AboutBot(BasicPlug):
    doc = "Инфа о боте"
    command = ["/оботе"]
    def main(self):
        info = """
        бот написан на python, двумя прогерами
        первый прогер: *slava_a_i_r
        второй прогер: *pythonoglot
        модуль на распознавание гс написал: *feelan03
        Так же, он опенсурс, репа: github.com/anar66/vk-bot
        Приятного пользования~
        Узнать команды: /хелп
        """
        self.sendmsg(info)
