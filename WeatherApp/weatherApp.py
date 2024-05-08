from tkinter import *
from geopy import Photon
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather Application")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)


def get_default():
    geolocator = Photon(user_agent="weatherApp")
    location = geolocator.geocode("wroclaw")

    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timeZone.config(text=result)

    longLat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 1)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # Create weather forecast apr with api key from home.openweathermap.org
    api = ("https://api.openweathermap.org/data/3.0/onecall?lat=" + str(location.latitude) +
           "&lon=" + str(location.longitude) + "&units=metric&exclude=hourly&appid=30e73567a6988acdea1ef26dd0b42c4c")

    json_data = requests.get(api).json()

    # Get current information
    temperature = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    t.config(text=(temperature, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description) 

    # Inserting images for weather conditions
    first_day_image = json_data['daily'][0]['weather'][0]['icon']
    second_day_image = json_data['daily'][1]['weather'][0]['icon']
    third_day_image = json_data['daily'][2]['weather'][0]['icon']
    fourth_day_image = json_data['daily'][3]['weather'][0]['icon']
    fifth_day_image = json_data['daily'][4]['weather'][0]['icon']
    sixth_day_image = json_data['daily'][5]['weather'][0]['icon']
    seventh_day_image = json_data['daily'][6]['weather'][0]['icon']

    # Importing pictures displaying different weather conditions
    # First day
    photo1 = ImageTk.PhotoImage(file=f"files/{first_day_image}@2x.png")
    firstImage.config(image=photo1)
    firstImage.image = photo1
    temp_day1 = json_data['daily'][0]['temp']['day']
    temp_night1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day: {round(temp_day1)} °C\n Night: {round(temp_night1)} °C")

    # Second day
    img = (Image.open(f"files/{second_day_image}@2x.png"))
    resized_img = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_img)
    secondImage.config(image=photo2)
    secondImage.image = photo2
    temp_day2 = json_data['daily'][1]['temp']['day']
    temp_night2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day: {round(temp_day2)} °C\n Night: {round(temp_night2)} °C")

    # Third day
    img2 = (Image.open(f"files/{third_day_image}@2x.png"))
    resized_img2 = img2.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_img2)
    thirdImage.config(image=photo3)
    thirdImage.image = photo3
    temp_day3 = json_data['daily'][2]['temp']['day']
    temp_night3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day: {round(temp_day3)} °C\n Night: {round(temp_night3)} °C")

    # Fourth day
    img3 = (Image.open(f"files/{fourth_day_image}@2x.png"))
    resized_img3 = img3.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_img3)
    fourthImage.config(image=photo4)
    fourthImage.image = photo4
    temp_day4 = json_data['daily'][3]['temp']['day']
    temp_night4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day: {round(temp_day4)} °C\n Night: {round(temp_night4)} °C")

    # Fifth day
    img4 = (Image.open(f"files/{fifth_day_image}@2x.png"))
    resized_img4 = img4.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_img4)
    fifthImage.config(image=photo5)
    fifthImage.image = photo5
    temp_day5 = json_data['daily'][4]['temp']['day']
    temp_night5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day: {round(temp_day5)} °C\n Night: {round(temp_night5)} °C")

    # Sixth day
    img5 = (Image.open(f"files/{sixth_day_image}@2x.png"))
    resized_img5 = img5.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_img5)
    sixthImage.config(image=photo6)
    sixthImage.image = photo6
    temp_day6 = json_data['daily'][5]['temp']['day']
    temp_night6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day: {round(temp_day6)} °C\n Night: {round(temp_night6)} °C")

    # Seventh day
    img6 = (Image.open(f"files/{seventh_day_image}@2x.png"))
    resized_img6 = img6.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_img6)
    seventhImage.config(image=photo7)
    seventhImage.image = photo7
    temp_day7 = json_data['daily'][6]['temp']['day']
    temp_night7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day: {round(temp_day7)} °C\n Night: {round(temp_night7)} °C")

    # Get day information
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


