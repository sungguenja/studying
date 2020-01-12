data_list = list(range(1, 21)) # data_list={1,2,skip,20}

map_list = list(map(lambda x: x + 5, data_list)) # map_list = data+list + 5

print("this is data list that is added map function : {0}".format(map_list))

filter_list = list(filter(lambda x: x%3==0 , map_list))
print("this is 3's multiple in data list : {0}".format(filter_list))

map_str=input("pls input what do you want to do data list : (ex: x+5)")
filter_str=input("input filter expression : ")
new_list=list(map(lambda x: eval(map_str), data_list))
m_filter_list = list(filter(lambda x: eval(filter_str) , new_list))
print("this is ur map list : {0}".format(new_list))
print("this is ur filter list : {0}".format(m_filter_list))