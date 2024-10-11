# 2. 我来造轮子 - Bash

编写一个bash脚本`search_file.sh`，要求：

-   要求用户输入要搜索的扩展名和要搜索的目录。当用户输入q，程序退出

> 如：

```text
Please input file extension (q to quit): 
Please input directory to search (q to quit):
```

-   根据用户输入的扩展名和目录，递归搜索所有扩展名匹配的文件，将其路径输出到屏幕（绝对/相对路径都可以）。
-   若文件路径是绝对路径，且以家目录开头，将整个家目录替换成`~`

> 注意：[环境变量](https://zhuanlan.zhihu.com/p/557885534 "环境变量")`$HOME`就是家目录的绝对路径。在终端中，可以用`echo $HOME`查看家目录的绝对路径。在bash脚本中，同样使用`$HOME`来指代家目录的绝对路径。

```text
$ echo $HOME
/c/Users/<user name>     # git bash
/home/<user name>        # linux
```

> 示例：将以家目录开头的目录替换为\~开头：

```text
/home/fracher/code/test.c   ->   ~/code/test.c
```

-   输出一共有多少个文件
-   从第一步开始重复，直到用户输入q

### 附加要求

-   使输出更加好看，可以在echo时为文本[添加颜色](https://zhuanlan.zhihu.com/p/181609730 "添加颜色")。
-   此脚本不符合Unix哲学，即一件工具只做一件事。要求使用参数来控制该脚本的行为。仅当参数为`--interactive`时，才进行上面的轮询，否则仅根据参数进行一次搜索。如：
    ```bash
    $ ./search_file.sh --extension docx --directory ./Documents
    ./Documents/file1.docx
    ./Documents/file2.docx
    Total 2 files.
    $ ./search_file.sh --interactive
    Please input file extension (q to quit): ...
    Please input directory to search (q to quit): ...
    ...
    $ ./search_file.sh --help               # 输出帮助信息
    search_file.sh is a script to search files in a particular directory.
    USAGE:
    search_file.sh [OPTIONS]
    ... ... ...

    ```
    注：帮助信息的样例可以参考系统中的命令的帮助信息，如：
    ```bash
    $ ls --help
    $ cp --help
    ```
    简单写一点即可，不必过于详细。

### 可以参考的项目

-   Fracher的 [配置文件管理器](https://github.com/FrozenArcher/dotfiles/blob/main/dot "配置文件管理器")
-   [i3lock-fancy](https://github.com/meskarune/i3lock-fancy/blob/master/i3lock-fancy "i3lock-fancy")

### 另编

Vim之父 Bram Moolenaar 于2023年8月3日去世。让我们深切悼念这位开发者，他为自己的人生写下了最后一句 ":wq"。