def get_weather():

    city = textfield.get()

    if city != "":
        geolocator = Photon(user_agent="weatherApp")
        location = geolocator.geocode(city)

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        timeZone.config(text=result)

        longLat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 1)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)

        # Create weather forecast apr with api key from home.openweathermap.org
        api = ("https://api.openweathermap.org/data/3.0/onecall?lat=" + str(location.latitude) +
               "&lon=" + str(
                    location.longitude) + "&units=metric&exclude=hourly&appid=30e73567a6988acdea1ef26dd0b42c4c")

        json_data = requests.get(api).json()

        # Get current information
        temperature = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']

        t.config(text=(temperature, "°C"))
        h.config(text=(humidity, "%"))
        p.config(text=(pressure, "hPa"))
        w.config(text=(wind, "m/s"))
        d.config(text=description)

        # Inserting images for weather conditions
        first_day_image = json_data['daily'][0]['weather'][0]['icon']
        second_day_image = json_data['daily'][1]['weather'][0]['icon']
        third_day_image = json_data['daily'][2]['weather'][0]['icon']
        fourth_day_image = json_data['daily'][3]['weather'][0]['icon']
        fifth_day_image = json_data['daily'][4]['weather'][0]['icon']
        sixth_day_image = json_data['daily'][5]['weather'][0]['icon']
        seventh_day_image = json_data['daily'][6]['weather'][0]['icon']

        # Importing pictures displaying different weather conditions
        # First day
        photo1 = ImageTk.PhotoImage(file=f"files/{first_day_image}@2x.png")
        firstImage.config(image=photo1)
        firstImage.image = photo1
        temp_day1 = json_data['daily'][0]['temp']['day']
        temp_night1 = json_data['daily'][0]['temp']['night']
        day1temp.config(text=f"Day: {round(temp_day1)} °C\n Night: {round(temp_night1)} °C")

        # Second day
        img = (Image.open(f"files/{second_day_image}@2x.png"))
        resized_img = img.resize((50, 50))
        photo2 = ImageTk.PhotoImage(resized_img)
        secondImage.config(image=photo2)
        secondImage.image = photo2
        temp_day2 = json_data['daily'][1]['temp']['day']
        temp_night2 = json_data['daily'][1]['temp']['night']
        day2temp.config(text=f"Day: {round(temp_day2)} °C\n Night: {round(temp_night2)} °C")

        # Third day
        img2 = (Image.open(f"files/{third_day_image}@2x.png"))
        resized_img2 = img2.resize((50, 50))
        photo3 = ImageTk.PhotoImage(resized_img2)
        thirdImage.config(image=photo3)
        thirdImage.image = photo3
        temp_day3 = json_data['daily'][2]['temp']['day']
        temp_night3 = json_data['daily'][2]['temp']['night']
        day3temp.config(text=f"Day: {round(temp_day3)} °C\n Night: {round(temp_night3)} °C")

        # Fourth day
        img3 = (Image.open(f"files/{fourth_day_image}@2x.png"))
        resized_img3 = img3.resize((50, 50))
        photo4 = ImageTk.PhotoImage(resized_img3)
        fourthImage.config(image=photo4)
        fourthImage.image = photo4
        temp_day4 = json_data['daily'][3]['temp']['day']
        temp_night4 = json_data['daily'][3]['temp']['night']
        day4temp.config(text=f"Day: {round(temp_day4)} °C\n Night: {round(temp_night4)} °C")

        # Fifth day
        img4 = (Image.open(f"files/{fifth_day_image}@2x.png"))
        resized_img4 = img4.resize((50, 50))
        photo5 = ImageTk.PhotoImage(resized_img4)
        fifthImage.config(image=photo5)
        fifthImage.image = photo5
        temp_day5 = json_data['daily'][4]['temp']['day']
        temp_night5 = json_data['daily'][4]['temp']['night']
        day5temp.config(text=f"Day: {round(temp_day5)} °C\n Night: {round(temp_night5)} °C")

        # Sixth day
        img5 = (Image.open(f"files/{sixth_day_image}@2x.png"))
        resized_img5 = img5.resize((50, 50))
        photo6 = ImageTk.PhotoImage(resized_img5)
        sixthImage.config(image=photo6)
        sixthImage.image = photo6
        temp_day6 = json_data['daily'][5]['temp']['day']
        temp_night6 = json_data['daily'][5]['temp']['night']
        day6temp.config(text=f"Day: {round(temp_day6)} °C\n Night: {round(temp_night6)} °C")

        # Seventh day
        img6 = (Image.open(f"files/{seventh_day_image}@2x.png"))
        resized_img6 = img6.resize((50, 50))
        photo7 = ImageTk.PhotoImage(resized_img6)
        seventhImage.config(image=photo7)
        seventhImage.image = photo7
        temp_day7 = json_data['daily'][6]['temp']['day']
        temp_night7 = json_data['daily'][6]['temp']['night']
        day7temp.config(text=f"Day: {round(temp_day7)} °C\n Night: {round(temp_night7)} °C")

        # Get day information
        first = datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first + timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first + timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first + timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first + timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth = first + timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))

        seventh = first + timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))


# Icon
image_icon = PhotoImage(file="files/logo.png")
root.iconphoto(False, image_icon)

scale_w = 2
scale_h = 1
Round_box = PhotoImage(file="files/Rounded+Rectangle+1.png").zoom(scale_w, scale_h)
Label(root, image=Round_box, bg="#57adff", border=0).place(x=-100, y=115)

# creating label for different weather parameters
label1 = Label(root, text="Temperature", font=("Helvetice", 11), fg="white", bg="#203243")
label1.place(x=40, y=120)

label2 = Label(root, text="Humidity", font=("Helvetice", 11), fg="white", bg="#203243")
label2.place(x=40, y=140)

