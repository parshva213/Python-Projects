#5.struct
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking App")

        # Create main frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(pady=10)

        self.booking_frame = tk.Frame(self.main_frame)
        self.booking_frame.pack(pady=10)

        self.exit_frame = tk.Frame(self.main_frame)
        self.exit_frame.pack(pady=10)

        # Create flight data
        self.flights = [
            {"number": "AI101", "from": "Delhi", "to": "Mumbai", "time": "09:00"},
            {"number": "AI102", "from": "Mumbai", "to": "Delhi", "time": "11:00"},
            {"number": "AI103", "from": "Delhi", "to": "Bangalore", "time": "13:00"},
            {"number": "AI104", "from": "Bangalore", "to": "Delhi", "time": "15:00"},
            {"number": "AI105", "from": "Delhi", "to": "Hyderabad", "time": "17:00"},
            {"number": "AI106", "from": "Hyderabad", "to": "Delhi", "time": "19:00"},
            {"number": "UK987", "from": "Mumbai", "to": "Chennai", "time": "09:00"},
            {"number": "UK988", "from": "Chennai", "to": "Mumbai", "time": "11:00"},
            {"number": "SG123", "from": "Delhi", "to": "Kolkata", "time": "13:00"},
            {"number": "SG124", "from": "Kolkata", "to": "Delhi", "time": "15:00"},
        ]

        # Create search frame widgets
        self.search_label = tk.Label(self.search_frame, text="Search Flights")
        self.search_label.pack()

        self.from_label = tk.Label(self.search_frame, text="From:")
        self.from_label.pack(side=tk.LEFT)

        self.from_var = tk.StringVar()
        self.from_entry = ttk.Combobox(self.search_frame, textvariable=self.from_var)
        self.from_entry['values'] = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata']
        self.from_entry.pack(side=tk.LEFT)

        self.to_label = tk.Label(self.search_frame, text="To:")
        self.to_label.pack(side=tk.LEFT)

        self.to_var = tk.StringVar()
        self.to_entry = ttk.Combobox(self.search_frame, textvariable=self.to_var)
        self.to_entry['values'] = ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata']
        self.to_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_flights)
        self.search_button.pack(side=tk.LEFT)

        # Create booking frame widgets
        self.booking_label = tk.Label(self.booking_frame, text="Book Flight")
        self.booking_label.pack()

        self.flight_number_label = tk.Label(self.booking_frame, text="Flight Number:")
        self.flight_number_label.pack(side=tk.LEFT)

        self.flight_number_var = tk.StringVar()
        self.flight_number_entry = ttk.Combobox(self.booking_frame, textvariable=self.flight_number_var)
        self.flight_number_entry['values'] = [flight['number'] for flight in self.flights]
        self.flight_number_entry.pack(side=tk.LEFT)

        self.book_button = tk.Button(self.booking_frame, text="Book", command=self.book_flight)
        self.book_button.pack(side=tk.LEFT)

        # Create exit frame widgets
        self.exit_button = tk.Button(self.exit_frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # Create timer label
        self.timer_label = tk.Label(self.main_frame, text="Time remaining: 10 minutes")
        self.timer_label.pack()

        # Start timer
        self.start_time = datetime.now()
        self.timer()

    def search_flights(self):
        # Search flights logic here
        from_city = self.from_var.get()
        to_city = self.to_var.get()
        result = [flight for flight in self.flights if flight['from'] == from_city and flight['to'] == to_city]
        print("Search result:")
        for flight in result:
             print(f"Flight Number: {flight['number']}, From: {flight['from']}, To: {flight['to']}, Time: {flight['time']}")

    def book_flight(self):
        # Book flight logic here
        flight_number = self.flight_number_var.get()
        result = [flight for flight in self.flights if flight['number'] == flight_number]
        if result:
            print(f"Flight {flight_number} booked successfully!")
        else:
            print(f"Flight {flight_number} not found!")

    def timer(self):
        current_time = datetime.now()
        time_diff = current_time - self.start_time
        if time_diff < timedelta(minutes=10):
            time_remaining = timedelta(minutes=10) - time_diff
            minutes, seconds = divmod(time_remaining.seconds, 60)
            self.timer_label['text'] = f"Time remaining: {minutes:02d}:{seconds:02d}"
            self.root.after(1000, self.timer)
        else:
            self.timer_label['text'] = "Time's up!"
            self.root.destroy()


root = tk.Tk()
app = FlightBookingApp(root)
root.mainloop()



#4.struct
'''import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking App")

        # Create main frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(pady=10)

        self.booking_frame = tk.Frame(self.main_frame)
        self.booking_frame.pack(pady=10)

        self.exit_frame = tk.Frame(self.main_frame)
        self.exit_frame.pack(pady=10)

        # Create search frame widgets
        self.search_label = tk.Label(self.search_frame, text="Search Flights")
        self.search_label.pack()

        self.from_label = tk.Label(self.search_frame, text="From:")
        self.from_label.pack(side=tk.LEFT)

        self.from_entry = tk.Entry(self.search_frame)
        self.from_entry.pack(side=tk.LEFT)

        self.to_label = tk.Label(self.search_frame, text="To:")
        self.to_label.pack(side=tk.LEFT)

        self.to_entry = tk.Entry(self.search_frame)
        self.to_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_flights)
        self.search_button.pack(side=tk.LEFT)

        # Create booking frame widgets
        self.booking_label = tk.Label(self.booking_frame, text="Book Flight")
        self.booking_label.pack()

        self.flight_number_label = tk.Label(self.booking_frame, text="Flight Number:")
        self.flight_number_label.pack(side=tk.LEFT)

        self.flight_number_entry = tk.Entry(self.booking_frame)
        self.flight_number_entry.pack(side=tk.LEFT)

        self.book_button = tk.Button(self.booking_frame, text="Book", command=self.book_flight)
        self.book_button.pack(side=tk.LEFT)

        # Create exit frame widgets
        self.exit_button = tk.Button(self.exit_frame, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        # Create timer label
        self.timer_label = tk.Label(self.main_frame, text="Time remaining: 10 minutes")
        self.timer_label.pack()

        # Start timer
        self.start_time = datetime.now()
        self.timer()

    def search_flights(self):
        # Search flights logic here
        print("Searching flights from", self.from_entry.get(), "to", self.to_entry.get())

    def book_flight(self):
        # Book flight logic here
        print("Booking flight", self.flight_number_entry.get())

    def timer(self):
        current_time = datetime.now()
        time_diff = current_time - self.start_time
        if time_diff < timedelta(minutes=10):
            time_remaining = timedelta(minutes=10) - time_diff
            minutes, seconds = divmod(time_remaining.seconds, 60)
            self.timer_label['text'] = f"Time remaining: {minutes:02d}:{seconds:02d}"
            self.root.after(1000, self.timer)
        else:
            self.timer_label['text'] = "Time's up!"
            self.root.destroy()

root = tk.Tk()
app = FlightBookingApp(root)
root.mainloop()
'''


#3.struct
'''import tkinter as p1
from tkinter import font as p2
from tkinter import ttk as p3


class App():
    def main_w(self,main_window):
        self.main_window=main_window
        self.widgets=[]

    def create_widgets(self):
        switch=p3.Combobox(
            state="readonly",
            values=['Searching','Booking','Exit']
        )
        switch.place(x=50,y=50)
        switch.set('select app functions')
        #switch.bind("<<ComboboxSelected>>", s1)

        referesh=p3.Button(self.main_window,text='referesh')
        referesh.pack()
        referesh.place(x=200,y=50)
        
        self.widgets.append(switch)
        self.widgets.append(referesh)

    def referesh(self):
        for widget in self.widgets:
            widget.destory()
        self.widgets=[]

        self.create_widgets()





main_window=p1.Tk()
main_window.title("FLIGHT BOOKING SYSTEM")
main_window.geometry("5000x5000")


app=App()
app.create_widgets()

main_window.mainloop()
'''

#2.struct
'''import tkinter as p1
from tkinter import font as p2
from tkinter import ttk as p3
import datetime as date
import sys,os


def search():
    
    

def s1(event):
    sw=switch.get()
    if sw=='Searching':
        search()


def s():
    
    switch.set('select app functions')




main_window=p1.Tk()
main_window.title("FLIGHT BOOKING SYSTEM")
main_window.geometry("5000x5000")

RCB=p2.Font(font='bold',size=15)


switch=p3.Combobox(
    state="readonly",
    values=['Searching','Booking','Exit']
    )
switch.place(x=50,y=50)
switch.set('select app functions')
switch.bind("<<ComboboxSelected>>", s1)


referesh=p3.Button(text='referesh',command=s)
referesh.pack()
referesh.place(x=200,y=50)



main_window.mainloop()
'''


#1.struct
'''import datetime

class Flight:
    def _init(self, flight_id, departure_city, arrival_city, departure_date, arrival_date, price):
        self.flight_id = flight_id
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.price = price

class FlightBookingSystem:
    def _init_(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, departure_city, arrival_city, departure_date):
        matching_flights = []
        for flight in self.flights:
            if (flight.departure_city == departure_city and
                    flight.arrival_city == arrival_city and
                    flight.departure_date == departure_date):
                matching_flights.append(flight)
        return matching_flights

    def book_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                print(f"Flight {flight_id} booked successfully!")
                return
        print("Flight not found!")

def main():
    booking_system = FlightBookingSystem()

    # Add some sample flights
    booking_system.add_flight(Flight(_init("AA101", "New York", "Los Angeles", datetime.date(2024, 3, 15), datetime.date(2024, 3, 16), 200)))
    booking_system.add_flight(Flight(_init("AA102", "Los Angeles", "New York", datetime.date(2024, 3, 16), datetime.date(2024, 3, 17), 250)))
    booking_system.add_flight(Flight(_init("UA201", "Chicago", "San Francisco", datetime.date(2024, 3, 15), datetime.date(2024, 3, 16), 300)))

    while True:
        print("\nFlight Booking System")
        print("1. Search Flights")
        print("2. Book Flight")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            departure_city = input("Enter departure city: ")
            arrival_city = input("Enter arrival city: ")
            departure_date = datetime.datetime.strptime(input("Enter departure date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            matching_flights = booking_system.search_flights(departure_city, arrival_city, departure_date)
            if matching_flights:
                print("Matching Flights:")
                for flight in matching_flights:
                    print(f"{flight.flight_id}: {flight.departure_city} to {flight.arrival_city} on {flight.departure_date} - ${flight.price}")
            else:
                print("No matching flights found!")

        elif choice == "2":
            flight_id = input("Enter flight ID to book: ")
            booking_system.book_flight(flight_id)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

#if _name_ == "_main_":
main()
'''
