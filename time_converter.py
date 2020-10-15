#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print("--- Program starting ---")
print("Welcome to this time converter.")

cont = "y"
while(cont.lower() == "y"):
    hours = int(input("Enter the number of hours:"))
    minutes = int(input("Enter the number of minutes:"))
    seconds = int(input("Enter the number of seconds:"))

    print(f"That is {to_seconds(hours,minutes,seconds)} seconds.")
    print()
    cont = input("Do you want to do another conversion? [Y/n]")

print("--- Program exiting ---")