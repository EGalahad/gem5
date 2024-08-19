from m5.params import *
from m5.objects import *

from common import FileSystemConfig

from topologies.BaseTopology import SimpleTopology

# Creates a generic Ring assuming an equal number of cache
# and directory controllers.


class Ring(SimpleTopology):
    description = "Ring"
    
    def __init__(self, controllers):
        self.nodes = controllers
        
    # Makes a generic ring
    # assuming an equal number of cache and directory cntrls
    
    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        nodes = self.nodes
        
        num_routers = options.num_cpus
        
        # default values for link latency and router latency.
        # Can be over-ridden on a per link/router basis
        link_latency = options.link_latency
        router_latency = options.router_latency
        
        # There must be an evenly divisible number of cntrls to routers
        cntrls_per_router, remainder = divmod(len(nodes), num_routers)
        assert remainder == 0
        
        # Create the routers in the ring
        routers = [
            Router(router_id=i, latency=router_latency)
            for i in range(num_routers)
        ]
        network.routers = routers
        
        # link counter to set unique link ids
        link_count = 0
        
        # Create the ring links
        ext_links = []
        for (i, n) in enumerate(nodes):
            cntrl_level, router_id = divmod(i, num_routers)
            assert cntrl_level < cntrls_per_router
            ext_links.append(
                ExtLink(
                    link_id=link_count,
                    ext_node=n,
                    int_node=routers[router_id],
                    latency=link_latency,
                )
            )
            link_count += 1
        network.ext_links = ext_links
        
        # Create the ring links
        int_links = []
        
        # Clockwise ring connections
        for i in range(num_routers):
            int_links.append(
                IntLink(
                    link_id=link_count,
                    src_node=routers[i],
                    dst_node=routers[(i + 1) % num_routers],
                    src_outport="CW",
                    dst_inport="CCW",
                    latency=link_latency,
                    weight=1,
                )
            )
            link_count += 1
        
        for i in range(num_routers):
            int_links.append(
                IntLink(
                    link_id=link_count,
                    src_node=routers[i],
                    dst_node=routers[(i - 1) % num_routers],
                    src_outport="CCW",
                    dst_inport="CW",
                    latency=link_latency,
                    weight=1,
                )
            )
            link_count += 1
        network.int_links = int_links
    
    def registerTopology(self, options):
        for i in range(options.num_cpus):
            FileSystemConfig.register_node([i], MemorySize(options.mem_size) // options.num_cpus, i)
        