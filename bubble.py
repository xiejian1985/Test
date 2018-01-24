# coding=utf-8
# 冒泡排序

def bubble(date):
    lenth = len(date)
    while lenth > 0:
        lenth -= 1
        first_date = 0
        while first_date < lenth:
            if date[first_date] > date[first_date+1]:
                date[first_date], date[first_date+1] = date[first_date+1], date[first_date]

            first_date += 1

    return date

if __name__ == '__main__':
    a = [12,45,42,10,25,67]
    print(bubble(a))