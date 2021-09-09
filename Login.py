import csv
import pandas as pd
import os
def show_choose():
    print("学生信息管理系统")
    print("-功能菜单")
    print()
    print("1.录入学生信息")
    print("2.查找学生信息")
    print("3.删除学生信息")
    print("4.修改学生信息")
    print("5.统计学生总数")
    print("6.显示学生信息")
    print("7.考勤登录")
    print("0.退出信息管理系统")


def input_info():
    if os.path.exists('1.csv') == False:
        f = pd.DataFrame(columns=['学号', '姓名', '性别', '班级', '课程'])
        f.to_csv('1.csv', sep=',', index=False, encoding='gb18030')
    flag = 'y'
    # 向文件中录入学生信息，每一个学生的信息单独占一行
    infile_info = open('1.csv', 'a', newline="")
    while flag == 'y' or flag == 'Y':
        stu_id = input("请输入学生学号（如2002040101）：")
        stu_name = input("请输入学生姓名：")
        stu_sex = input("请输入学生性别：")
        stu_class = input("请输入学生班级：")
        stu_course = input("请输入学生课程：")
        stu_info = stu_id + ',' + stu_name + ',' + stu_sex + ',' + stu_class + ',' + stu_course + '\n'
        infile_info.write(stu_info)
        import get_faces_from_camera
        get_faces_from_camera.main()
        flag = input("是否继续添加学生信息？y/n")
    print("信息录入完毕！！！")
    infile_info.close()
def find_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0
        m = 0  # 定义m，n是为了用作判断文件中是否有此人信息的标记
        findfile_info = open('1.csv', 'r')  # 以可读方式打开文件
        line_info = findfile_info.readlines()
        find_nid = input("按学号查找请输入1，按姓名查找请输入2：")  # 查询方式分为按学号和按姓名
        if find_nid == '1':
            find_id = input('请输入学生学号：')
            for line in line_info:
                if find_id in line:
                    print(line)
                    n = n + 1
            if n == 0:
                print("没有查询到学生信息，无数据显示！！！")
        if find_nid == '2':
            find_name = input('请输入学生姓名：')
            for line in line_info:
                if find_name in line:
                    print(line)
                    m = m + 1
            if m == 0:
                print("没有查询到学生信息，无数据显示！！！")
        findfile_info.close()
        flag = input("是否继续查询学生信息？y/n")
def del_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0  # 用以查无此人时的标记
        defile_info1 = open('1.csv', 'r')  # 以可读方式打开文件
        line_info = defile_info1.readlines()  # 将文件的信息按行全部读取出来，此时line_info是一个列表，每一行是一个元素
        defile_info2 = open('1.csv', 'w')  # 以可写方式打开文件，用来将删除后的信息写入文件
        del_id = input("请输入要删除的学生的学号：")
        for line in line_info:  # 如果要删除的学生学号在文件存储的信息中，就将后面的信息向前移动覆盖这条信息
            if del_id in line:
                continue
            defile_info2.write(line)
            n = n + 1
        if n == len(line_info):
            print("无此学生信息，请核对后再操作！！！")
        else:
            print("学号为{0}的学生信息已被删除！！！".format(del_id))
        defile_info1.close()
        defile_info2.close()
        flag = input("是否继续删除学习信息？y/n")
def mod_info():
    flag = 'y'
    while flag == 'y' or flag == 'Y':
        n = 0  # 用以查无此人时的标记
        mod_id = input("请输入要修改的学生学号：")
        modfile_file1 = open('1.csv', 'r')  # 以可读方式打开文件，读取到line_info中，每一行就是一个列表的元素
        line_info = modfile_file1.readlines()
        modfile_file2 = open('1.csv', 'w')  # 用以写入修改后的数据
        for line in line_info:  # 遍历列表
            if mod_id in line:  # 如果修改的学生信息存在，就重新写入学生信息
                print("已找到学生，请修改信息！")
                mod_id = input("请输入学生学号（如2020001）：")
                mod_name = input("请输入学生姓名：")
                mod_sex = input("请输入学生性别：")
                mod_class = input("请输入学生班级：")
                mod_course = input("请输入学生课程：")
                mod_stu_info = mod_id + ',' + mod_name + ',' + mod_sex + ',' + mod_class + ',' + mod_course + '\n'
                modfile_file2.write(mod_stu_info)
                print("修改成功！！！")
                continue
            modfile_file2.write(line)  # 由于w方式打开的文件重新后会覆盖原有数据，所以需要将原有数据写入
            n = n + 1
        if n == len(line_info):
            print("无此学生信息，请核对后再操作！！！")
        else:
            print("学号为{0}的学生信息已修改！！！".format(mod_id))
        modfile_file1.close()
        modfile_file2.close()
        flag = input("是否继续修改学习信息？y/n")
def sum_info():
    sumfile_info = open('1.csv', 'r')
    line_info = sumfile_info.readlines()
    sum_stu = len(line_info)  # 写出列表中的元素个数
    print("一共有{0}名学生。".format(sum_stu))
    sumfile_info.close()

def show_info():
    showfile_info = pd.read_csv('1.csv', encoding='gb18030')
    print(showfile_info)

def login():
    f = pd.read_csv("1.csv", encoding='gb18030')
    f.insert(5, '考勤', " ", allow_duplicates=False)
    f.to_csv('1.csv', sep=',', index=False, encoding='gb18030')
    import features_extraction_to_csv
    features_extraction_to_csv.main()
    import face_reco_from_camera
    face_reco_from_camera.main()
    yes = str(len(f['考勤'] == '出勤'))
    print("出勤人数:"+yes,"没出勤人数:"+str(len(f.iloc[:, 0:5].values.tolist())-int(yes)))
    f.drop(["考勤"], axis=1, inplace=True)
    f.to_csv('1.csv', sep=',', index=False, encoding='gb18030')

def main():
    show_choose()
    choose_menu = input("请选择：")
    while choose_menu != '0':
        if choose_menu == '1':
            input_info()
        if choose_menu == '2':
            find_info()
        if choose_menu == '3':
            del_info()
        if choose_menu == '4':
            mod_info()
        if choose_menu == '5':
            sum_info()
        if choose_menu == '6':
            show_info()
        if choose_menu == '7':
            login()
        choose_menu = input("请选择：")

    print("欢迎您再次使用！！！")
main()

