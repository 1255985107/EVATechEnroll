# 4. 204什么情况？- Backend

根据传统，老东西们会在204门口的电闸上贴上一个便利贴，写着“都别动！动会死！”。因为协会在自闭间有三台服务器，其中一台服务器上运行着EVA File、EVA Wiki等各种重要的网络服务。如果断电了，协会的部分网络服务无法正常运行，也有可能会损伤服务器硬件。但是，如果碰到了突发情况，又没有人在204，如何方便得知204服务器运行的状态呢？

我们可以在另一台较可靠的服务器（如云服务器）上搭建一个简单的服务端，并让204的服务器定时向云服务器发送请求。如果云服务器那端验证是204服务器发送过来的请求，那么就更新时间戳。如果过了一定时间（如：5分钟）没有来自204服务器的请求，那么就说明204的服务器可能出了问题，需要去检查情况了。

现在，就请你根据以上描述搭建一个简单的云端监测服务吧！

### 你的任务

在本地搭建一个服务端，并完成以下需求：

| **需求**  | **需求描述**                            | **HTTP路由**      |
| ------- | ----------------------------------- | --------------- |
| 检验网络连通性 | 服务端在接收到客户端发来请求后返回成功提示               | `[GET]` /ping   |
| 更新时间戳   | 服务端在接收到待检测服务器发送的请求后返回更新情况           | `[POST]`/check  |
| 查询更新时间  | 服务端在接收到客户端发送的服务器名称后返回上一次更新时间、以及是否失联 | `[POST]`/status |

-   **通用格式**：
    所有的返回值都需要符合以下格式：
    ```json
    {
        "code": 0,       // 错误码，非 0 表示失败
        "msg": "",       // 错误描述
        "data":
          {
              ...        // 数据主体中的具体内容
          },
    }
    ```

在后续的返回值格式描述中，我们将**略去通用部分**，只描述数据主体（即 data 部分）的格式。

-   `[GET]`/ping
    **返回值**：
    ```json
    {
        "msg": "pong"
    }
    ```
    
-   `[POST]`/check
    **请求体**：
    ```json
    {
        "source": "ZJUEVA204", // 待监测服务器名称，你可以自拟
    }

    ```
    **返回体**：
    ```json
    {
        "isChecked": true,     // 是否更新时间戳
    }
    ```
    **可能的错误信息**：
    1.  服务器未在监测列表内
        ```json
        {
            "code": 100,
            "msg": "Server not authorized",
            "data":
              {
                  "isChecked": false,
                  ...
              },
        }
        ```
    2.  请求未提供服务器名称
        ```json
        {
            "code": 101,
            "msg": "Should have a server name",
            ...
        }
        ```
    
-   `[POST]`/status
    **请求体**：
    ```json
    {
        "server": "ZJUEVA204", // 待检查服务器名称，你可以自拟
    }
    ```
    **返回体**：
    ```json
    {
        "lastTime": "1984/10/01 11:45:14", // 按照"yyyy/mm/dd hh:mm:ss"的格式返回
        "isDisconnected": true,            // 是否失联
        "hitokoto": "你好呀，祝你满绩每一天"  // （选做）一言 API 返回的语句
    }
    ```
    不要求错误处理。

    你可以适当减少监测间隔时长以方便调试。

### 附加题

- 将服务器名称链接数据库，形式不限，数据自拟即可。
- 当访问`/status`路由时从一言API拉取语句数据再发送给客户端，你可能要再自拟一些错误情况处理。

### 一些需要注意的事

本题不做语言限制，你可以用任何你喜欢的编程语言完成这一题。如果你没有头绪的话，可以试试
Go的Gin框架，或者Nodejs的express包，Python与C#也是一个不错的选择。~~C++也不是不行~~
服务只需要在本地运行，不必上传至服务器，提交时提交源码即可。

### 参考资料

-   [Nodejs](https://nodejs.org/en/docs/ "Nodejs")
-   [Express](https://expressjs.com/ "Express")
-   [The Little Go Book](https://www.openmymind.net/assets/go/go.pdf "The Little Go Book")
-   [Gin](https://gin-gonic.com/ "Gin")
-   [What is Hypertext Transfer Protocol (HTTP)](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "What is Hypertext Transfer Protocol (HTTP)")
-   [HTTP Tutorial](https://www.runoob.com/http/http-tutorial.html "HTTP Tutorial")
