So I made jammer based on HackRF One SDR radio, at home it's power with some old PC based on AMD CPU from 2013, and for outside I'm using Raspberry PI 3b+, which can compute more for 10-15% than old AMD CPU PC machine. When is connected with power jack (not on battery). Sure TX gain that you will get with Hack RF and/or Lime is not enough for that, you will need to amplify signal, think that Hack RF and Lime can't give you [gain](https://hackrf.readthedocs.io/en/latest/faq.html) more that 13-15Dbm between 0-30MHz or HF band that we need to jam, so you need amplifier, and I do a lots of searching around the net, but first I like to pint out, you will need much bigger amplifier for home, house or flat, comparing to amplifier for outside, and that all can fit in one backpack. I plan to made this as technical tutorial. 

I'm good at linux on admin level, and good PC technician, also because people who fucks me all day 24/7 knows what I'm doing, and they know that I will finally get them with that, they just sabotage everything, so basically I couldn't find electrician guy in city with 800k inhabitants, why because when I start to play with amplifiers, and this is devices that are pretty simple, with few electronic elements, and operate basically with lower input power at the end or output MA port they will produce 10, 20,30 time more power than on input, so all amplifiers have one and only issue, great heat dissipation, means the will fry like pop corn, and until now I fried more than 10 of them, so when someone sabotage you, I start to play with soldering, and I learn how to fix that 45W amplifier on my own, and also can build YID kit on my own. 
Shortly, if you manage to control heat, amplifier will work better and long life, also if you have amplifier with greater output power, more than 45W, you can't travel with that in backpack, also you don't need that outside, because that stupidity that this folks do is to announce you where ever you go, in the bar, library, at job, and if someone smiles at you, you will feel pain, great disorder in the head, angry and son on, it's all arranged, but if you have active jammer, there is no purpose for announcing, no matter where do you go, you can have just amplifier from 1W, I'm using right now amplifier that I will show later from 45W, just because I fried that smaller amplifiers from 1W or 2W.   

For PC or raspberry pi, I'm using Linux, sorry Linux will be covered here only. Presume that most of you will use Ubuntu or rasbian pi, I'm using arch Linux, main difference is that they are using different commands for installing something, but also arch Linux has great tutorial, and don't have all necessary packages that Ubuntu have with default installation, equals lower hardware drains.

I will not cover Arch installation here, more arch Linux pi for raspberry.
Instructions presume that you already have some installation of Linux, and that you have SD reader card on your laptop, although more that you will have that by default on older laptops. When you put SD card inside, sorry micro SD in Card adapter, you need  to find out first name of your micro SD device.

Sudo fdisk -l 

and you will looking something like this  mmcblk0

No matter if you have new or old micro SD card, first you need to delete MBR records from beginning of the card

 sudo dd if=/dev/zero of=/dev/mmcblk0 bs=512 count=1

Although in manual they will recommend using specially image for raspberry pi 2, I install also specially 64bit made just for raspebrry pi 3b+, but they say that is not full covered with support.

