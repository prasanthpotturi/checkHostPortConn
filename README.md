# check Host Port Connectivity 
This utility API proxy is useful in checking whether there is connectivity from MPs to backend/target host and port. This would be a self service proxy to application teams to verify whether a target endpoint is accessable instead of reaching out to support/internal operations teams.

## Steps to run install
1. Download and install Maven 3.0.*
2. Clone this repo https://github.com/prasanthpotturi/checkHostPortConn
3. cd checkHostPortConn/checkHostPortConn
4. Execute mvn install -Ptest -Dusername={apigee-edge-email} -Dpassword={apigee-edge-password} -Dorg={apigee-edge-org}

## Steps to test/run

### Header:

Authorization: Basic <orgAdmin/readonlyOrgAdmin>

Content-Type:application/json

### Body:

    {
        "hostip" :"xx.xxx.xxx.001",
         "port" : "443"
    }


## Sample Response:

//Sample response : when success

    {
        "host": "35.227.194.212",
        "ip": "443",
        "result": "Port is open"
    }

//Sample response : when failed

    {
        "host": "xx.xxx.xxx.001",
        "port": "4433",
        "result": "AccessControlException HOST not reachable"
    }