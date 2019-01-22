#write a program to calculate how much money you should be paid for working at a job.
#For the first 40 hours,you should be paid at an hourly rate.
#Any hours over 40 should be paid at time and a half times the rate:

rate = 10.00
totalHours = 45
regularHours = 40
overTimeHours = totalHours - regularHours
pay = (rate * regularHours) + ((rate * 1.5) * overTimeHours)
print ('For working', totalHours, 'hours, I should be paid', pay)
