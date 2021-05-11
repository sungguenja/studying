import csv
import matplotlib.pyplot as plt
csv_file = open('읽을 csv 파일')
read_file = csv.reader(csv_file)

country_set = set()
source_set = set()
playtime_list = []
sales_list = []
cnt = 0
sales_dict = {}
for line in read_file:
    if cnt == 0:
        cnt += 1
        continue
    # 한줄씩 진행할 코드 진행

# x축,y축 해당될 리스트 생성
# plt.plot(x축,y축,'ro')
# plt.show()

csv_file.close()
