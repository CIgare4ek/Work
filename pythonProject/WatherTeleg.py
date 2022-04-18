from pyowm import OWM
import telebot

owm = OWM('bea3a86964e0b0e3e38b675d924fa732')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5133853760:AAGxthdMjT3c_YnLiX-QYifp-T2ISBI1LoI", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = observation.weather.temperature('celsius')['temp']

    answer = "В місті: " + message.text + " зараз " + str(w.detailed_status) + "\n"
    answer += "Температура повітря: " +  str(temp) + "\n\n"

    if temp < 2:
        answer += "Необхідно одягатися дуже тепло!"
    elif temp < 10:
        answer += "Радимо одягнути куртку"
    else:
        answer += "Комфортна погода, одягайтеся як бажаєте"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )


