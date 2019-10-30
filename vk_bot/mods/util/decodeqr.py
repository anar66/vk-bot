import requests
from vk_bot.core.utils.modutil import BacisPlug
class Decodeqr(BacisPlug):
    doc = "Расшифровать qrcode"
    command = ["/decodeqr"]
    def main(self):
        try:
            image_url = self.event.object['attachments'][0]['photo']['sizes'][-1]['url']
            api = "http://api.qrserver.com/v1/read-qr-code/"
            params = {
                'fileurl' : image_url
            }
            r = requests.get(api, params=params)
            encode = r.json()
            if encode[0]['symbol'][0]["data"] == None:
                self.sendmsg("Не вижу здесь qrcode")
            else:
                self.sendmsg(encode[0]['symbol'][0]["data"])
        except:
            self.sendmsg("Мне нужно фото!")