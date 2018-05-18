import math

## Question 1 ##
# Variable Sets #
radius=5
vol=4/3*math.pi*radius**3
# Display #
print(f"1. Sphere Radius={radius} Volume={round(vol,2)}")

## Question 2 ##
# Variable Sets #
cost=24.95
disc=0.40
ship=3
shipdisc=0.75
numbooks=60
# Display #
total=((cost*(1-disc))*60)+(ship+(numbooks-1)*shipdisc)
print(f"2. Total cost for {numbooks} books: ${round(total,2)}")

## Question 3 ##
# Variable Sets #
startTime = [6,52]
easyPace = [8,15]
fastPace = [7,12]
totalTime = (easyPace[0]*2+fastPace[0]*3)+(int((easyPace[1]*2+fastPace[1]*3)/60))
endTime = [startTime[0]+int((startTime[1]+totalTime)/60), (startTime[1]+totalTime)%60]
# Display #
print(f"3. Start Time: {startTime[0]}:{startTime[1]}, Total run time: {totalTime} mins, End Time: {endTime[0]}:{endTime[1]}")


''' OUTPUT FROM ABOVE 

1. Sphere Radius=5 Volume=523.6
2. Total cost for 60 books: $945.45
3. Start Time: 6:52, Total run time: 38 mins, End Time: 7:30

'''



