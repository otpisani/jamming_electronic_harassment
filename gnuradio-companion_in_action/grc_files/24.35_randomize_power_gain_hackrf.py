#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Power-modulated Jammer
# Author: Pietro Tedeschi
# E-mail: ptedeschi@hbku.edu.qa
# Description: Power-Modulated Jammer
# GNU Radio version: v3.8.2.0-73-g4a84443c
# All rights reserved.

from gnuradio import analog
from gnuradio import gr
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time

import random


class pmj(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Power-modulated Jammer")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 8e6
        self.f0 = f0 = 24.95e6
        self.bw = bw = 1.5e6

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "soapy=0,driver=hackrf,serial=0909862dc2672b3cf"
        )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(f0, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(14, 0)
        self.osmosdr_sink_0.set_if_gain(16, 0)
        self.osmosdr_sink_0.set_bb_gain(0	, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(bw, 0)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                150.0e3,
                950.0e3,
                15.0e3,
                window.WIN_HAMMING,
                6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.osmosdr_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(20, self.samp_rate,  150.0e3, 950.0e3, 15.0e3, window.WIN_HAMMING, 6.76))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_f0(self):
        return self.f0

    def set_f0(self, f0):
        self.f0 = f0
        self.osmosdr_sink_0.set_center_freq(self.f0, 0)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.osmosdr_sink_0.set_bandwidth(self.bw, 0)

    def pulse(self):
        print('Press CTRL+C to stop the power-modulated jammer.')
        while True:
            time.sleep(1)
            self.osmosdr_sink_0.set_if_gain(random.randint(0,47), 0)



def main(top_block_cls=pmj, options=None):
    tb = top_block_cls()
    random.seed(0)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.pulse()
    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
