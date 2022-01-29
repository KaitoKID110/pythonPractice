from admin import Admin
from atm import ATM
import time


def main():
    # 界面对象
    admin = Admin()

    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    admin.printFunctionView()

    #提款机
    atm = ATM()

    while True:
        admin.printFunctionView()
        #等待用户操作
        option = input("请输入您的操作")
        if option == "1":
            atm.createUser()
        elif option == "2":
            print("查询")
        elif option == "3":
            print("取款")
        elif option == "4":
            print("存储")
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            print("锁定")
        elif option == "8":
            print("解锁")
        elif option == "9":
            print("补卡")
        elif option == "10":
            print("销户")
        elif option == "t":
            if not admin.adminOption():
                return -1
        time.sleep(2)

if __name__ == "__main__":
    main()
