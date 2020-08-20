# ORACLE

ORACLE: c**O**llabo**R**ation of d**A**ta and **C**ontrol p**L**an**E**s to detect DDoS attacks in a Software-Defined Networking (SDN) architecture. This DDoS detection system is composed by two modules: a control plane implementation developed in an **ONOS** controller, and a data plane implementation developed using the **P4**.  In order to communicate both planes is used the P4Runtime interface which allows controlling in real-time the data plane elements of a p4 device.

## Getting Started

These instructions will guide you to run the detection mechanism under an ONOS+P4 experimental scenario. We recommend using an Ubuntu 18.04 virtual machine.

### Prerequisites

To run the DDoS detection system is needed to install at the virtual machine the following dependencies:

- [ONOS](https://wiki.onosproject.org/display/ONOS/Development+Environment+Setup "ONOS")
