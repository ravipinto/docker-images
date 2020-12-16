#!/usr/bin/python
# Copyright (c)  2020, Oracle and/or its affiliates. All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#
# ==============================================
import sys

domain_name = os.environ.get("DOMAIN_NAME", "wc_domain")
domain_root = os.environ.get("DOMAIN_ROOT", "/u01/oracle/user_projects/domains")
admin_name  = os.environ['ADMIN_USERNAME']
admin_pass  = os.environ['ADMIN_PASSWORD']
admin_port  = os.environ['ADMIN_PORT']
hostname    = sys.argv[1]
vol_name    = sys.argv[2]
url         = hostname + ':' + admin_port

print('')
print('Configuring Node Manager');
print('=========================');
print('')
print('')

# Setting domain path
# ===================
domain_path  = domain_root + '/' + domain_name
nodemanager_path = '/' + vol_name + '/oracle/wlserver/common/nodemanager'

# Read domain for updates
# =======================
readDomain(domain_path)

# Set listen address
# ==================
cd('/')
cd('/Machines/machine1/NodeManager/machine1')
cmo.setListenAddress(hostname)
cmo.setListenPort(5556)
cmo.setDebugEnabled(false)

# Updating domain
# ==============================
updateDomain()
closeDomain()

#Set up Node Manager
#==========================
connect(admin_name, admin_pass, url)
nmEnroll(domain_path, nodemanager_path)
disconnect()
exit()
