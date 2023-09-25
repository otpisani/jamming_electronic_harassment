All this amplifiers I bought personally, some of them work, and then died, some of them I couldn’t start
even from start

Amplifiers for outside/backpack

[2W amplifier](https://www.aliexpress.com/item/1005004055558726.html?spm=a2g0o.order_list.order_list_main.285.66ae1802u
s3Maj), I didn’t bought that amplifier when I buy accumulator battery 12.6V, 15Ah, just for outside
perpose This amplifer work some time in my flat, and it’s doing good job, it’s linear amplifier, and 
jamming line when amp is on, can actually boost gain for around 33dBm, but didn’t last very long, it have
passiev cooler, but presume that you need to put bigger passive radiator



[4W amplifiers](https://www.aliexpress.com/item/1005004349939985.html?spm=a2g0o.order_list.order_list_main.74.21ef1802bGcr8w)
I also have this one, still didn’t use that in practise for longer period, what I know when I connect it 
on power supply aorund 18-19V, with regulated voltage and current from 0-120V and 0-5A,this power supply
will not last for a lo ng time, because it’s heat a lot, also another buyer publich comments that it’s not
recommended to put voltage more than 20V, and/or that you put bigger passiev radiator

For that amplifer you will need [ voltage booster](https://www.aliexpress.com/item/1005001622004014.html?spm=a2g0o.order_list.order_list_main.62.21ef1802bGcr8w), if you plan to supply ampliefer with more than 12.6V


 Amplifiers for home

This is amplifier that I mannage to know better, and on which I spend most of the time playing with amplifiers

45W amplifier both in DIY kit and alreydy buoild with passive radiator, in DIY kit you will not get passive
radiator

Or this one, which is the same as build amplifier, if you chech closer DIY kit from above, you will se 
that it’s some previous amplifer build number

https://www.aliexpress.com/item/1005002362165650.html?pdp_npi=3%40dis%21USD%21US%20%2419.11%21US%20%2413.76%21%21%21%21%21%402101ef6816921179106696335efe50%211
2000020317776876%21im%21%21

https://www.aliexpress.com/item/1005002222653277.html?spm=a2g0o.order_list.order_list_main.279.1dc41802h
2qLgD

Step voltage [down regulator](https://www.aliexpress.com/item/1005004983920053.html?spm=a2g0o.order_list.order_list_main.140.1dc
41802h2qLgD ), for outside, if you will buy battery accumulator Litium 18650, which is much 
better than lead batteries, they last longer and they are much lighter for carrying arround, 12.6V Lithium
battery 15Ah, weight around 450g, same lead batteries around 5kg. Step down voltage regulator is needed if 
you will connect raspberry pi 3B+ operate on 5.1-5.2V, or amplifiers which uses 5V power supply

Somewhere in manual states that just PCB board with elements will use around 250mA, and when you solder 
mosfets, the both need to be configure with trimmers to have around 30-35mA per gate side.
If you will buy already build 45W amplifier you will notice that trimmer is very bad for configuring, but 
beacuse it's have very small foot print, there is not much option for replacing, but you can find better trimmers which
are just for fine tuning and they need to be 5KΩ or 10KΩ

https://duckduckgo.com/?q=multi+turn+trimmer+potentiometer&iax=images&ia=images


25W amplifiers

This would be almost pro amplifier with heat thermostat regulator, which starts active fan, mosfet 
inside is this XRPA mosfet 841-MRFE6VS25NR1 

600W
and last amplifer that I bought, still didn’t test it, it's monster 600W, and this is serious gear. 
For that you need special active and passive radiator, and building installation is here, I manage to fry 
300BN mosfets, and still can’t regulate bias current, so I’m waiting to come bigger passive radiator,
and copper plate

[Building manual](https://www.nxp.com/company/blog/homebrew-rf-design-challenge-winners:BL-HOMEBREW-RF-DESIGN-CHALLENGE-WINNERS?spm=a2g0s.imconversation.0.0.6e913e5fTA2gwg#iw_comp1596645344954), but you need part when he put thermo past, but also conductive, bigger radiator and 
copper plate, also this guy is presume ham operator, and he actually won sonme award from XRP mosfets 
manufacturer for he’s amplifier design.
