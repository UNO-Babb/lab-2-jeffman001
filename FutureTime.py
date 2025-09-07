#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime
def main():
  print("Futuretime")
#getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5)
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hour = input("how many hours?:  ")
  #Ask user for minutes
  minutes = input("how many minutes?:  ")
  #Calculate the time after the user-supplied time has passed.
  futureMinute = (currentMinute + int(minutes)) % 60
  extraHour = (currentMinute + int(minutes)) // 60

  futurehour = (currentHour + int(hour) + extraHour) % 24
  #Do not use any if statements in calculating the time.
  print(str(futurehour) + ":" + str(futureMinute))
  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
