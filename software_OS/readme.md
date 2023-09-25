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

After that please follow this
