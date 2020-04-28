import mysql.connector
import requests
if __name__ == "__main__":
    db_manager

token = "1238492927:AAFbniUq4oby9XtN3kuzxYpMnbmWWewG2hM"


class db_manager():
    __db = ""
    __cursor = ""

    def __init__(self, host, user, passwd, database, url):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.__URL = url
        self.__db = mysql.connector.connect(
            host=self.host, user=self.user, passwd=self.passwd)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def get_all_data(self):
        response = requests.get(self.__URL)
        return response.json()

    def save_all_data(self, data):
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID_19;")
        self.__cursor.execute("USE COVID_19;")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS CORONA (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), "
            "Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10), "
            "NewRecovered INT(10),TotalRecovered INT(10), Date VARCHAR(255))")

        for item in data["Countries"]:
            Country = item["Country"]
            Slug = item["Slug"]
            NewConfirmed = item["NewConfirmed"]
            TotalConfirmed = item["TotalConfirmed"]
            NewDeaths = item["NewDeaths"]
            TotalDeaths = item["TotalDeaths"]
            NewRecovered = item["NewRecovered"]
            TotalRecovered = item["TotalRecovered"]
            Date = item["Date"]
            self.__cursor = self.__db.cursor()
            sql = "INSERT INTO CORONA (Country,Slug,NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered,Date ) " \
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (Country, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            print(self.__cursor.rowcount, "Case added")

    def show_cases(self, data):
        self.__cursor.execute("USE COVID_19;")
        sql = "SELECT * FROM CORONA "
        self.__cursor.execute(sql)
        records = self.__cursor.fetchall()
        for item in records:
            print("Country = ", item[0])
            print("Slug = ", item[1])
            print("NewConfirmed == ", item[2])
            print("TotalConfirmed == ", item[3])
            print("NewDeaths == ", item[4])
            print("TotalDeaths == ", item[5])
            print("NewRecovered == ", item[6])
            print("TotalRecovered == ", item[7])
            print("Date == ", item[8])

    def show_cases_by_country(self, data, country):
        self.__cursor.execute("USE COVID_19;")
        sql = "SELECT * FROM CORONA WHERE Country = '" + country + "'"
        self.__cursor.execute(sql)
        myresult = self.__cursor.fetchall()
        return myresult
