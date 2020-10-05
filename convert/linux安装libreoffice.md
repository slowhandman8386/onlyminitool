### linux安装libreoffice 

```shell
#删除久的
yum remove libreoffice-*

#需要安装java
yum -y install java-1.8.0-openjdk*

#从官方下载最新的
https://www.libreoffice.org/download/download/

tar xvf LibreOffice_6.2.5.2_Linux_x86-64_rpm.tar.gz
cd LibreOffice_6.2.5.2_Linux_x86-64_rpm/RPMS/
yum localinstall *.rpm

yum install cairo cups-libs libSM -y
yum install ibus -y
yum install libreoffice-headless -y

#输入命令 有显示 就安装没问题
libreoffice -help

#字体乱码问题
https://zh-cn.libreoffice.org/download/fonts/
```

### 转换命令

```shell
libreoffice6.4 --invisible --convert-to pdf /opt/ipad.docx

# --outdir 指定路径
libreoffice6.4 --invisible --convert-to pdf /opt/ipad.docx --outdir /opt


```

