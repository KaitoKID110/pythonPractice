from card import Card
from user import User
import random
class ATM(object):
    def __init__(self):
        self.allUsers = {}

    #开户
    def createUser(self):
        #目标：向用户字典中添加一对键值对{卡号-用户}
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestoreMoney = int(input("请输入预存金额："))
        if prestoreMoney < 0:
            print("预存输入有误，开户失败……")
            return -1

        onePasswd = input("请设置密码：")
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！开户失败……")

        #信息已完整
        cardStr = self.randomCardId()

        card = Card(cardStr,onePasswd,prestoreMoney)
        user = User(name,idcard,phone,card)
        self.allUsers[cardStr] =user
        print("开户成功！！请牢记卡号（%s）……"% cardStr)

    #查询
    def searchUserInfo(self):
        pass
    #取款
    def getMony(self):
        pass
    #存款
    def saveMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    #改密
    def changePasswd(self):
        pass
    #锁定
    def lockUser(self):
        pass
    #解锁
    def unlockUser(self):
        pass
    #补卡
    def newCard(self):
        pass
    #销户
    def killUser(self):
        pass

    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False
    #生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord("0"),ord("9")+1))
                str += ch
            if not self.allUsers.get(str):
                return str