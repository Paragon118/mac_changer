import subprocess
import optparse
import re

 
def pars():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="-i ,--interface -Your interface" )
    parse.add_option("-m","--macaddress",dest="mac_address",help=" -m ,--macaddress -Your new mac adsress")
    return parse.parse_args()


def subp(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])
def control_new_mac(interface):
    ifconfig= subprocess.check_output(["ifconfig",interface])
    newmac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if newmac:
        return newmac.group(0)
print("Mac Changer started")
(user_input,arguments)= pars()
subp(user_input.interface,user_input.mac_address)
finally_mac = control_new_mac(user_input.interface)
if finally_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")

 
