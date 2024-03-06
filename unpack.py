def total(hour, minute, second):
    return (hour*60 +minute)*60 + second

time = { "hour" : 1 , "minute" :25 , "second" : 10}
print(f"{total(**time)} seconds") # * unpacks the list  and ** unpacks dictionary