def saveFile(data):
    save_path = 'D:\\temp.out'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()