#!/usr/bin/python
# Copyright (c)  2020, Oracle and/or its affiliates. All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
import sys

#============================================================
#Connect To AdminServer and create Content Server Connection
#============================================================

adminHost     = os.environ.get("ADMIN_SERVER_CONTAINER_NAME")
adminPort     = os.environ.get("ADMIN_PORT")
adminName     = os.environ.get("ADMIN_USERNAME")
adminPassword = os.environ.get("ADMIN_PASSWORD")

configureConnection = os.environ.get("CONFIGURE_UCM_CONNECTION")
ucmConnectionName = 'wcp_ucm'
ucmHost = os.environ.get("UCM_HOST")
ucmPort = os.environ.get("UCM_PORT")
ucmPortalIdentifier = 'webcenter'
ucmSecurityGroup = 'UCM_Portal'
ucmAdminUserName = os.environ.get("UCM_ADMIN_USER")
ucmsocketType    = os.environ.get("UCM_SOCKET_TYPE")
ucmUrl           = os.environ.get("UCM_URL")


print('')
print('Configuring Content Server Connection');
print('=====================================');
print('Parameters :');
print('Configure Connection :' + configureConnection);
print('Connection Name :' + ucmConnectionName);
print('Server Host Name :' + ucmHost);
print('Port :' + ucmPort);
print('Portal Identifier :' + ucmPortalIdentifier);
print('Security Group :' + ucmSecurityGroup);
print('Admin User Name :' + ucmAdminUserName);
print('Socket Type :' + ucmsocketType);
print('UCM Url :' + ucmUrl);
print('')
print('')

url = adminHost + ":" + adminPort
connect(adminName, adminPassword, url)

deleteContentServerConnection(appName='webcenter', name=ucmConnectionName)
if ucmsocketType == 'socket':
    createContentServerConnection (appName='webcenter', name=ucmConnectionName, socketType=ucmsocketType, serverHost=ucmHost, serverPort=ucmPort, isPrimary='true')
if ucmsocketType == 'jaxws':
    createContentServerConnection (appName='webcenter', name=ucmConnectionName, socketType=ucmsocketType, url=ucmUrl,adminUsername=ucmAdminUserName,isPrimary='true')

setContentServerProperties(appName='webcenter', portalServerIdentifier=ucmPortalIdentifier, securityGroup=ucmSecurityGroup, adminUserName=ucmAdminUserName)
listContentServerConnections(appName='webcenter',verbose=1)
listContentServerProperties(appName='webcenter')
    
disconnect()
exit()

