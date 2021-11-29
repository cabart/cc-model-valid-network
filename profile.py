"""
This profile describes n sender nodes connected through one switch to a single receiver node

Instructions:
Will follow soon.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal context.
pc = portal.Context()

# Add parameters
pc.defineParameter("usePhysical","Use physical nodes instead of VMs",portal.ParameterType.BOOLEAN,False)
pc.defineParameter("sender","Number of sender nodes", portal.ParameterType.INTEGER, 2)

# Retrieve user input from instantiation
params = pc.bindParameters()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
if params.sender < 1 or params.sender > 10:
    pc.reportError(portal.ParameterError("Number of senders should be between 1 and 10"))

# Add switch
switch = request.Switch("switch1")
sw_rcv_iface = switch.addInterface()

# Add receiver VM
rcvName = "rcv"
if params.usePhysical:
    nodeRcv = request.RawPC(rcvName)
else:
    nodeRcv = request.XenVM(rcvName)

rcv_iface = nodeRcv.addInterface()
#rcv_iface.addAddress(pg.IPv4Address("192.168.1.0","255,255,255,0"))

# Create link between switch and receiver node
link = request.L1Link("rcvlink")
link.addInterface(rcv_iface)
link.addInterface(sw_rcv_iface)

# Add sender VMs
for i in range(params.sender):
    # create node + interface + address
    nodeName = "sender" + str(i)
    if params.usePhysical:
        node = request.RawPC(nodeName)
    else:
        node = request.XenVM(nodeName)
    iface = node.addInterface()
    #iface.addAddress(pg.IPv4Address("192.168.1." + str(i),"255.255.255.0"))
    # Add startup script
    node.addService(pg.Execute(shell="sh", command="/local/repository/startup.sh"))
    # Add interface to switch
    sw_send_iface = switch.addInterface()
    # Add link to switch
    link = request.L1Link("link" + str(i))
    link.addInterface(iface)
    link.addInterface(sw_send_iface)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
