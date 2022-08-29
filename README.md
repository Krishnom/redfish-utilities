### How to test with mock redfish api

#### setup python virtualenv
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

####  Start mock server
Open another shell and run below commands. 
```bash
git clone https://github.com/DMTF/Redfish-Mockup-Server
cd Redfish-Mockup-Server
pip install -r requirements.txt
python redfishMockupServer.py  -H 127.0.0.1 -p 9099 -S
```


## Run the script  against mockup server
```bash
git clone https://github.com/Krishnom/redfish-utilities
cd redfish-utilities && pip install -r requirements.txt

python main.py --url 'http://127.0.0.1:9099' 
```


## Get All/CPU/Memory/Storage/NIC/Boot/Bios settings 
To get individual settings, run below command
