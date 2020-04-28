from lib.db_manager import db_manager, token
from lib.settings import *
import telebot
__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, database, __URL)
covid_19_data = db_object.get_all_data()


def menu():
    exit = False
    while not exit:
        choice = int(
            input("1.Update covid19 database\n2.Show all cases\n3.Show cases by country\n0.Exit \n===>"))
        if choice == 1:
            db_object.save_all_data(covid_19_data)
        elif choice == 2:
            db_object.show_cases(covid_19_data)
        elif choice == 3:
            country = input("Enter your country : ")
            myresult = db_object.show_cases_by_country(covid_19_data, country)
            for item in myresult:
                print("Country = ", item[1])
                print("Slug = ", item[2])
                print("NewConfirmed == ", item[3])
                print("TotalConfirmed == ", item[4])
                print("NewDeaths == ", item[5])
                print("TotalDeaths == ", item[6])
                print("NewRecovered == ", item[7])
                print("TotalRecovered == ", item[8])
                print("Date == ", item[9])
        elif choice == 0:
            exit = True
            print("Bye...")


# menu()


bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    country = message.text
    myresult = db_object.show_cases_by_country(covid_19_data, country)
    print(myresult)
    if message.text == country:
        for item in myresult:
            bot.send_message(message.from_user.id, "Information about Coronavirus in the world  [𝐂𝐎𝐕𝐈𝐃-19]\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"+"\nCountry → " + str(item[1]) +
                             "\nNumber of diseases  → " + str(item[4]) + "\nNumber of diseases in one day  → " + str(item[5]) + "\nNumber of deaths  → " + str(item[6]) + "\nNumber of deaths in one day → " + str(item[5]) + "\nNumber of cured  → " + str(item[8]) + "\nNumber of cured in one day → " + str(item[7]))


bot.polling(none_stop=True)
