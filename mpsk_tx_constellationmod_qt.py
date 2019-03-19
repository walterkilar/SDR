#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MPSK Transmitter
# Author: Walt Kilar
# Generated: Mon Mar 18 20:18:48 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sip
import sys
from gnuradio import qtgui


class mpsk_tx_constellationmod_qt(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MPSK Transmitter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MPSK Transmitter")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "mpsk_tx_constellationmod_qt")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate = samp_rate = 32000
        self.qpsk_const = qpsk_const = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 2, 2, 1, 1).base()
        self.excess_bw = excess_bw = 0.35
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'QT GUI Plot', #name
        	5 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	5 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.digital_constellation_modulator_0_1 = digital.generic_mod(
          constellation=qpsk_const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0_0_0 = digital.generic_mod(
          constellation=qpsk_const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=1.0,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
          constellation=qpsk_const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.5,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
          constellation=qpsk_const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.22,
          verbose=False,
          log=False,
          )
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=qpsk_const,
          differential=True,
          samples_per_symbol=sps,
          pre_diff_code=True,
          excess_bw=0.1,
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 1000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.qtgui_const_sink_x_0, 3))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.digital_constellation_modulator_0_0_0_0, 0), (self.qtgui_const_sink_x_0, 4))
        self.connect((self.digital_constellation_modulator_0_0_0_0, 0), (self.qtgui_freq_sink_x_0, 4))
        self.connect((self.digital_constellation_modulator_0_1, 0), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.digital_constellation_modulator_0_1, 0), (self.qtgui_freq_sink_x_0, 2))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "mpsk_tx_constellationmod_qt")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_qpsk_const(self):
        return self.qpsk_const

    def set_qpsk_const(self, qpsk_const):
        self.qpsk_const = qpsk_const

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=mpsk_tx_constellationmod_qt, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
