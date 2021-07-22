## 前言

本项目仅作学习之用，不得用作其他用途。

## 运行环境

Win 10 专业版

python 3.8.5

pyQt5 

附[pyqt5安装教程](https://blog.csdn.net/qq_32892383/article/details/108867482)在这里，非常详细，感谢大佬的无私分享

mysql 8.0

使用pymysql与数据库进行交互



## 系统数据库

系统数据库只有两张表，user表和card表，具体参数如下图，**在运行程序前一定要在func.py中将数据库信息更换为自己的**，否则不会运行成功。

<img src="https://github.com/er-jia/PicGo/blob/master/20210723005256.png" alt="image-20210723005255840" style="zoom:50%;" />



## 系统实现的功能

### 1.管理员界面

开户，解锁账户，注销账户，登录，开户包括用户信息输入和密码确认



### 2.ATM界面

存款，取款，转账，查询，退卡，存款包括选择金额存款和自定义金额存款，取款包括选择金额取款和自定义金额取款，

所有界面都可以跳转ATM界面或退卡

退卡界面会在显示10秒钟之后直接跳转到管理员界面



### 3.与mysql进行交互

所有增删改查操作都会与数据库进行交互



## 系统文件介绍

后缀为ui的文件及其同名文件为各种界面的python文件及ui文件

main.py为系统运行文件

func.py存储了所有系统与数据库交互的函数以及前期数据库准备阶段用到的数据

后缀为prc文件及其同名python文件为系统所用到的图片



## 系统主要界面及功能图

<img src="https://github.com/er-jia/PicGo/blob/master/20210723001527.png" alt="image-20210723001520353" style="zoom:80%;" />

## 系统运行截图

管理界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723001721.png" alt="image-20210723001721864" style="zoom:50%;" />

开户界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723001818.png" alt="image-20210723001818474" style="zoom:50%;" />

登录界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723001857.png" alt="image-20210723001857440" style="zoom:50%;" />

atm界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723002039.png" alt="image-20210723002039378" style="zoom:50%;" />

取款界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723002108.png" alt="image-20210723002108261" style="zoom:50%;" />

查询界面

<img src="https://github.com/er-jia/PicGo/blob/master/20210723004358.png" alt="image-20210723004358048" style="zoom:50%;" />