label3 = Label(root, text="Pressure", font=("Helvetice", 11), fg="white", bg="#203243")
label3.place(x=40, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetice", 11), fg="white", bg="#203243")
label4.place(x=40, y=180)

label5 = Label(root, text="Description", font=("Helvetice", 11), fg="white", bg="#203243")
label5.place(x=40, y=200)

# Creating a search box
Search_image = PhotoImage(file="files/Rounded+Rectangle+3.png")
myImage = Label(image=Search_image, bg="#57adff")
myImage.place(x=350, y=140)

Weather_image = PhotoImage(file="files/Layer+7.png")
weatherImage = Label(root, image=Weather_image, bg="#203243")
weatherImage.place(x=370, y=147)

textfield = Entry(root, justify='center', width=15, font=("poppins", 25, 'bold'), bg="#203243", border=0, fg='white')
textfield.insert(0, "Wroclaw")
textfield.place(x=450, y=150)
textfield.focus()

Search_icon = PhotoImage(file="files/Layer+6.png")
searchIcon = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg="#203243", command=get_weather)
searchIcon.place(x=725, y=145)

# Creating bottom boxes
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstBox = PhotoImage(file="files/Rounded+Rectangle+2.png")
secondBox = PhotoImage(file="files/Rounded+Rectangle+2+copy.png")

Label(frame, image=firstBox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=800, y=30)

# Creating a clock with the current timezone
clock = Label(root, font=("Helvetica", 30, 'bold'), fg='white', bg="#57adff")
clock.place(x=50, y=30)

# Creating a label for the timezone
timeZone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timeZone.place(x=650, y=20)

# Creating a label for the longitude and latitude for the search location
longLat = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
longLat.place(x=650, y=50)

# Create labels for weather details
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=140, y=120)

h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=140, y=140)

p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=140, y=160)

w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=140, y=180)

d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=140, y=200)

# Generating main cell
mainFrame = Frame(root, width=230, height=132, bg="#282829")
mainFrame.place(x=35, y=315)

day1 = Label(mainFrame, font="arial 15", bg="#282829", fg="#fff")
day1.place(x=115, y=5)

firstImage = Label(mainFrame, bg="#282829")
firstImage.place(x=1, y=15)

day1temp = Label(mainFrame, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

# Generating first small cell
firstFrame = Frame(root, width=70, height=115, bg="#282829")
firstFrame.place(x=305, y=325)

day2 = Label(firstFrame, font="arial 8", bg="#282829", fg="#fff")
day2.place(x=5, y=1)

secondImage = Label(firstFrame, bg="#282829")
secondImage.place(x=7, y=20)

day2temp = Label(firstFrame, bg="#282829", fg="#57adff")
day2temp.place(x=2, y=70)

# Generating second small cell
secondFrame = Frame(root, width=70, height=115, bg="#282829")
secondFrame.place(x=405, y=325)

day3 = Label(secondFrame, font="arial 8", bg="#282829", fg="#fff")
day3.place(x=5, y=1)

thirdImage = Label(secondFrame, bg="#282829")
thirdImage.place(x=7, y=20)

day3temp = Label(secondFrame, bg="#282829", fg="#57adff")
day3temp.place(x=2, y=70)

# Generating third small cell
thirdFrame = Frame(root, width=70, height=115, bg="#282829")
thirdFrame.place(x=505, y=325)

day4 = Label(thirdFrame, font="arial 8", bg="#282829", fg="#fff")
day4.place(x=5, y=1)

fourthImage = Label(thirdFrame, bg="#282829")
fourthImage.place(x=7, y=20)

day4temp = Label(thirdFrame, bg="#282829", fg="#57adff")
day4temp.place(x=2, y=70)

# Generating fourth small cell
fourthFrame = Frame(root, width=70, height=115, bg="#282829")
fourthFrame.place(x=605, y=325)

day5 = Label(fourthFrame, font="arial 8", bg="#282829", fg="#fff")
day5.place(x=5, y=1)

fifthImage = Label(fourthFrame, bg="#282829")
fifthImage.place(x=7, y=20)

day5temp = Label(fourthFrame, bg="#282829", fg="#57adff")
day5temp.place(x=2, y=70)

# Generating fifth small cell
fifthFrame = Frame(root, width=70, height=115, bg="#282829")
fifthFrame.place(x=705, y=325)

day6 = Label(fifthFrame, font="arial 8", bg="#282829", fg="#fff")
day6.place(x=5, y=1)

sixthImage = Label(fifthFrame, bg="#282829")
sixthImage.place(x=7, y=20)

day6temp = Label(fifthFrame, bg="#282829", fg="#57adff")
day6temp.place(x=2, y=70)

# Generating sixth small cell
sixthFrame = Frame(root, width=70, height=115, bg="#282829")
sixthFrame.place(x=805, y=325)

day7 = Label(sixthFrame, font="arial 8", bg="#282829", fg="#fff")
day7.place(x=5, y=1)

seventhImage = Label(sixthFrame, bg="#282829")
seventhImage.place(x=7, y=20)

day7temp = Label(sixthFrame, bg="#282829", fg="#57adff")
day7temp.place(x=2, y=70)

get_default()

mainloop()
