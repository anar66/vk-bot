# GLaDOS (до освобождения от модулей)
## Гайд по запуску
### Зависимости
Напишите  в терминале от рута ```  pip install -r requirments.txt```, чтобы установить зависимости.  
А так же, через ваш пакетный менеджер поставьте ffmpeg   
В пипе не нашел, поэтому еще поставьте https://github.com/Nekos-life/nekos.py    
А еще запустите локально сервер memcached        
Добавьте в pythonpath путь к репе     
Например,  как можно сделать это в линуксе:
```
export PYTHONPATH=/home/$USER/GLaDOS
```
### Бд (mysql)
Поднимете msql аль его форки, в инете гайдов на это много
### config.env
заполните конфиг в vk_bot/config.env.example и переименуйте его в config.env
### Создание таблиц в бд
Запустите скрипт, по созданию всех нужных таблиц: ``` python vk_bot/createtabes.py ```
### Запуск
Для бота в группе python vk_bot/main2.py
Для страничного python vk_bot/main.py
### ???
PROFFIT!!!
/хелп  и в путь дорогу
## PS\ЗЫ
root без авы, который делает коммиты - это [данила](https://github.com/Ferowenso)

