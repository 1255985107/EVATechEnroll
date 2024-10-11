# 0. 来签到啦！- Git

作为一位（准）开发人员，你会遇到很多很多与他人合作完成项目的场景。你也许听说过“这个项目我Fork了”“这个项目我Star了”“我提交了一个PR”这样的说法，其实这都与Git息息相关。

Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。它是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。

### 你的任务

1.  新建一个Git远程仓库，并保证技术小组管理员可以访问到你的仓库，托管平台不限。
2.  使用你的学号作为密钥，将管理员发送给你的一串密文进行解密，并将解密结果放在一个文本文件里，和其他题目的作答分别放在以题目序号命名的文件夹中，推送到你自己的远程仓库。文件格式不限。
3.  技术小组的纳新试题也会同步放在ZJU Git,Github以及Gitea托管平台，当你完成时，请在纳新试题仓库提出issue，并附上你的个人仓库链接。

### 明文的加密过程

1.  明文固定4位，密钥固定学号后4位
2.  将明文与学号对应位置的字符先转化为整数，再相乘，将结果转换为16进制
3.  将4个独立的运算结果之间以`"/"`分割，再整合为一个字符串（密文）
4.  如果搞不清楚这个运算过程，下面有一个利用Python实现的加密示例：

```python
# 明文固定4位，密钥为你的学号后4位
encrypt = lambda clear, key: "".join([hex(ord(clear[i]) * ord(key[i]))[2:] + '/' for i in range(4)])[:-1]

```

你可能会用到的Git命令：

-   `git init`：在当前目录初始化Git仓库
-   `git add . `：将当前目录下所有文件加入暂存区
-   `git commit -m "xxx"`：提交暂存区的更改，并附加评论“xxx”
-   `git push`：将本地仓库的更改推送到远程仓库
-   `git clone https://xxxx`：将\[URL]的仓库克隆到本地

### 附加题

-   请简单解释一下这个函数是如何只用一行代码就完成工作的。它们还能再简化吗？

如果你实在无法通过Git将代码上传到你的个人仓库，请于2024年10月18日23:59之前打包发送到jeffreyqjfing\@gmail.com，邮件标题格式为 **姓名-学号-部门-技术小组纳新**。

### 参考资料

-   [Git](https://git-scm.com/ "Git")
-   [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN "Learn Git Branching")
-   [ZJU Git](https://git.zju.edu.cn/ "ZJU Git")
-   [Python入门](https://www.runoob.com/python/python-tutorial.html "Python入门")