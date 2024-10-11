# 1. 集装箱? - Docker

Docker是一种容器化技术，可以快速构建、测试和部署应用程序，相比于传统的运维，使用Docker可以解决“为什么在我的机器上跑得起来，在你的机器上不行呢？”等等一系列问题，同时也能够充分利用系统资源。当有一个DockerFile的时候，甚至不用去了解项目就可以部署它，那么，这么好用的东西...

### 你的任务
-  安装Docker(Windows, Linux都可)
-  使用Docker启动一个centos，并截图记录
-  尝试使用Docker挂载卷，并截图记录
-  使用Docker启动一个MySQL服务，并映射端口，截图记录

### 一些可能需要用到的命令：
-  `docker ps`： 列出Docker容器 
-  `docker run`： 创建并启动一个新的容器
-  `docker start/stop/restart`： 启动/停止/重启容器

相关的教程可以参考：
[Docker教程](http://www.dockerinfo.net/document "Docker教程")