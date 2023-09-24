Mostly you will need osmocom sink which you need to install separately, package name is gnuradio-osmosdr (can have different name depends about linux dis), although hackrf and LimeSDR also have soapy sink, soapy is like emulator, but osmocom can run in "soapy mode", that would be about you, whats batter suits you best solution for you, depends a lot of python version, errors that you will have, number one rules is !!!!don’t ever update OS which is just for jamming!!!!

option to put in osmocom block under device arguments 

driver=hackrf 

is not relevant if you only have one device, but if you have multiple version of hackrf or lime, you need to tell on which hardware you meant when you choose osmocom sink, if you going emulate soapy mode within osmocom sink you need to enter also

soapy=0,serial=, driver=lime or hackrf

for serial you will enter 

hackrf_info or 

LimeUtil –find

Because soapy will not run if you don't specify serial number, you can see that sample block is prepared for hackrf before, Ch0 is center frequency, from which on both side starts ½ of bandwidth, hackrf also have two tx option for transmition gain, ch0 Rf and ch0 IF, both parameter you can find with soapy commands 

SoapySDRUtil --probe=driver=hackrf, 

Ok after some issues presume double install of soapysdr true source and/or repository

when you enter 

SoapySDRUtil --probe=driver=hackrf, just scroll under tx results

    Full gain range: [0, 61] dB
    VGA gain range: [0, 47, 1] dB
    AMP gain range: [0, 14, 14] dB

last number means that you can raise gain by 1 with vga if gain, and with amp or if rf you can choose only 14 or nothing or 0, bandwidth is 28.0e6, when you enter 28 MHz, you will need to enter
28.0e6

For lime, you will enter only if gain, which can be from -12 to +64, and this parameters you can also get with 

SoapySDRUtil --probe=driver=lime


besides osmocom sink you can also choose soapyhackrf or soapylimesdr

Now I choose to run jamming with both gaussian and uniform classic, mode, but also like I said you have noise fast, you can sure run scripts with grc extension, but than you need to install X desktop on linux, if you don't install, to run script under terminal, you need to change this, 

run without GUI, also you need to check if block by himself can actually run in terminal without GUI, but if you see red line within blocks, means that you have some kind of error, AND THIS IS ALL FROM SOFTWARE SIDE TO RUN JAMMING WITH PC OR RASPBERRY WITH HELP OF HACKRF OR LIME


So to run script under terminal with python you just need to enter command

python3 -uuu name of the script in my case test_purpose.py     

python3 -uuu test_purpose.py

With sudo usb_top you can check if script actually runnning, and you can see how much samples hackrf can handle, and it's only usb 2.0, in case of lime, that will be with USB 3.0 cable around 300Kb/s >

before sudo usbtop you need to insert module usbmon

sudo modprobe usbmon but do that on start or boot
