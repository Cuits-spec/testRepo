#hah

def print_info():
    print('*' * 30)
    print('欢迎使用学生管理系统')
    print('1：添加学员')
    print('2：删除学员')
    print('3：修改学员信息')
    print('4：查看学员信息')
    print('5：显示所有学员信息')
    print('6: 退出系统')
    print('*' * 30)

info = []

def add_info():
    """ 添加学员 """
    new_id = input('请输入学员ID')
    new_name = input('请输入学员姓名')
    new_tel = input('请输入学员电话')

    #声明全局变量info
    global info
    #遍历info若存在重名则报错
    for i in info:
        if new_name == i['name']:
            return '该学员已经存在'

    info_dict = {}
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print(f'添加成功，添加后的数据为{info}')

def del_info():
    """ 删除学员 """
    del_name = input('请输入学员姓名')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('该学员不存在！')
    print(f'删除后数据为：{info}')

def update_info():
    """ 更新学员信息 """
    update_name = input('请输入要修改的学员姓名：')
    global info
    for i in info:
        if update_name != i['name']:
            print('该学员不存在！')
        elif update_name == i['name']:
            print(f'该学员ID为：{i["id"]}，姓名为：{i["name"]},电话为：{i["tel"]}')
            i["id"] = input('请输入修改后的学员id:')
            i["name"] = input('请输入修改后的学员姓名:')
            i["tel"] = input('请输入修改后的学员电话:')
        print(f'修改成功，修改后的数据为{info}')

def quert_info():
    """ 根据id查询学员信息 """
    quert_id = int(input('请输入要查询的学员id'))
    global info
    for i in info:
        if quert_id == i['id']:
            print(f'查询成功，该学员ID为：{i["id"]}，姓名为：{i["name"]},电话为：{i["tel"]}')
        elif quert_id != i['id']:
            print('该学员不存在，请重新输入！')

def print_add():
    """ 查询所有学员信息 """
    print('学号\t姓名\t手机\t')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')

while True:
    print_info()
    user_num = input('请输入功能序号：')
    if user_num == '1':
        add_info()
    elif user_num == '2':
        del_info()
    elif user_num == '3':
        update_info()
    elif user_num == '4':
        quert_info()
    elif user_num == '5':
        print_add()
    elif user_num == '6':
        esc_off = input('是否退出系统----yes or no？')
        if esc_off == 'yes':
            break
        # elif esc_off == 'no':
        #     print('请重新输入功能序号：')

    else:
        print('输入有误，请重新输入！')



