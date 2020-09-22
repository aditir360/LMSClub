#!/usr/bin/env python3

#
# This is my code which includes a function that will check if in my schedule that there is a "Monday" in it, and prints the schedule in uppercase.
#


def find_monday(mycalender1):
    mycalendar1 =  """Day               Time          Subject
                    Monday   9:10 AM - 10:15 AM      LA
                              10:35 AM - 11:40 AM     SS
                              12:10 PM - 1:15 PM      S
                    Tuesday  9:10 AM - 10:15 AM     Math
                              10:35 AM - 11:40 AM  Orchestra
                              12:10 PM - 1:15 PM      PF"""
   # This is my calendar.
   if "Monday" in mycalendar1:
       print "Monday is present."
   else:
       print "Monday is not present."
   # This is how the function will check if "Monday" is there in the schedule or not.
   return
def main():
    print find_monday()
    # This is where I call my function.
    print mycalendar.upper()
    # This is where I print my schedule in UPPERCASE.
    
