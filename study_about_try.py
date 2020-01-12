data_list=list(range(1, 11))

print("data list :",data_list)


try:
    num = int(input("input number for using index :"))
    print("[{0}]: {1}".format(num, data_list[num]))
except IndexError as exception:
    print(exception)
except ValueError as exception:
    print(exception)
except Exception as exception:
    print(exception)