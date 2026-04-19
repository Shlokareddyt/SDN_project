from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet.ipv4 import ipv4

log = core.getLogger()

class TrafficClassifier(object):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)
        # Initialize our traffic counters
        self.tcp_count = 0
        self.udp_count = 0
        self.icmp_count = 0

    def _handle_PacketIn(self, event):
        print("\n!!! I SEE A PACKET !!!\n")
        packet = event.parsed
        if not packet.parsed: return

        # 1. Let ARP packets pass through! (Crucial for hosts to find each other)
        if packet.find('arp') is not None:
            msg = of.ofp_packet_out()
            msg.data = event.ofp
            msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
            self.connection.send(msg)
            return

        # 2. Look for IPv4 traffic to classify
        ip_packet = packet.find('ipv4')
        if ip_packet is None: return # Ignore other random non-IP traffic

        # 3. Match & Action Setup (The OpenFlow Rule)
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 10
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))

        # 4. Classification Logic
        if ip_packet.protocol == ipv4.TCP_PROTOCOL:
            self.tcp_count += 1
            log.info(f"*** TCP Packet Detected! Total TCP: {self.tcp_count} ***")
           
        elif ip_packet.protocol == ipv4.UDP_PROTOCOL:
            self.udp_count += 1
            log.info(f"*** UDP Packet Detected! Total UDP: {self.udp_count} ***")
           
        elif ip_packet.protocol == ipv4.ICMP_PROTOCOL:
            self.icmp_count += 1
            log.info(f"*** ICMP Packet Detected! Total ICMP: {self.icmp_count} ***")

        # Push the rule and the packet back to the switch
        msg.data = event.ofp
        self.connection.send(msg)

def launch():
    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        TrafficClassifier(event.connection)
    core.openflow.addListenerByName("ConnectionUp", start_switch)
