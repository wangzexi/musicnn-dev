# 运行方法

为了方便测试，这里用 docker 打包了整个开发环境。docker 有点像一种轻量虚拟机。

## 启动环境

在**本目录**下运行如下命令：

```
$ docker run --rm -it -v $(pwd):/data wangzexi/musicnn
```

首次启动，将花费一些时间下载大约 1GB 的镜像文件。
容器启动后，终端就进入了拥有 python3.7 且安装好了 musicnn 等相关依赖的 Debain 环境。

## 运行分类脚本

```
$ python test.py
```

稍等片刻就能看到分类结果，修改 `test.py`，试试其他歌。

## 相关链接

[musicnn](https://github.com/jordipons/musicnn)
[在线音频编辑](https://www.bearaudiotool.com/tw/)
