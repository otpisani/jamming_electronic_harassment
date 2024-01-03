# jamming_electronic_harassment
jamming electronic harrasment at home, flat, outside

Main frequency which is actually multi chanell, presume for microphone (vocoder), maping human body is around 24.35MHz, beacuse band from 0-30MHZ is military and/or maritime, need to be some military signal, bandwidth is around 700-800KHz, although could be less, antenna is in apartment, RTL card is excellent specially made for HF band, but it's "fine tuning science", measuring need to be outside, so that line could be even parasitic/ghost signal, but this is it for sure, there is couple of known military modulation operating with in that bandwidth according to [sigidwiki](https://https://www.sigidwiki.com/wiki/Category:Military). That frequency jump out recently somehow when I jamming whole apartment. Software is SDR++ on linux, with SDR card airspy HF+, with active loop antenna, bought on Ali, but loop is made from cooper tube for radiators heaters.![MKULTRA](https://github.com/otpisani/jamming_electronic_harassment/assets/4509181/c5420226-7d3a-411a-9a26-b1c20f744e75)

What is not working as it should, that you just turn on some noise, in GNUradio that would be uniform or gaussian, and than that looks like this, that signal is flatten, jammed but not good enough, no matter if I change noise source every 60s, like this
while true; do
timeout -s 9 60s /home/otpisani/limeSDR-grc_uniform_24332_classic.py
timeout -s 9 60s /home/otpisani/limeSDR-grc_gaussian_24332_classic.py!
#timeout -s 9 30s python3 -uuu ~/Downloads/hackrf_osmo_104_gaussian_classic.py
#timeout -s 9 30s python3 -uuu ~/Downloads/hackrf_osmo_104_uniform_classic.py;
done
jamming signal is above biggest pick signal that I try to jam, but is not good enough
![uniform_flat_line](https://github.com/otpisani/jamming_electronic_harassment/assets/4509181/97e86561-7853-4c70-b48b-2dd8ab5b3cf9)

But actually what is works is this:

What is working actually is that you put with in py script randomize power gain, which pulses between min and max gain that you configure in script, also better effect is that you cutoff min and max frequency that you plan to jam, and it's looking
![pulsing_randomize_gaussian](https://github.com/otpisani/jamming_electronic_harassment/assets/4509181/9c2734cf-8897-4078-bca8-bdfc9212790a)

Whole video is ![here](https://github.com/otpisani/jamming_electronic_harassment/blob/main/gnuradio-companion_in_action/randomize_power_gain)

and py script file with randomize power gain is ![here](https://github.com/otpisani/jamming_electronic_harassment/blob/main/gnuradio-companion_in_action/grc_files/24.35_randomize_power_gain_hackrf.py)

!!!Older idea!!!
!!!It would be nice that other contribute also!!!. I never have chance to try hackrf [portapack](https://hackaday.com/2020/11/28/hackrf-portapack-firmware-spoofs-all-the-things/), for people which doesn't know what porta pack actually is, is upgrade, or hardware module in which can be placed hackrf, battery and also has small LCD display with arrow like in game pad, instead mouse, for example. On the first glance it's kids tool, but can actually replace carrying big Li ion battery in the backpack, because newest version have also option to charge battery true USB port. What I don't know what is computation power, because portapack uses arm CPU, which is in hackrf device, and author of hackrf one Mossman didn't predict that, more to use hackrf one as SDR device in PC, so I don't know what is actually computation power comparing with PC, I can say with that raspberry pi4 is far more powerful (and it's actually Arm but octal CPU core), than mine AMD A8-3850 CPU in old PC. Further more, porta pack is useless unless you don't upgrade firmware like [mayhem](https://github.com/eried/portapack-mayhem) firmware, which has already build inside RX and TX different modulation, and you don't need to use software like, Angel,Gqrx or gnu-companion, because everything is in the firmware, but again don't know if you can run successfully jamming of 20MB bandwidth, plus is to avoid bottle neck which is USB cable A-micro B used for connection between raspberry pi and hackrf, no matter what cable you bought after some time you will going to lost connection with hackrf!!!??? 
Porta pack and smaller external amplifier can replaced big lithium battery, but again this need to be tested yet.

That would be active jammer against human radar, which cause all synthetic disease, pain, made by another frequency operate on much bigger band, microwave. You can describe that as laser which is in the hand of Navy Seal operator on the ground, marking target, and in the same time, fighters above drops, smart bomb on target, efficient is from 90% >. 

I first invest in passive shielding, and this days still combine passive shielding and active jammer based on SDR device HackRF One Card, and also have LimeSDR USB, card, and both of them are Chinese clones, because Lime but also HackRF are product from crowd funding campaigns, but HackRF are still exist, Lime are gone for years, and Lime was chipper version of URP device, which are much expensive. Biggest differences between HackRF and Lime is that hackRF one is 12bit card, uses old 2.0 v USB, which is slower comparing with Lime 3.0 USB, hackrf can do 20MS/s with 28MHz bandwidth, and Lime can do 60MS/s per TX channel (has two of them) with 120MHz bandwidth. You notice that bandwidth, it is actually area of some band that one card can cover, so 120MHz is better that 28MHz, but that again, you only need to cover HF band, or 0-30MHz. I’m focusing on jamming that „Navy Seal” operator on the ground who actually marking my body, WHOLE fucking day, never mind, if I'm on the street or back home in my flat. We will not cover here Microwave, which operate on bigger band, and thy are not of much importance for me. As human if we are targeted with microwaves, which operates on that bigger band, we will be dead already, much bigger frequency means bigger dissipation of energy, so it's very simple practice example. If you enter into big electronic store with radio devices, they operate on FM band, if you pass true the shells with radio devices, they will all start to make that nice sound of jamming, you know we have big station operate on 88.10 MHz back home, and if I turn on jammer, they will made the same sound when you passing shells with radio devices, and „Navy Seal” operator is whole day behind you marking your body with logarithmic antenna or some other direct antenna.

###[software_os](https://github.com/otpisani/jamming_electronic_harassment/blob/main/software_OS/readme.md)
###[antennas](https://github.com/otpisani/jamming_electronic_harassment/blob/main/antennas/readme.md)
###[amplifiers](https://github.com/otpisani/jamming_electronic_harassment/edit/main/amplifiers/readme.txt)
###[hackrf changes](https://github.com/otpisani/jamming_electronic_harassment/tree/main/SDR_cards/hackrf/changes_that_you_need_to_do)

