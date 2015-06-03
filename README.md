# lsdns
lsdns queries a DNS server for all host names within a given IP range. The result is printed as a list of comma separated values for further processing.

# Usage
./lsdns.py <dns server to query> <IP address or range>

Example: ./lsdns.py 8.8.8.8 148.198.1.0/24

# Sample Output
148.198.1.84,ns1.kapsch.net
148.198.1.85,ns2.kapsch.net
148.198.1.87,vitatv.kapsch.net
148.198.1.89,partners.kapsch.net
148.198.1.92,www2.kapsch.net,xmas.kapsch.net,www.kapsch.net
148.198.1.93,www3.kapsch.net
148.198.1.94,tts-ad.ae,mobile.kapsch.net,www.tts-ad.ae
148.198.1.116,emorelte.kapsch.net
148.198.1.117,emu.kapsch.net
148.198.1.126,sitemanager.kapsch.net
148.198.1.132,s060b264.kapsch.net
148.198.1.150,ftp.kapsch.net
148.198.1.214,profilesftp.kapschcarrier.com
148.198.1.228,cumulus.kapsch.net.1.198.148.in-addr.arpa
148.198.1.230,servicetest.kapschbusiness.com
