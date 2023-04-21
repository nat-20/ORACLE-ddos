#!/usr/bin/python

#-------------------------------------------------------
#----------------- By: SEBASTIAN GOMEZ -----------------
#-------------- Universidad de Antioquia ---------------
#-------------------------------------------------------

import argparse

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo

from bmv2 import ONOSBmv2Switch, ONOSHost
from stratum import StratumBmv2Switch

CPU_PORT = 255
pipeconf_name = "org.p4.template"

#----- Niveles de debug que permite BMV2 -----
loglevel0 = "trace"
loglevel1 = "debug"
loglevel2 = "info"
loglevel3 = "notice"
loglevel4 = "warn"
loglevel5 = "err"
loglevel6 = "critical"
loglevel7 = "alert"
loglevel8 = "emerg"


class TutorialTopo(Topo):

    def __init__(self, *args, **kwargs):
        Topo.__init__(self, *args, **kwargs)

        s1 = self.addSwitch('s1', cls=StratumBmv2Switch, grpcport=50001, thriftport=60004,
                               cpuport=CPU_PORT, pipeconf=pipeconf_name, loglevel=loglevel1) 

        # IPv4 switches
        h1 = self.addHost('h1', cls=None, mac="00:00:00:00:00:01",
                           ipv4='10.0.0.1/32')
        h2 = self.addHost('h2', cls=None, mac="00:00:00:00:00:02",
                           ipv4='10.0.0.2/32')

        # Host Links
        self.addLink(h1, s1)  # port 3
        self.addLink(h2, s1)  # port 4


def main(argz):
    topo = TutorialTopo()
    controller = RemoteController('c0', ip=argz.onos_ip)
    #controller = RemoteController('c0', ip='127.0.0.1')

    net = Mininet(topo=topo, controller=None)
    #net = Mininet(topo=topo, controller=lambda name: controller, listenPort=6633)
    net.addController(controller)

    net.start()
    CLI(net)
    net.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Mininet script for 2x2 fabric with BMv2 and IPv6 hosts')
    parser.add_argument('--onos-ip', help='ONOS controller IP address',
                        type=str, action="store", required=True)
    args = parser.parse_args()
    setLogLevel('info')

    main(args)
