from vk_bot.core.modules.basicplug import BacisPlug
class Test2(BacisPlug):
    doc = "первый модуль, тест"
    types = 'commandb'
    @staticmethod
    def getcommand(uid, text):
        return "/тест"
    def main(self):
        self.sendmsg(self.text[0])
