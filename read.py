data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0: # 計數每1000筆，%是求餘數
			print(len(data)) # 才印出資料長度
print(len(data))
print(data[0]) # 取出data清單中的第1項
print('----------------------------------') # 分隔號
print(data[1]) # 取出data清單中的第2項