# PySideFrameless

A skeleton of frameless desktop application using PySide6.

这是一个使用PySide6实现的基于无边框窗体的桌面应用程序骨架。
<br/>

Simple and beautiful. 

它简单而且美观。
<br/>

Just use Python to create desktop application.

只使用Python就可以创建桌面应用程序。
<br/>


Feel free to try it!

快来试试吧！

# Screenshots
截图

Multi-theme:

多主题：
![image](https://github.com/iounce/PySideFrameless/blob/813492b54c1ce951f4fac40f82e35de090fd5ee3/images/main.png)
<br/>

Multi-language:

多语言
![image](https://github.com/iounce/PySideFrameless/blob/813492b54c1ce951f4fac40f82e35de090fd5ee3/images/main-en.png)

# Usage

使用方法

1.Install dependency library：
安装依赖包：

_pip install pyside6_

_pip install qtawesome_

_[The latest library is a little bit different, so fix the version]_

_[最新的库略有不同，所以这里指定了版本]_

_pip install qt_material==2.12_
<br/>

2.Run the main.py script:

运行main.py脚本

_python main.py_

# Develop

开发

It's not hard to write your own application based on this repo. Just take Windows as an example:

在本仓库的基础上创建自定义的应用程序并不是一件难事，接下来以Windows系统为例：

1.Clone this repo

克隆本仓库
<br/>

2.Install dependency library(The same as usage)

安装依赖包（和用法里面的一致）
<br/>

3.Create a new window:

创建一个新的窗体
<br/>

*Copy a .ui file and rename

*拷贝.ui文件并重命名
<br/>

*Use designer.exe to redesign the window details

*使用designer.exe重新设计界面细节
<br/>

*Use pyside6-uic.exe to compile the .ui file and get a .py file, for example:

*使用pyside6-uic.exe编译.ui文件并得到对应的.py文件，譬如：

_pyside6-uic ui_main.ui > ui_main.py_
<br/>

*Create a new .py file and create a new class derived from QDialog(or others), and then use the ui file above

*创建一个新的.py文件，并新建继承自QDialog（或其他基类）的类，然后在此类中调用上面的ui文件
<br/>

4.Run the main.py script:

运行main.py脚本：

_python main.py_
<br/>

You can get the Qt tools, such as _designer.exe and pyside6-uic.exe_, after installing the PySide6 library.

安装PySide6库以后就可以得到Qt工具包，如 _designer.exe和pyside6-uic.exe_。
<br/>

# Internationalization

国际化

1.Edit _en_US.ts_ file to add English text

在_en_US.ts_文件中增加新的英文文本内容
<br/>

2.Edit _zh_CN.ts_ file to add the translated Chinese text

在_zh_CN.ts_文件中增加对应翻译的中文文本内容
<br/>

3.Compile _en_US.ts_ and _zh_CN.ts_, using _linguist.exe_

使用_linguist.exe_编译_en_US.ts_和_zh_CN.ts_文件
<br/>

4.Use _en_US.qm_和_zh_CN.qm_, generated after compiling

在程序中使用编译后的_en_US.qm_和_zh_CN.qm_文件即可
<br/>

# Acknowledgements
致谢

1.pyside6

https://doc.qt.io/qtforpython/index.html

2.qtawesome

https://github.com/spyder-ide/qtawesome

3.qt_material

https://github.com/UN-GCPDS/qt-material