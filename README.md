# EPG
## 利用央视网节目单json接口抓取CCTV1-CCTV15一周内节目单  
可用于Perfect Player IPTV 等支持xml节目表的IPTV播放器  
## 配置方法:  
### 环境：Python,Openwrt  
### 步骤：  
#### 将源程序上传到Openwrt web根目录  
#### 设置定时任务：crontab -e   
#### 设置每天12点更新：00 00 * * * /usr/local/bin/python main.py  
## 使用方法：  
#### IPTV播放器设置节目单网络源 http://路由器IP/CCTV_EPG.xml即可获取节目表  
### 注意：   
运行脚本后会在当前目录生成 *.xml节目表，URL与实际所放的Web路径有关  
