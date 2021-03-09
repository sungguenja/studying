import mine_array

def myLineEditor():
    now_list = mine_array.ArrayList()
    while True:
        command = str(input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료 => "))

        if command == "i":
            position = int(input("입력행 번호: "))
            content  = str(input("입력 내용  : "))
            now_list.insert(position,content)
        elif command == "d":
            position = int(input("삭제할 행  : "))
            now_list.delete(position)
        elif command == "r":
            position = int(input("변경할 행  : "))
            content  = str(input("입력 내용  : "))
            now_list.replace(position,content)
        elif command == "p":
            print("라인 내용")
            for line in range(now_list.size()):
                print(now_list.getElement(line))
        elif command == "l":
            filename = "test.txt"
            infile   = open(filename,"r")
            lines = infile.readlines()
            for line in lines:
                now_list.insert(now_list.size(),line.rstrip("\n"))
            infile.close()
        elif command == "s":
            filename = "test.txt"
            outfile = open(filename,"w")
            for i in range(now_list.size()):
                outfile.write(now_list.getElement(i),"\n")
            outfile.close()
        else:
            print("명령어만 입력해주세요")
myLineEditor()