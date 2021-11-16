"""An example of constructing a profile with two VMs connected by a LAN. (copy of two-vm-lan for testing purposes)

Instructions:
Wait for the profile instance to start, and then log in to either VM via the
ssh ports specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two XenVM nodes.
node1 = request.XenVM("node1")
node2 = request.XenVM("node2")

# Create a link between them
link1 = request.Link(members = [node1,node2])

portal.context.printRequestRSpec()
