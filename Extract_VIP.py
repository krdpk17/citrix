from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.stat.lb.lbvserver_stats import lbvserver_stats
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.util.filtervalue import filtervalue
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_cachepolicy_binding import lbvserver_cachepolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_service_binding import lbvserver_service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwconfidfield import appfwconfidfield
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwlearningdata import appfwlearningdata
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwlearningdata_args import appfwlearningdata_args
from nssrc.com.citrix.netscaler.nitro.resource.config.appfw.appfwprofile import appfwprofile
from nssrc.com.citrix.netscaler.nitro.resource.config.audit.auditnslogaction import auditnslogaction
from nssrc.com.citrix.netscaler.nitro.resource.config.audit.auditsyslogparams import auditsyslogparams
from nssrc.com.citrix.netscaler.nitro.resource.config.authorization.authorizationpolicylabel_binding import authorizationpolicylabel_binding 
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service import service
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_binding import service_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.servicegroup_servicegroupmember_binding import servicegroup_servicegroupmember_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.basic.service_lbmonitor_binding import service_lbmonitor_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.cache.cacheobject import cacheobject
from nssrc.com.citrix.netscaler.nitro.resource.config.cmp.cmppolicy_lbvserver_binding import cmppolicy_lbvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsnsecrec import dnsnsecrec
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnssuffix import dnssuffix
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnsview_dnspolicy_binding import dnsview_dnspolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.dns.dnszone import dnszone
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbldnsentries import gslbldnsentries
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbparameter import gslbparameter
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice import gslbservice
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbservice_binding import gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbsite import gslbsite
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver import gslbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.gslb.gslbvserver_gslbservice_binding import gslbvserver_gslbservice_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ha.hanode import hanode
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_binding import lbvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.network.Interface import Interface
from nssrc.com.citrix.netscaler.nitro.resource.config.network.channel import channel
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsacl import nsacl
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip import nsip
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsip_args import nsip_args
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nslimitidentifier import nslimitidentifier
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nstcpbufparam import nstcpbufparam
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsversion import nsversion
from nssrc.com.citrix.netscaler.nitro.resource.config.ns.nsxmlnamespace import nsxmlnamespace
from nssrc.com.citrix.netscaler.nitro.resource.config.policy.policyexpression import policyexpression
from nssrc.com.citrix.netscaler.nitro.resource.config.policy.policyexpression_args import policyexpression_args
from nssrc.com.citrix.netscaler.nitro.resource.config.protocol.protocolhttpband import protocolhttpband
from nssrc.com.citrix.netscaler.nitro.resource.config.protocol.protocolhttpband_args import protocolhttpband_args
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpgroup import snmpgroup
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpmanager import snmpmanager
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpoid import snmpoid
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpoid_args import snmpoid_args
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmptrap import snmptrap
from nssrc.com.citrix.netscaler.nitro.resource.config.snmp.snmpuser import snmpuser
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcipher_binding import sslcipher_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslfipskey import sslfipskey
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpolicy_binding import sslpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslpolicy_csvserver_binding import sslpolicy_csvserver_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemgroup_binding import systemgroup_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.transform.transformprofile_transformaction_binding import transformprofile_transformaction_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnglobal_authenticationldappolicy_binding import vpnglobal_authenticationldappolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.vpn.vpnglobal_vpnclientlessaccesspolicy_binding import vpnglobal_vpnclientlessaccesspolicy_binding



import json
import sys
import requests
import ast

token = None
def cpxlogin(ip="172.17.0.2",username="nsroot",password="nsroot"):
	
	global token
	url="http://"+ip+"/nitro/v1/config/login"
	headers = {'Content-type': 'application/vnd.com.citrix.netscaler.login+json'}
	content = {"login":{"username":username,"password":password}}
	request = requests.post(url,data=json.dumps(content),headers=headers)
	cookie = request.headers.get('Set-Cookie')
	var = cookie.split(' ')
	var = var[7].split('=')
	token = var[1][:-1]
	token = 'NITRO_AUTH_TOKEN='+token
	return request.status_code



def cpxlogout(ip="172.17.0.2"):

	global token
	url="http://"+ip+"/nitro/v1/config/logout"
	headers = {'Content-type': 'application/json','Cookie':token}
	payload = {"logout":{}}
	request = requests.post(url,data=json.dumps(payload),headers=headers)
	token = None
	return request.status_code

def getVipStatus(ip="172.17.0.2"):

	global token
	url="http://"+ip+"/nitro/v1/stat/lbvserver"
	headers = {'Accept': 'application/vnd.com.citrix.netscaler.lbvserver+json','Cookie':token}
	payload = {}
	request = requests.get(url,data=json.dumps(payload),headers=headers)
	
	lbVServer = ast.literal_eval(request.text) #converting unicode to dict format
	vips=lbVServer["lbvserver"] 
	lbvservers = [] 

	for i in vips:
		server = [i["name"],i["primaryipaddress"],i["state"], i["totalpktssent"], i["pktsrecvdrate"],i["pktssentrate"], i["primaryport"], i["totalrequests"], i["invalidrequestresponsedropped"], i["vslbhealth"], i["sortorder"], i["type"], i["inactsvcs"]]
		lbvservers.append(server)

	ret = [request.status_code,lbvservers]

	return ret


login = cpxlogin(sys.argv[1],sys.argv[2],sys.argv[3])

if login == 200 or login == 201:
	
	vips = getVipStatus()
	if vips[0]==200 or vips[0]==201:
		print(json.dumps(vips[1]))
	else:	
		result = ["Error:","Couldn't get the VIPs"]
		print(json.dumps(result))
	logout = cpxlogout("172.17.0.2")

else:
	result = ["Error:","Couldn't login. Please provide valid information."]
	print(json.dumps(result))
