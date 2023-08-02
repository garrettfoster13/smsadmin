# smsadmin


```
└─# python3 smsadmin.py -h                                                                                               
usage: smsadmin.py [-h] [-t TARGET] [-tu TARGETUSER] [-s SID] [-u USER] [-p PASSWORD]

Remotely add Site Server Admin

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target site server IP or hostname.
  -tu TARGETUSER, --targetuser TARGETUSER
                        Target Username.
  -s SID, --sid SID     Target user's SID.
  -u USER, --user USER  Site Server Admin Username.
  -p PASSWORD, --password PASSWORD
                        Site Server Admin Password or Hash (LMHASH:NTHASH
```
### Installation
```
git clone https://github.com/garrettfoster13/smsadmin.git
cd smsadmin
pip3 install -r requirements.txt
```
