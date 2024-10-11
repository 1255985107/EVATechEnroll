# 3. 网页小实践 - Frontend

请制作一个本地网页，实现一些简单的效果。要求如下：

> 功能要求：

-   这个网页有一个文本输入框和一个按钮，按钮上写着“生成”字样
-   在文本框中输入一个数字，按下“生成”按钮，下方会生成对应数量的小方块，小方块从左至右，从上至下以一定间距排列
-   左键点击小方块可以消除该小方块，其他小方块顺位排列填补空缺
-   在已经有生成小方块的情况下点击“生成”按钮，会在原有基础上增加相应数量的小方块

> 外观样式要求：

-   没有硬性要求，当然我们鼓励你按自己想法装饰网页

> 文件组织要求：

-   采用外置的JavaScript脚本和CSS层叠样式表
-   最终应该提交一个文件夹，内含一个.html文件，.css文件，一个.js文件。

***

样例：

1.  网页刚刚加载&#x20;

![](https://github.com/jeffreyqjf/zjueva-tech-joinus-internal/blob/master/img/p1_YDG9sgo3rv.png)

1.  在文本框中输入"3"并点击"生成"按钮

![](https://github.com/jeffreyqjf/zjueva-tech-joinus-internal/blob/master/img/p2_d8lLSjKqx0.png)

1.  左键单击最左侧的小方块&#x20;

![](https://github.com/jeffreyqjf/zjueva-tech-joinus-internal/blob/master/img/p3_zTbicgK-TB.png)

1.  再次点击"生成"按钮

![](https://github.com/jeffreyqjf/zjueva-tech-joinus-internal/blob/master/img/p4_Yd9bfVwRC0.png)

***

一些可能有助于完成项目的小提示：

-   小方块的长相和排列方式可以通过修改HTML元素"li"的样式获得
-   左键小方块使其消失的功能，需要在生成小方块时对每个小方块注册"onclick"事件
-   你可能需要学习一些基础的HTML、JS、CSS的语法，可以考虑参考[这个网站](https://www.runoob.com/ "这个网站")上的教程