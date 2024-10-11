# 6.网络蜘蛛侠 - spider

小钱同学是一个医学专业的小e，很多时候需要搜索文献，但是人工手动搜索文献效率太低了，小钱同学就想着能不能通过一个自动程序来将相关的搜索结果以 **文献标题：文献链接** 保存为为一个.txt的文件中。

### 你的任务

-  将[Nature](https://www.nature.com/ "Nature")上的文章的文献标题和文献链接保存下来，比如 
```text
Fratricide-resistant CD7-CAR T cells in T-ALL : https://www.nature.com/articles/s41591-024-03228-8

A CAR enhancer increases the activity and persistence of CAR T cells : https://www.nature.com/articles/s41587-024-02339-4
```
这样两行，搜索的关键词可以自定义，如`CAR-T`。
-  你所需要提交的包括一个.txt文件和相应的源代码（建议使用python）。

### 一些可能有助于完成项目的小提示：

-  某些网站可能存在反爬虫的策略，为了更好的得到数据，可以使用chromedriver + python中的`selenium`包 来模仿用户行为，selenium相关教程可以参考[这个网站](https://selenium-python-zh.readthedocs.io/en/latest/getting-started.html "这个网站")。
-  Nature的web源代码可能比较多，可以在查看网页源代码的同时使用ctrl + F 来搜索自己感兴趣的的地方（比如网址）。
-  在page source 中获取自己感兴趣的内容（文献标题与文献链接），可以使用 `BeautifulSoup` 包来解析，也可以使用正则表达式来匹配，BeautifulSoup相关教程可以参考[这个网站](https://beautifulsoup.readthedocs.io/zh-cn/v4.4.0/ "这个网站").

### 附加题

1. 实现从一页相关的搜索结果拓展到10页，将10页中的`文献标题：文献链接`内容都下载下来。
2. 实现不仅仅只获取文献链接，将文献链接所指的PDF也下载到本地。