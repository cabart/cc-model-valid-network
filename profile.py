"""
This is a simple profile.

Instructions:
Will follow soon.
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add two VMs
node1 = request.XenVM("node1")
node2 = request.XenVM("node2")

# Add link between nodes
link1 = request.Link(members = [node1, node2])

# Install and execute a script that is contained in the repository.
node1.addService(pg.Execute(shell="sh", command="/local/repository/startup.sh"))
node2.addService(pg.Execute(shell="sh", command="/local/repository/startup.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
