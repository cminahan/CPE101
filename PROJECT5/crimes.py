# Project 5
# Name: Claire Minahan
# Section: CPE101-03
# Instructor: S. Einakian

# Crime class
class Crime:
    #constructor
    def __init__(self, crime_id, crime_category):
        self.id = crime_id
        self.category = crime_category
        self.day_of_week = None
        self.month = None
        self.hour = None

    #boilerpoints
    def __eq__(self, other):
        return type(self) == type(other) and\
               self.id == other.id
    def __repr__(self):
        return '{} \t {} \t {} \t {} \t {} \n'.format(self.id, self.category, self.day_of_week, self.month, self.hour)

    # turn the object into string format
    def __str__(self):
        return '%d \t %s \t %s \t %s \t %s \n' %(self.id, self.category, self.day_of_week, self.month, self.hour)

    # change the time components to proper format
    def set_time(self, day_of_week, month, hour):
        self.day_of_week = day_of_week
        if month == '01':
            self.month = 'January'
        elif month == '02':
            self.month = 'Febraury'
        elif month == '03':
            self.month = 'March'
        elif month == '04':
            self.month = 'April'
        elif month == '05':
            self.month = 'May'
        elif month == '06':
            self.month = 'June'
        elif month == '07':
            self.month = 'July'
        elif month == '08':
            self.month = 'August'
        elif month == '09':
            self.month = 'September'
        elif month == '10':
            self.month = 'October'
        elif month == '11':
            self.month = 'November'
        elif month == '12':
            self.month = 'December'
        hour = int(hour)
        if hour == 0:
            self.hour = '12AM'
        elif 0 < hour < 12:
            self.hour = '%dAM' %hour
        else:
            self.hour = '%dPM' %(hour-12)

# swap two variable in a list
# list int int --> none
def swap(A, X, Y):
    tmp = A[X]
    A[X] = A[Y]
    A[Y] = tmp

# access the crimes file and turn it into a list
# none --> list
def crimes_tsv():
    fin = open('crimes.tsv', 'r')
    list1 = []
    x = 0
    for lines in fin:
        if x == 0:
            x += 1
            continue
        lines = lines.split()
        id = int(lines[0])
        list2 = [id, lines[1]]
        list1.append(list2)
    fin.close()
    return list1

# access the times.tsv file and return a list of all the crimes
# none --> list
def times_tsv():
    fin = open('times.tsv', 'r')
    list1 = []
    x = 0
    for lines in fin:
        if x == 0:
            x += 1
            continue
        lines = lines.split()
        id = int(lines[0])
        date = lines[2][0:2]
        time = lines[3][0:2]
        list2 = [id, lines[1], date, time]
        list1.append(list2)
    fin.close()
    return list1

# create a list with no duplicates of only robberies and put into numerical order
# list --> list
def create_crimes(lines):
    list1 = []
    for crime in lines:
        if crime[1] == 'ROBBERY':
            list1.append(crime)
    list2 = []
    for item in list1:
        list2.append(item[0])
    list3 = []
    for id in list2:
        if id not in list3:
            list3.append(id)
    for x in range(len(list3)):
        if list1[x][0] != list3[x]:
            list1.remove(list1[x])
            x -= 1
    for i in range(len(list1)):
        minIndex = i
        for k in range(i + 1, len(list1)):
            if list1[k][0] < list1[minIndex][0]:
                minIndex = k
        swap(list1, minIndex, i)
    return list1

#returns the crime object matching the given ID
#list int --> int
def find_crimes(crimes, crime_id):
    for x in range(len(crimes)):
        if crimes[x][0] == crime_id:
            return x
    return -1

# add the time components to their crime object
# list list --> list
def update_crimes(crimes,lines):
    for x in range(len(lines)):
        index = find_crimes(crimes, lines[x][0])
        if index == -1:
            continue
        index = int(index)
        if len(crimes[index]) == 2:
            crimes[index].append(lines[x][1])
            crimes[index].append(lines[x][2])
            crimes[index].append(lines[x][3])
    return crimes

