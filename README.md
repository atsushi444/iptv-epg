# EPG
## 配置方法:  
### 环境：Python,Openwrt  
### 步骤：  
#### 将源程序上传到Openwrt web根目录  
#### 设置定时任务：crontab -e   
#### 设置每天12点更新：00 00 * * * /usr/local/bin/python main.py  
### 注意：   
运行脚本后会在当前目录生成 *.xml节目表，URL与实际所放的Web路径有关  
