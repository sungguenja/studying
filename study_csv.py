import csv

friend = {
    '홍길동': '010-0000-1111',
    '둘리': '010-2222-3333',
    '나루토': '010-4444-5555',
    '파이썬': '010-6666-7777',
    '으아이': '010-8888-9999',
}

csvfile = open('studt_csv.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csvfile)

for name, phone in friend.items():
    csv_writer.writerow([name, phone])

csvfile.close()

# if we know `with` we can write like below

# with open('study_csv.csv','w',encoding='utf-8',newline='') as csvfile:
#   csv_writer = csv.writer(csvfile)
#   for name, phone in friend.items():
#      csv_writer.writerow([name, phone])