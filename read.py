# 讀取留言檔的資料/計算有多少筆留言
data = [] # 建立空清單
count = 0 # 筆數從0開始
with open('reviews.txt', 'r') as f: # 讀取reviews.txt檔案
	for line in f:
		data.append(line) # 將f檔中的每一行資料加入 data清單中
		count += 1 # 繼續計算筆數
		if count % 1000 == 0: # 計數為1000的倍數，%是求餘數
			print(len(data)) # 印出每1000筆的資料長度
print('檔案讀取完成，總共有', len(data), '筆資料')

# 計算留言的平均長度
sum_len = 0 # 從0計算
for d in data:
	sum_len = sum_len + len(d) # 累加每一筆留長的長度
print('留言的平均長度為', sum_len/len(data)) # 總長度/總筆數
