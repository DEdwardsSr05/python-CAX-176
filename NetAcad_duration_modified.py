# NetAcad duration script
# July 15, 2026
# Original script calculated duration but not say number of days in output

# # Starting input
# hour = int(input("Starting time (hours): "))   # Start at 8am
# mins = int(input("Starting time (minutes): ")) # Start at 00 minutes
# duration = int(input("Event duration (minutes): "))  # 10200 minutes, should be 10am following day

# # Convert minutes to days
# days = duration // 1440

# # Convert remaining minutes to hours
# hours = duration % 1440

# # Remaining minutes after days and hours conversions


# # hour = hour + (minutes // 60)
# # minutes = minutes % 60
# # hour = hour % 24

# # print(hour, ":", minutes, sep=" ")


# Script from Claude that works. Need to understand it. Need to wrp head around why adding start time hours and minutes
# to the duration still gives correct answer.  
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura              # total minutes: start minutes + full duration
hour = hour + mins // 60        # add whole hours hidden in that total (NOT capped at 24 yet)
mins = mins % 60                # leftover minutes, 0-59

days = hour // 24                # <-- the fix: capture full days BEFORE hour gets capped
hour = hour % 24                 # NOW cap hour to 0-23

print(days, ":", hour, ":", mins, sep='')