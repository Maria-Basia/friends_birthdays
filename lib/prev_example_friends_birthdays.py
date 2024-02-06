from datetime import datetime 

class Friends(): 

    def __init__(self): 
        self.records = {}
        self.cards_sent = {}
        self.date_today = datetime.today()
    
    def add(self, friend, date): 
        if friend in self.records: 
            return "That name already exists"
        self.records[friend] = date
        self.cards_sent[friend] = False
        
    def new_birthday(self, friend, date): 
        self.records[friend] = date

    def birthday_reminder(self): 
        upcoming = []
        for friend in self.records: 
            birthday = datetime.strptime(self.records[friend], "%d/%m/%Y").replace(year=datetime.today().year)
            difference = (birthday - self.date_today).days
            if difference < 0 or difference > 14:
                continue 
            else: 
                upcoming.append(f"{friend}: {self.records[friend]}")
        return upcoming
            

    def upcoming_age_check(self, friend):
        birthday_this_year = datetime.strptime(self.records[friend], "%d/%m/%Y").replace(year=datetime.today().year)
        birthday = datetime.strptime(self.records[friend], "%d/%m/%Y")
        upcoming_age = (birthday_this_year - birthday).days // 365
        return upcoming_age

    def card_sent(self, friend):
        self.cards_sent[friend] = True
    
    def birthday_card_tracker(self):
        for friend in self.records:
            birthday_this_year = datetime.strptime(self.records[friend], "%d/%m/%Y").replace(year=datetime.today().year)
            if self.cards_sent[friend] == True and birthday_this_year < self.date_today:
                self.cards_sent[friend] = False
        return self.cards_sent
    
    



# YOU COULD TRY REFACTORING THE CODING FOR AGE WITH THE DATEUTIL MODULE (SEE BELOW)
# NOTE: This is code relating to a different challenge relating to an age check if under 16, but the relevant code is on line 76


import re
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Info on importing dateutil from here:
# https://www.influxdata.com/blog/guide-dateutil-module-python/#:~:text=The%20dateutil%20module%20is%20not,normally%20use%20other%20Python%20modules.

# Info on using re.match
# https://www.guru99.com/python-regular-expressions-complete-tutorial.html

# Convert age to years using dateutil relativedelta
# https://stackoverflow.com/questions/32083726/how-do-i-convert-days-into-years-and-months-in-python



def age_check(date):
    if type(date) is not str:
        raise Exception("Incorrect type")
    format = (r'^\d{4}-\d{2}-\d{2}$')
    if bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date)) == False:
        raise Exception("Incorrect date format")
    print(re.match(r'^\d{4}-\d{2}-\d{2}$', date))

    age = (relativedelta(datetime.now(), datetime.strptime(date, '%Y-%m-%d'))).years
    # age = (datetime.now() - datetime.strptime(date, '%Y-%m-%d')).days // 365
    print(age)
    if age < 16:
        return f"access denied! you are {age} years old and need to be 16"
    return "access granted!"