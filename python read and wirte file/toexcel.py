import pandas as pd
raw_data = {'date':[],'Gl_max':[]}
read_f = open('file_name.txt','r')

for line,value in enumerate(read_f):
    if line<2:
        continue
    data,content = value.split('=')
    data_row,data_type = data.split('_')
    if data_type == 'DateTime':
        date = list(content.split())
        date = date[0]
        raw_data['date'].append(date)
    elif data_type == 'ResMsg':
        msg_content = content.split(',')
        msg_content = msg_content[-1][1:-1]
        raw_data['Gl_max'].append(msg_content)
raw_data = pd.DataFrame(raw_data)
raw_data.to_excel(excel_writer='excel_name.xlsx')