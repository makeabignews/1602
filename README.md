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
su root -c "/usr/bin/python /home/pi/1602/show.py"
``
``
reboot
``
