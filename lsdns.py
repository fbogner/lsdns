#!/usr/bin/python

import sys

sys.stderr.write("###########################################################\n")
sys.stderr.write("       lsdns by Florian Bogner @ Kapsch BusinessCom\n")
sys.stderr.write("            florian.bogner[at]kapsch[dot]net\n\n")
sys.stderr.write("lsdns queries a DNS server for all host names within a \ngiven IP range. The result is printed as a list of comma\nseparated values for further processing.\n")
sys.stderr.write("###########################################################\n\n")

try:
	import dns.resolver
	import dns.reversename
except:
	# disable stack trace
	sys.tracebacklimit = 0
	
	sys.stderr.write("Failed to import the module dns. This module has to be installed manually for python2. Please see the dependencies folder.\n")
	
	# exit manually as we caught the exception
	exit(1)
	
	
try:
	import ipaddress
except:
	# disable stack trace
	sys.tracebacklimit = 0
	
	sys.stderr.write("Failed to import the module ipaddress. This module has to be installed manually for python2. Please see the dependencies folder.\n")
	
	# exit manually as we caught the exception
	exit(1)
	

# check the arguments
if len(sys.argv) != 3:
	sys.stderr.write("Wrong number of arguments!\n")
	sys.stderr.write("Usage: "+sys.argv[0]+" <dns server to query> <IP address or range>\n")
	exit(1)

dns_server=sys.argv[1]	
my_hosts=None

# parse given IP address or range
try: 
		# try to convert the given string to a network
		my_hosts=list(ipaddress.ip_network(sys.argv[2].decode("utf-8")).hosts())
		
		# if the resulting network contains no hosts this indicates that a single ip adress was given => let's try to parse that
		if len(my_hosts) == 0:
			my_hosts.append(ipaddress.ip_address(sys.argv[2].decode("utf-8")))
		
except:
	sys.stderr.write("The given IP address or range could not be parsed.\n")
	sys.stderr.write("Please provide them in the following form: 10.1.0.0/23 for networks or 192.168.1.1 for hosts\n")
	exit(1)

# create the resolver object		
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = [dns_server]

# do the real work by querying the DNS server
for my_host in my_hosts:

	if not sys.stdout.isatty():
		sys.stderr.write(".")

	try: 
		addr = dns.reversename.from_address(str(my_host))
		answers = my_resolver.query(addr,'PTR')

		if len(answers) != 0:
	
			sys.stdout.write(str(my_host))
			for rdata in answers:
				sys.stdout.write(","+str(rdata)[:-1])
			
			sys.stdout.write("\n")
	except:
		#ignore a failed query
		pass
