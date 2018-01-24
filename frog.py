# coding=utf-8
# 

def frog(deep):
	meter_day = 2
	day_1 = deep % meter_day
	if deep>5:
		if day_1>0:
			day = (deep-5)//meter_day+1
		else:
			day = deep/meter_day-1
		print("*" * 50)
		print("\n需要{0}天\n".format(int(day)))
	else:
		day = 1
		print("需要1天")

	return day

if __name__ == '__main__':
	a = int(input("\n请输入井深："))
	frog(a)