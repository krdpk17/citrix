try:
    	import pexpect
except:
    	ImportError, "Pexpect module is missing, please install the module"

import sys

try:
     	child = pexpect.spawn('telnet localhost bgpd')
except pexpect.ExceptionPexpect:
    	raise exceptions.NetworkException("Unable to spawn telnet process")
else:
	child.expect('.*Password:')
    	child.sendline('zebra')
	child.expect('.+>')
	child.sendline('en')
	child.expect('.+#')
	child.sendline('configure terminal')
	child.expect('.+\(config\)#')
	child.sendline('router bgp 100')
	child.expect('.+\(config-router\)#')
	s = str(sys.argv[1])
	sl = s.split(",")
	
	for i in range(1, len(sl)):
		cmd = 'no network ' + sl[i] + ' mask 255.255.255.255'
		child.sendline(cmd)
		child.expect('.+')

	child.sendline('exit')
	child.expect('.+\(config\)#')
	child.sendline('exit')
	child.expect('.+#')
	child.sendline('write')
	child.expect('Configuration saved to /etc/quagga/bgpd.conf')
	child.sendline('exit')
	
        
finally:
	child.close()
