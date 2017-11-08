

# 1602
1602
```
sudo apt-get install i2c-tools python-smbus
```
```
sudo i2cdetect -y 1
```
```
git clone https://github.com/makeabignews/1602.git
```
```
sudo nano /etc/rc.local 
```
add:
``
su root -c "/usr/bin/python /home/pi/1602/server.py"
``

 ```
 sudo chmod +x server.py
 ```
``
reboot
``


添加到计划任务
#为脚本增加可执行权限
```
#将脚本加入cronjob（计划任务）
sudo crontab -e
#在cornjob文件中添加下面一行，并保存(表示10分钟执行一下脚本，时间可自行修改)
*/10 * * * * /home/pi/show.py