After that please follow this [manual](https://archlinuxarm.org/platforms/armv7/broadcom/raspberry-pi-2)
wget http://os.archlinuxarm.org/os/ArchLinuxARM-rpi-aarch64-latest.tar.gz

After installation you can put micro SD card into raspberry, and you can boot system without monitor, and you can connect true terminal with ssh

ssh alarm@ipaddress that router attach for arch pi

you can look on router which all have web interface, what he dedicate for arch pi, because arch pi have dhcpcd client enabled by default, but you can always found out IP address with command sudo rap -a -i hardware device that you will scan, usually eth0

you need to install only this packages to arch pi, to be able to run gnu radio python script with hacker or Limescale, I list mine packages with command pacman -Qe
archlinuxarm-keyring 20140119-2 
base 3-1 
base-devel 1-1 
cmake 3.27.5-1 
dhcpcd 10.0.2-1 
dialog 1:1.3_20230209-1 
git 2.42.0-1 
gnuradio 3.10.7.0-5 
gnuradio-osmosdr 0.2.4-7 
hackrf 2023.01.1-1 
htop 3.2.2-1 
limesuite 22.09.1-3 
linux-rpi 6.1.53-1 
mc 4.8.30-1 
nano 7.2-1 
net-tools 2.10-2 
netctl 1.28-2 
openssh 9.4p1-4 
pkgfile 21-2 
raspberrypi-bootloader 20230914-1 
raspberrypi-firmware 20230914-1 
soapyhackrf 0.3.4-1 
sudo 1.9.14.p3-1 
tmux 3.3_a-7 
usbtop 1.0-1 
usbutils 015-3 
vi 1:070224-6 
which 2.21-6 
wireless-regdb 2023.09.01-1 
wireless_tools 30.pre9-3 
wpa_supplicant 2:2.10-8 
yay 12.1.2-1

packages marked with Italic are installed specially by me, other you will get with installation, cmake is tool for compiling if you want to compile let say latest hackrf packages or SoapySDR, although you don’t need that because you will get latest package with pacman installation pacman -Sy hackrf
hackrf is utilities made by hackrf team with Mosmman, for running python scripts, you also need gnuradio 3.10.7.0-5 
gnuradio-osmosdr 0.2.4-7 soapyhackrf tmux is emulator on which you can open command true ssh session and command will not be terminated after you leave ssh session with [shortcuts](https://tmuxcheatsheet.com/) yay is package installer for third party software repository


Because you will not have monitor attached when you will have all that in backpack, you can only check some basics with mobile phone, if script is running, we will put script to auto boot when arch pi booting.

sudo nano /etc/systemd/network/wlan0.network and change file like this if it’s different 
[Match] 
Name=wlan0 

[Network] 
Description=On-board wireless NIC 
DHCP=yes 

or if you want to use static address

[Match] 
Name=wlan0 

[Network] 
Description=On-board wireless NIC 
Address=192.168.x.y 
Gateway=192.168.x1.y1 
DNS=192.168.x1.y1

with ip addr s you can check if you have more than one ip address attached to device wlan0 by your router or mobile phone hot spot, if you have means that also dhcpcd and service systemd-networkd are enable on boot by default, so you need to disable one of that service, but warning, if you disable wrong one, you will not have to attach back without monitor and keyboard attached on raspberry.

sudo systemctl disable dhcpcd 

but check if you have systemd-networkd enabled

sudo systemctl | grep systemd-networkd

you need to have configured wpa_supplicant to connect arch pi to wlan router or mobile hotspot, and you need to put file in this path

/etc/wpa_supplicant/wpa_supplicant-wlan0.conf if you using wlan0 interface,and this is basic what you need to put inside 

sudo nano etc/wpa_supplicant/wpa_supplicant-wlan0.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=wheel 


network={ 
       ssid="name of SSID" 
       psk="wpa key" 
       scan_ssid=1
       key_mgmt=WPA-PSK 
}

you can enable all interface to boot with sudo systemctl enable systemd-networkd, or just one of tham, wlan for example  sudo systemctl enable systemd-networkd@wlan0

Now you need to put python script to start execute when arch pi starts, and again we will use systemctl service for that to start at boot time, another method would be execute script at boot time with cronie @reboot name of the command or script.

sudo nano /etc/systemd/system/name_of_the_service

you than need to place inside just path where is the script 

Unit] 
Description=Script 

[Service] 
ExecStart=/usr/bin/bash /home/your-account_name/name_of_the-script.sh 

[Install] 
WantedBy=multi-user.target


and after that 

sudo systemctl enable /etc/systemd/system/name_of_the_service

And Finally you need to put python script that you made before with gnuradio-companion GUI version of gnuradio, and guess what will be using inside gnuradio-companion as major blocks, noise-source, and also you have option fast-noise-source, everything you put inside “name_of_the-script.sh”, will actually do jamming process.