# find the most popular dates of robberies
# list --> list
def count_crimes(crimes):
    tot_robberies = len(crimes)
    monday = 0
    tuesday = 0
    wednesday = 0
    thursday = 0
    friday = 0
    saturday = 0
    sunday = 0
    jan = 0
    feb = 0
    march = 0
    april = 0
    may = 0
    june = 0
    july = 0
    aug = 0
    sept = 0
    oct = 0
    nov = 0
    dec = 0
    twelve_am = 0
    one_am = 0
    two_am = 0
    three_am = 0
    four_am = 0
    five_am = 0
    six_am = 0
    seven_am = 0
    eight_am = 0
    nine_am = 0
    ten_am = 0
    eleven_am = 0
    twelve_pm = 0
    one_pm = 0
    two_pm = 0
    three_pm = 0
    four_pm = 0
    five_pm = 0
    six_pm = 0
    seven_pm = 0
    eight_pm = 0
    nine_pm = 0
    ten_pm = 0
    eleven_pm = 0
    objects = []
    fin = open('robberies.tsv', 'w')
    fin.write('ID \t Category \t DayOfWeek \t Month \t Hour \n')
    for line in crimes:
        crime_object = Crime(line[0], line[1])
        if len(line) == 5:
            crime_object.set_time(line[2], line[3], line[4])
            objects.append(crime_object)
            object_crime = str(crime_object)
            fin.write(object_crime)
        if crime_object.day_of_week == 'Monday':
            monday += 1
        elif crime_object.day_of_week == 'Tuesday':
            tuesday += 1
        elif crime_object.day_of_week == 'Wednesday':
            wednesday += 1
        elif crime_object.day_of_week == 'Thursday':
            thursday += 1
        elif crime_object.day_of_week == 'Friday':
            friday += 1
        elif crime_object.day_of_week == 'Saturday':
            saturday += 1
        elif crime_object.day_of_week == 'Sunday':
            sunday += 1
        if crime_object.month == 'January':
            jan += 1
        elif crime_object.month == 'February':
            feb += 1
        elif crime_object.month == 'March':
            march += 1
        elif crime_object.month == 'April':
            april += 1
        elif crime_object.month == 'May':
            may += 1
        elif crime_object.month == 'June':
            june += 1
        elif crime_object.month == 'July':
            july += 1
        elif crime_object.month == 'August':
            aug += 1
        elif crime_object.month == 'September':
            sept += 1
        elif crime_object.month == 'October':
            oct += 1
        elif crime_object.month == 'November':
            nov += 1
        elif crime_object.month == 'December':
            dec += 1
        if crime_object.hour == '12AM':
            twelve_am += 1
        elif crime_object.hour == '1AM':
            one_am += 1
        elif crime_object.hour == '2AM':
            two_am += 1
        elif crime_object.hour == '3AM':
            three_am += 1
        elif crime_object.hour == '4AM':
            four_am += 1
        elif crime_object.hour == '5AM':
            five_am += 1
        elif crime_object.hour == '6AM':
            six_am += 1
        elif crime_object.hour == '7AM':
            seven_am += 1
        elif crime_object.hour == '8AM':
            eight_am += 1
        elif crime_object.hour == '9AM':
            nine_am += 1
        elif crime_object.hour == '10AM':
            ten_am += 1
        elif crime_object.hour == '11AM':
            eleven_am += 1
        elif crime_object.hour == '12PM':
            twelve_pm += 1
        elif crime_object.hour == '1PM':
            one_pm += 1
        elif crime_object.hour == '2PM':
            two_pm += 1
        elif crime_object.hour == '3PM':
            three_pm += 1
        elif crime_object.hour == '4PM':
            four_pm += 1
        elif crime_object.hour == '5PM':
            five_pm += 1
        elif crime_object.hour == '6PM':
            six_pm += 1
        elif crime_object.hour == '7PM':
            seven_pm += 1
        elif crime_object.hour == '8PM':
            eight_pm += 1
        elif crime_object.hour == '9PM':
            nine_pm += 1
        elif crime_object.hour == '10PM':
            ten_pm += 1
        elif crime_object.hour == '11PM':
            eleven_pm += 1
    days = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
    months = [jan, feb, march, april, may, june, july, aug, sept, oct, nov, dec]
    times = [twelve_am, twelve_pm, one_pm, one_am, two_pm, two_am, three_pm, three_am, four_pm, four_am, five_pm, five_am, \
             six_pm, six_am, seven_am, seven_pm, eight_pm, eight_am, nine_pm, nine_am, ten_pm, ten_am, eleven_pm, eleven_am]
    max_days = 0
    max_day = ''
    for day in days:
        if day > max_days:
            max_days = day
    if max_days == monday:
        max_day += 'Monday'
    elif max_days == tuesday:
        max_day += 'Tuesday'
    elif max_days == wednesday:
        max_day += 'Wednesday'
    elif max_days == thursday:
        max_day += 'Thursday'
    elif max_days == friday:
        max_day += 'Friday'
    elif max_days == saturday:
        max_day += 'Saturday'
    elif max_days == sunday:
        max_day += 'Sunday'

    max_months = 0
    max_month = ''
    for month in months:
        if month > max_months:
            max_months = month
    if max_months == jan:
        max_month += 'January'
    if max_months == feb:
        max_month += 'February'
    if max_months == march:
        max_month += 'March'
    if max_months == april:
        max_month += 'April'
    if max_months == may:
        max_month += 'May'
    if max_months == june:
        max_month += 'June'
    if max_months == july:
        max_month += 'July'
    if max_months == aug:
        max_month += 'August'
    if max_months == sept:
        max_month += 'September'
    if max_months == oct:
        max_month += 'October'
    if max_months == nov:
        max_month += 'November'
    if max_months == dec:
        max_month += 'December'

    max_times = 0
    max_hour = ''
    for time in times:
        if time > max_times:
            max_times = time
    if max_times == twelve_pm:
        max_hour += '12PM'
    if max_times == twelve_am:
        max_hour += '12AM'
    if max_times == one_pm:
        max_hour += '1PM'
    if max_times == one_am:
        max_hour += '1AM'
    if max_times == two_pm:
        max_hour += '2PM'
    if max_times == two_am:
        max_hour += '2AM'
    if max_times == three_am:
        max_hour += '3AM'
    if max_times == three_pm:
        max_hour += '3PM'
    if max_times == four_pm:
        max_hour += '4PM'
    if max_times == four_am:
        max_hour += '4AM'
    if max_times == five_am:
        max_hour += '5AM'
    if max_times == five_pm:
        max_hour += '5PM'
    if max_times == six_am:
        max_hour += '6AM'
    if max_times == six_pm:
        max_hour += '6PM'
    if max_times == seven_pm:
        max_hour += '7PM'
    if max_times == seven_am:
        max_hour += '7AM'
    if max_times == eight_am:
        max_hour += '8AM'
    if max_times == eight_pm:
        max_hour += '8PM'
    if max_times == nine_pm:
        max_hour += '9PM'
    if max_times == nine_am:
        max_hour += '9AM'
    if max_times == ten_pm:
        max_hour += '10PM'
    if max_times == ten_am:
        max_hour += '10AM'
    if max_times == eleven_am:
        max_hour += '11AM'
    if max_times == eleven_pm:
        max_hour += '11PM'
        
    result = ('NUMBER OF PROCESSED ROBBERIES: %s \nDAY WITH MOST ROBBERIES: ' + max_day + '\nMONTH WITH MOST ROBBERIES: ' + max_month + '\nHOUR WITH MOST ROBBERIES: ' + max_hour) %tot_robberies

    fin.close()
    return result

# put all the functions together to run
# none --> none
def main():
    crimes = crimes_tsv()
    times = times_tsv()
    crimes1 = create_crimes(crimes)
    updatedCrimes = update_crimes(crimes1, times)
    print(count_crimes(updatedCrimes))

main()

