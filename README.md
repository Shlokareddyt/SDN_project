# SDN Traffic Classifier
An OpenFlow-based reactive traffic classifier implemented using the POX controller and Mininet.

## Problem Statement
Traditional network devices are "black boxes." This project implements a Software-Defined Networking (SDN) controller to inspect packet headers in real-time, classify traffic by protocol (TCP, UDP, ICMP), and demonstrate reactive flow management.

## Setup & Execution
### Prerequisites
- Ubuntu Linux
- Mininet
- POX Controller (Note: Recommended Python 3.8+)

### Steps
1. Clone the repo: `git clone https://github.com/Shlokareddyt/SDN_project/`
2. Move the classifier: `cp src/traffic_classifier.py ~/pox/ext/`
3. Start the Controller: `./pox.py log.level --DEBUG traffic_classifier`
4. Start Mininet: `sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633`
5. Verify: Run `pingall` in Mininet CLI.

## Expected Output
The controller will display real-time classification logs:
`*** UDP Packet Detected! ***`
`*** TCP Packet Detected! ***`
`*** ICMP Packet Detected! ***`

## Proof of Execution
-<img width="930" height="457" alt="image" src="https://github.com/user-attachments/assets/b979f332-0974-4cd5-93d0-81cb7df5863b" />
-<img width="803" height="427" alt="image" src="https://github.com/user-attachments/assets/0d9ca286-34db-4fe3-88a4-6b5c6da2d7de" />

-<img width="516" height="121" alt="image" src="https://github.com/user-attachments/assets/a1e35b14-c80b-4d32-b4b3-7dbd189562cc" />
-<img width="940" height="157" alt="image" src="https://github.com/user-attachments/assets/83bac7c0-d57d-4959-8e2c-f2f1f42dfa86" />

- <img width="893" height="717" alt="image" src="https://github.com/user-attachments/assets/7ccdfe53-51d2-44b9-821c-9432878c12b6" />

## References
1. McCauley, J. (2020). *POX Controller Documentation*. Retrieved from https://noxrepo.github.io/pox-doc/html/
2. Mininet Project. (2026). *Mininet Walkthrough*. Retrieved from http://mininet.org/walkthrough/
