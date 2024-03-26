from image import newtweett
from gemini import get_tweet
import telebot

bot = telebot.TeleBot("6064570542:AAElcStNmpmmRwfcClBjTMHT7SJiJ9442xU")


@bot.message_handler(content_types=['text'])
def getText(msg):
    print(msg.chat)
    try:
        tweet = get_tweet()
        while (tweet.find('masculinesage')  == -1 and len(tweet) < 50):
            tweet = get_tweet()
        newtweett(tweet)
        with open('tweet.png', 'rb') as f:
            bot.send_photo(msg.chat.id, f)
    except Exception as e:
        print(e)
        bot.send_message(msg.chat.id, str(e))


bot.infinity_polling()
# tweet = get_tweet()
# print(len(tweet))
# print(tweet)
# while (tweet.find('masculinesage')  != -1):
#     tweet = get_tweet()
#     print(len(tweet))
#     print(tweet)
# newtweett(tweet)
