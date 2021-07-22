import sys
import func
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
import pics_rc
from atm import Ui_atm
from cash import Ui_cash
from cash1 import Ui_cash1
from login import Ui_login
from unlock import Ui_unlock
from signup import Ui_signup
from signup1 import Ui_signup1
from inquiry import Ui_inquiry
from manager import Ui_manager
from signout import Ui_signout
from deposit import Ui_deposit
from deposit1 import Ui_deposit1
from transfer import Ui_transfer
from card_out import Ui_card_out
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


# 管理员界面
class manager(QMainWindow, Ui_manager):
    def __init__(self):
        super(manager, self).__init__()
        self.setupUi(self)


# 输入身份信息界面
class signup(QMainWindow, Ui_signup):
    def __init__(self):
        super(signup, self).__init__()
        self.setupUi(self)
        self.tel.setValidator(QtGui.QIntValidator())  #########


# 注册输入密码界面
class signup1(QMainWindow, Ui_signup1):
    def __init__(self):
        super(signup1, self).__init__()
        self.setupUi(self)
        self.pwd.setValidator(QtGui.QIntValidator())  #########
        self.pwd1.setValidator(QtGui.QIntValidator())  #########


# 注销界面
class signout(QMainWindow, Ui_signout):
    def __init__(self):
        super(signout, self).__init__()
        self.setupUi(self)
        self.account.setValidator(QtGui.QIntValidator())  #########
        self.pwd.setValidator(QtGui.QIntValidator())  #########


# 账号解锁界面
class unlock(QMainWindow, Ui_unlock):
    def __init__(self):
        super(unlock, self).__init__()
        self.setupUi(self)
        self.account.setValidator(QtGui.QIntValidator())  #########


