# vrops_opsgenie_proxy
vRealize Operations OpsGenie Outbound Proxy


**Pre Requisition**

	- OS : Ubuntu20
	- Runtime : Python 3
	- PyPi Package : pygics

**Installation**

	$ apt install -y python3 python3-pip
	$ pip3 install pygics

**Configuration**

	Set "TOKEN" & "PROXY_LISTEN_PORT" vars in server.py

**Execution**

	$ python3 server.py