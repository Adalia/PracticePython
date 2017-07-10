def saveFile(data):
    print("保存数据：" + data)
    save_path = 'D:\\temp.out'
    f_obj = open(save_path, 'a')  # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
