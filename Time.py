str_seconds=input("enter seconds: ")
total_secs=int(str_seconds)

hours = total_secs//3600
secs_still_remaining = total_secs%3600
minutes=secs_still_remaining//60
secs_finally_remaining=secs_still_remaining%60
print("Hrs=", hours, ':' ,"mins=", minutes, ':' ,"secs=" ,secs_finally_remaining)
print("Hrs:Mins:Secs")
print(hours,minutes,secs_finally_remaining, sep=':')