# 登陆界面
class login(QMainWindow, Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.count = 3
        self.account.setValidator(QtGui.QIntValidator())  #########
        self.pwd.setValidator(QtGui.QIntValidator())  #########


# ATM机界面
class atm(QMainWindow, Ui_atm):
    def __init__(self):
        super(atm, self).__init__()
        self.setupUi(self)


# 取款界面1
class cash(QMainWindow, Ui_cash):
    def __init__(self):
        super(cash, self).__init__()
        self.setupUi(self)


# 其他金额取款
class cash1(QMainWindow, Ui_cash1):
    def __init__(self):
        super(cash1, self).__init__()
        self.setupUi(self)
        self.amount.setValidator(QtGui.QIntValidator())  #########


# 存款界面1
class deposit(QMainWindow, Ui_deposit):
    def __init__(self):
        super(deposit, self).__init__()
        self.setupUi(self)


# 其他金额存款
class deposit1(QMainWindow, Ui_deposit1):
    def __init__(self):
        super(deposit1, self).__init__()
        self.setupUi(self)
        self.amount.setValidator(QtGui.QIntValidator())  #########


# 转账界面
class transfer(QMainWindow, Ui_transfer):
    def __init__(self):
        super(transfer, self).__init__()
        self.setupUi(self)
        self.account.setValidator(QtGui.QIntValidator())  #########
        self.amount.setValidator(QtGui.QIntValidator())  #########


# 查询界面
class inquiry(QMainWindow, Ui_inquiry):
    def __init__(self):
        super(inquiry, self).__init__()
        self.setupUi(self)


# 取卡后界面
class card_out(QMainWindow, Ui_card_out):
    def __init__(self):
        super(card_out, self).__init__()
        self.setupUi(self)
        self.count = 10
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer1 = QTimer(self)  # 初始化一个定时器
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.Refresh)

    def Refresh(self):
        if self.count > 0:
            self.label_time.setText(str(self.count))
            self.count -= 1
        else:
            self.timer.stop()
            self.count = 10


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 各种界面示例创建
    manager = manager()
    signup = signup()
    signup1 = signup1()
    unlock = unlock()
    signout = signout()
    login = login()
    atm = atm()
    cash = cash()
    cash1 = cash1()
    deposit = deposit()
    deposit1 = deposit1()
    inquiry = inquiry()
    transfer = transfer()
    card_out = card_out()
    # 显示管理员界面
    manager.show()


    # 显示注册界面
    def show_signup():
        manager.close()
        signup.show()


    # 显示登录界面
    def show_login():
        manager.close()
        login.show()


    # 显示注销界面
    def show_signout():
        manager.close()
        signout.show()


    # 显示账户解锁界面
    def show_unlock():
        manager.close()
        unlock.show()


    """
    输入身份信息，点确定开户，验证身份信息，并显示填写密码阶段
    判断用户填写的信息是否正确
    正确
    跳转到输密码界面
    姓名为空
    电话号码为空
    提示：电话号码不为空请重新输入
    提示：身份证号输入错误，请重新输入
    全部正确，显示密码确认界面，显示注册账号
    """


    def show_signup1():
        if len(signup.name.text()) == 0:
            QMessageBox.warning(signup1, '警告', '姓名不为空，请重新输入！')
        elif len(signup.tel.text()) == 0:
            QMessageBox.warning(signup1, '警告', '电话不为空，请重新输入！')
        elif len(signup.tel.text()) > 12:
            QMessageBox.warning(signup1, '警告', '电话号码不规范，请重新输入！')
        elif len(signup.id.text()) == 0:
            QMessageBox.warning(signup1, '警告', '身份证号码不为空，请重新输入！')
        elif len(signup.id.text()) > 18:
            QMessageBox.warning(signup1, '警告', '身份证号码不规范，请重新输入！')
        elif not func.id_status(signup.id.text()):
            QMessageBox.warning(signup1, '警告', '您有账户尚处于冻结状态，无法开户！')
            signup.close()
            signup.name.setText("")
            signup.tel.setText("")
            signup.id.setText("")
            manager.show()
        else:
            reply = QMessageBox.question(signup, '询问', '确认信息填写无误', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                name = signup.name.text()
                tel = signup.tel.text()
                id1 = signup.id.text()
                func.insert_user(name, tel, id1)
                card_account = func.randomCardNum()
                signup1.account.setText(card_account)
                signup.close()
                signup.name.setText("")
                signup.tel.setText("")

                signup1.show()  # show()方法显示窗口
            elif reply == QMessageBox.No:
                pass


    # 从输入用户信息界面返回管理员界面
    def signup_return_manager():
        reply = QMessageBox.question(signup, '询问', '您正在进行开户操作，确认退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            signup.name.setText("")
            signup.tel.setText("")
            signup.id.setText("")
            signup.close()
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass


    """
    注册验证密码界面
    注册 检验用户两次密码信息输入是否正确
    是
    提示：开户成功，返回到管理员界面
    否
    提示：密码输入不一致，请重新输入
    """


    def signup_confirm():
        if len(signup1.pwd.text()) == 0:
            QMessageBox.warning(signup1, '警告', '密码不为空，请重新输入！')
        elif signup1.pwd.text() != signup1.pwd1.text():
            QMessageBox.warning(signup1, '警告', '密码不一致，请重新输入！')
        elif len(signup1.pwd.text()) != 6:
            QMessageBox.warning(signup1, '警告', '密码长度为六位，请重新输入！')
        else:
            QMessageBox.information(signup1, '通知', '注册成功，请妥善保存您的账号和密码！')
            id2 = signup.id.text()
            cno = signup1.account.text()
            pwd = signup1.pwd.text()
            balance = 0
            status = 0
            func.insert_card(cno, id2, pwd, balance, status)
            signup1.close()
            signup.id.setText("")
            signup1.pwd.setText("")
            signup1.pwd1.setText("")
            signup1.account.setText("")
            manager.show()  # show()方法显示窗口


    # 注销界面返回管理员界面
    def signout_return_manager():
        reply = QMessageBox.question(signout, '询问', '您正在进行注销操作，确认退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            signout.account.setText("")
            signout.pwd.setText("")
            signout.close()
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass


    # 账户解锁界面返回管理员界面
    def unlock_return_manager():
        reply = QMessageBox.question(unlock, '询问', '您正在进行账户解锁操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            unlock.account.setText("")
            unlock.id.setText("")
            unlock.close()
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass


    # 登陆界面返回管理员界面
    def login_return_manager():
        reply = QMessageBox.question(login, '询问', '确认退出登录？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            login.account.setText("")
            login.pwd.setText("")
            login.close()
            login.count = 3
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass


    """
    解锁 检验账号信息和身份证号信息是否一致
    是
    提示：解卡成功
    否
    判断
    卡是否存在
    否
    提示：银行卡不存在
    判断是否处于冻结状态
    提示：此卡未被冻结请返回
    """


    def unlock_confirm():
        if len(unlock.account.text()) == 0:
            QMessageBox.warning(unlock, '警告', '账号不为空，请重新输入！')
        elif len(unlock.account.text()) != 6:
            QMessageBox.warning(unlock, '警告', '账号不符合规范，请重新输入！')
        elif len(unlock.id.text()) == 0:
            QMessageBox.warning(unlock, '警告', '身份证号码不为空，请重新输入！')
        elif len(unlock.id.text()) > 18:
            QMessageBox.warning(unlock, '警告', '身份证号码不规范，请重新输入！')
        elif not func.isExistCard(unlock.account.text()):
            QMessageBox.information(unlock, '警告', '账户不存在！')
        elif func.card_status(unlock.account.text()):
            QMessageBox.information(unlock, '警告', '账户未被冻结，无需解锁！')
        else:
            reply = QMessageBox.question(unlock, '询问', '确认解锁账户', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if func.unlock_card(unlock.account.text(), unlock.id.text()):
                    QMessageBox.information(unlock, '提示', '您的账户已解锁！')
                    unlock.close()
                    unlock.account.setText("")
                    unlock.id.setText("")
                    manager.show()  # show()方法显示窗口
                else:
                    QMessageBox.warning(unlock, '警告', '身份证id错误，请重新输入！')
            elif reply == QMessageBox.No:
                pass


    """
    注销 注销账户的银行卡
    银行卡信息是否正确
    否
    提示卡号不存在或密码错误
    您还有()次机会
    若有余额
    提示：卡里还有钱未取请先取钱
    没余额
    提示您正在注销账户
    请确认操作
    Yes
    提示账户已注销
    No
    关闭messagebox
    """


    def signout_confirm():
        if len(signout.account.text()) == 0:
            QMessageBox.warning(signout, '警告', '账号不为空，请重新输入！')
        elif len(signout.account.text()) != 6:
            QMessageBox.warning(signout, '警告', '账号不符合规范，请重新输入！')
        elif len(signout.pwd.text()) == 0:
            QMessageBox.warning(signout, '警告', '密码不为空，请重新输入！')
        elif len(signout.pwd.text()) != 6:
            QMessageBox.warning(signout, '警告', '密码不规范，请重新输入！')
        elif not func.isExistCard(signout.account.text()):
            QMessageBox.warning(signout, '警告', '账户不存在！')
        elif not func.is_pwd_correct(signout.account.text(), signout.pwd.text()):
            QMessageBox.warning(signout, '警告', '密码不正确，请重新输入！')
        elif func.is_cash_enough(signout.account.text(), 1):
            QMessageBox.warning(signout, '警告', '账户尚有余额，无法注销，请联系柜台人员！')
        else:
            reply = QMessageBox.question(signout, '询问', '确认注销账户', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                func.del_account(signout.account.text())
                QMessageBox.information(signout, '提示', '您的账户已注销！')
                signout.close()
                signout.account.setText("")
                signout.pwd.setText("")
                manager.show()  # show()方法显示窗口
            elif reply == QMessageBox.No:
                pass


    """
    登录 用户登录到ATM界面
    判断卡号是否存在
    否
    提示：卡号输入错误
    密码是否输入正确
    是
    判断卡的状态
    status = 1
    提示：卡已被锁定，请先解卡
    ok
    status = 0
    跳转到用户界面
    否
    提示：密码输入错误
    """


    def show_atm():
        if len(login.account.text()) == 0:
            QMessageBox.warning(login, '警告', '账号不为空，请重新输入！')
        elif len(login.account.text()) != 6:
            QMessageBox.warning(login, '警告', '账号不符合规范，请重新输入！')
        elif len(login.pwd.text()) == 0:
            QMessageBox.warning(login, '警告', '密码不为空，请重新输入！')
        elif len(login.pwd.text()) != 6:
            QMessageBox.warning(login, '警告', '密码不规范，请重新输入！')
        elif not func.isExistCard(login.account.text()):
            QMessageBox.warning(login, '警告', '账户不存在！')
        elif not func.card_status(login.account.text()):
            QMessageBox.warning(login, '警告', '您的账户已冻结！请解锁账户后在登陆！')
        elif not func.is_pwd_correct(login.account.text(), login.pwd.text()):
            login.count -= 1
            if login.count <= 0:
                func.lock_card(login.account.text())
                QMessageBox.warning(login, '提示', '您的账户已被冻结！请解锁账户后在登陆！')
                login.close()
                login.account.setText("")
                login.pwd.setText("")
                manager.show()  # show()方法显示窗口
            else:
                QMessageBox.warning(login, '警告', f'密码不正确，您还有{login.count}次机会！')
        else:
            login.close()
            login.pwd.setText("")
            login.count = 3
            atm.show()  # show()方法显示窗口


    # 显示取款界面1
    def show_cash():
        atm.close()
        cash.show()


    # 显示取款界面2
    def show_cash1():
        cash.close()
        cash1.show()


    # 显示存款界面1
    def show_deposit():
        atm.close()
        deposit.show()


    # 显示存款界面2
    def show_deposit1():
        deposit.close()
        deposit1.show()


    # 显示转账界面
    def show_transfer():
        atm.close()
        transfer.show()


    # 显示查询界面
    def show_inquiry():
        inquiry.balance.setText(str(func.inquiry(login.account.text())))
        inquiry.balance1.setText(str(func.inquiry(login.account.text())))
        atm.close()
        inquiry.show()


    # 从取款界面1返回ATM界面
    def cash_return_atm():
        QMessageBox.information(cash, '提示', '正在退出取款界面，请保管好您的财物！')
        cash.close()
        atm.show()


    # 从取款界面2返回ATM界面
    def cash1_return_atm():
        reply = QMessageBox.question(transfer, '询问', '您正在进行取款操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash1.amount.setText("")
            cash1.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 从存款界面1返回ATM界面
    def deposit_return_atm():
        QMessageBox.information(deposit, '提示', '正在退出存款界面！')
        deposit.close()
        atm.show()


    # 从存款界面2返回ATM界面
    def deposit1_return_atm():
        reply = QMessageBox.question(deposit1, '询问', '您正在进行存款操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit1.amount.setText("")
            deposit1.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 转账界面返回ATM界面
    def transfer_return_atm():
        reply = QMessageBox.question(transfer, '询问', '您正在进行转账操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            transfer.amount.setText("")
            transfer.account.setText("")
            transfer.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 查询界面返回ATM界面
    def inquiry_return_atm():
        QMessageBox.question(inquiry, '提示', '正在退出查询界面')
        inquiry.balance.setText("")
        inquiry.balance1.setText("")
        inquiry.close()
        atm.show()


    # 以下是各种退卡操作
    def atm_show_card_out():
        reply = QMessageBox.question(atm, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            atm.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def cash_show_card_out():
        reply = QMessageBox.question(cash, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def cash1_show_card_out():
        reply = QMessageBox.question(cash1, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash1.amount.setText("")
            cash1.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def deposit_show_card_out():
        reply = QMessageBox.question(deposit, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def deposit1_show_card_out():
        reply = QMessageBox.question(deposit1, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit1.amount.setText("")
            deposit1.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def transfer_show_card_out():
        reply = QMessageBox.question(transfer, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            transfer.amount.setText("")
            transfer.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def inquiry_show_card_out():
        reply = QMessageBox.question(inquiry, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            inquiry.balance.setText("")
            inquiry.balance1.setText("")
            inquiry.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    # 各种取款操作
    def cash100():
        reply = QMessageBox.question(cash, '询问', '确认取款100元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if func.is_cash_enough(login.account.text(), 100):
                func.cash_out(login.account.text(), 100)
                QMessageBox.question(cash, '提示', '取款成功！')
            else:
                QMessageBox.warning(cash, '警告', '余额不足，无法取款！')
        elif reply == QMessageBox.No:
            pass


    def cash500():
        reply = QMessageBox.question(cash, '询问', '确认取款500元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if func.is_cash_enough(login.account.text(), 500):
                func.cash_out(login.account.text(), 500)
                QMessageBox.question(cash, '提示', '取款成功！')
            else:
                QMessageBox.warning(cash, '警告', '余额不足，无法取款！')
        elif reply == QMessageBox.No:
            pass


    def cash1000():
        reply = QMessageBox.question(cash, '询问', '确认取款1000元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if func.is_cash_enough(login.account.text(), 1000):
                func.cash_out(login.account.text(), 1000)
                QMessageBox.question(cash, '提示', '取款成功！')
            else:
                QMessageBox.warning(cash, '警告', '余额不足，无法取款！')
        elif reply == QMessageBox.No:
            pass


    def cash2000():
        reply = QMessageBox.question(cash, '询问', '确认取款2000元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if func.is_cash_enough(login.account.text(), 2000):
                func.cash_out(login.account.text(), 2000)
                QMessageBox.question(cash, '提示', '取款成功！')
            else:
                QMessageBox.warning(cash, '警告', '余额不足，无法取款！')
        elif reply == QMessageBox.No:
            pass


    def cash5000():
        reply = QMessageBox.question(cash, '询问', '确认取款5000元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            if func.is_cash_enough(login.account.text(), 5000):
                func.cash_out(login.account.text(), 5000)
                QMessageBox.question(cash, '提示', '取款成功！')
            else:
                QMessageBox.warning(cash, '警告', '余额不足，无法取款！')
        elif reply == QMessageBox.No:
            pass


    # 跳转其他金额取款界面
    def cash_other():
        cash.close()
        cash1.show()


    # 其他金额取款
    def cash_confirm():
        if cash1.amount.text() == 0:
            QMessageBox.warning(cash1, '警告', '取款金额不为0！')
        elif int(cash1.amount.text()) % 100 != 0:
            QMessageBox.warning(cash1, '警告', '取款金额必须为100整数倍！')
        else:
            reply = QMessageBox.question(cash1, '询问', f'确认取款{cash1.amount.text()}元？', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                if func.is_cash_enough(login.account.text(), cash1.amount.text()):
                    func.cash_out(login.account.text(), cash1.amount.text())
                    QMessageBox.question(cash1, '提示', '取款成功！')
                    cash1.amount.setText("")
                else:
                    QMessageBox.warning(cash1, '警告', '余额不足，无法取款！')
                    cash1.amount.setText("")
            elif reply == QMessageBox.No:
                pass


    # 存款操作
    def deposit100():
        reply = QMessageBox.question(deposit, '询问', '确认存款100元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            func.deposit(login.account.text(), 100)
            QMessageBox.question(deposit, '提示', '存款成功！')
        elif reply == QMessageBox.No:
            pass


    def deposit500():
        reply = QMessageBox.question(deposit, '询问', '确认存款500元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            func.deposit(login.account.text(), 500)
            QMessageBox.question(deposit, '提示', '存款成功！')
        elif reply == QMessageBox.No:
            pass


    def deposit1000():
        reply = QMessageBox.question(deposit, '询问', '确认存款1000元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            func.deposit(login.account.text(), 1000)
            QMessageBox.question(deposit, '提示', '存款成功！')
        elif reply == QMessageBox.No:
            pass


    def deposit2000():
        reply = QMessageBox.question(deposit, '询问', '确认存款 2000 元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            func.deposit(login.account.text(), 2000)
            QMessageBox.question(deposit, '提示', '存款成功！')
        elif reply == QMessageBox.No:
            pass


    def deposit5000():
        reply = QMessageBox.question(deposit, '询问', '确认存款 5000 元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            func.deposit(login.account.text(), 5000)
            QMessageBox.question(deposit, '提示', '存款成功！')
        elif reply == QMessageBox.No:
            pass


    # 跳转其他金额存款界面
    def deposit_other():
        deposit.close()
        deposit1.show()


    # 其他金额存款
    def deposit_confirm():
        if deposit1.amount.text() == 0:
            QMessageBox.warning(deposit1, '警告', '存款金额不为0！')
        elif int(deposit1.amount.text()) % 100 != 0:
            QMessageBox.warning(deposit1, '警告', '存款金额必须为100整数倍！')
        else:
            reply = QMessageBox.question(deposit1, '询问', f'确认存款 {deposit1.amount.text()} 元？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                func.deposit(login.account.text(), deposit1.amount.text())
                QMessageBox.question(deposit1, '提示', '存款成功！')
                deposit1.amount.setText("")
            elif reply == QMessageBox.No:
                pass


    # 确认转账操作
    def transfer_confirm():
        if len(transfer.account.text()) == 0:
            QMessageBox.warning(transfer, '警告', '收款账号不为空，请重新输入！')
        elif len(transfer.account.text()) != 6:
            QMessageBox.warning(transfer, '警告', '账号不符合规范，请重新输入！')
        elif len(transfer.amount.text()) == 0:
            QMessageBox.warning(transfer, '警告', '密码不为空，请重新输入！')
        elif login.account.text() == transfer.account.text():
            QMessageBox.warning(transfer, '警告', '无法为自身转账！')
        elif not func.isExistCard(transfer.account.text()):
            QMessageBox.warning(transfer, '警告', '转账收款账户不存在！')
        elif not func.is_cash_enough(login.account.text(), transfer.amount.text()):
            QMessageBox.warning(transfer, '警告', '余额不足，无法转账！')
        else:
            func.cash_out(login.account.text(), transfer.amount.text())
            func.deposit(transfer.account.text(), transfer.amount.text())
            transfer.amount.setText("")
            transfer.account.setText("")
            QMessageBox.warning(transfer, '提示', '转账成功！')


    # 退卡界面10秒后返回管理员界面
    def card_out_manager():
        card_out.close()
        card_out.timer1.stop()
        manager.show()


    # 各种按键与函数连接
    manager.signup_btn.clicked.connect(show_signup)
    manager.signout_btn.clicked.connect(show_signout)
    manager.login_btn.clicked.connect(show_login)
    manager.unlock_btn.clicked.connect(show_unlock)

    signup.return_manager_btn.clicked.connect(signup_return_manager)
    signup.confirm_btn.clicked.connect(show_signup1)
    signout.signout_btn.clicked.connect(signout_confirm)
    signout.return_manager_btn.clicked.connect(signout_return_manager)

    signup1.signup_btn.clicked.connect(signup_confirm)

    unlock.unlock_btn.clicked.connect(unlock_confirm)
    unlock.return_manager_btn.clicked.connect(unlock_return_manager)

    login.login_btn.clicked.connect(show_atm)
    login.return_manager_btn.clicked.connect(login_return_manager)

    atm.cash_btn.clicked.connect(show_cash)
    atm.deposit_btn.clicked.connect(show_deposit)
    atm.transfer_btn.clicked.connect(show_transfer)
    atm.inquiry_btn.clicked.connect(show_inquiry)
    atm.card_out_btn.clicked.connect(atm_show_card_out)

    cash.btn100.clicked.connect(cash100)
    cash.btn500.clicked.connect(cash500)
    cash.btn1000.clicked.connect(cash1000)
    cash.btn2000.clicked.connect(cash2000)
    cash.btn5000.clicked.connect(cash5000)
    cash.other_amount_btn.clicked.connect(cash_other)
    cash.return_btn.clicked.connect(cash_return_atm)
    cash.card_out_btn.clicked.connect(cash_show_card_out)

    cash1.cash_btn.clicked.connect(cash_confirm)
    cash1.return_btn.clicked.connect(cash1_return_atm)
    cash1.card_out_btn.clicked.connect(cash1_show_card_out)

    deposit.btn100.clicked.connect(deposit100)
    deposit.btn500.clicked.connect(deposit500)
    deposit.btn1000.clicked.connect(deposit1000)
    deposit.btn2000.clicked.connect(deposit2000)
    deposit.btn5000.clicked.connect(deposit5000)
    deposit.other_amount_btn.clicked.connect(deposit_other)
    deposit.return_btn.clicked.connect(deposit_return_atm)
    deposit.card_out_btn.clicked.connect(deposit_show_card_out)

    deposit1.deposit_btn.clicked.connect(deposit_confirm)
    deposit1.return_btn.clicked.connect(deposit1_return_atm)
    deposit1.card_out_btn.clicked.connect(deposit1_show_card_out)

    transfer.transfer_btn.clicked.connect(transfer_confirm)
    transfer.return_btn.clicked.connect(transfer_return_atm)
    transfer.card_out_btn.clicked.connect(transfer_show_card_out)

    inquiry.return_btn.clicked.connect(inquiry_return_atm)
    inquiry.card_out_btn.clicked.connect(inquiry_show_card_out)

    card_out.timer1.timeout.connect(card_out_manager)

    sys.exit(app.exec_())
