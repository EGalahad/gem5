"""Implements a k-ary n-cube (torus) topology.

The number of routers is equal to the number of controllers.
N = k**n
"""
from m5.objects import *

from common import FileSystemConfig

from topologies.BaseTopology import SimpleTopology


class Torus(SimpleTopology):
    description = "Torus"
    
    def __init__(self, controllers):
        self.nodes = controllers
        
    # Makes a generic torus
    # assuming an equal number of cache and directory cntrls
    
    def makeTopology(self, options, network, IntLink, ExtLink, Router):
        nodes = self.nodes
        
        num_routers = options.num_cpus
        k = options.kary
        n = options.ndim
        assert k > 0
        assert n > 0
        assert num_routers == k**n
        
        # default values for link latency and router latency.
        # Can be over-ridden on a per link/router basis
        link_latency = options.link_latency
        router_latency = options.router_latency
        
        # There must be an evenly divisible number of cntrls to routers
        cntrls_per_router, remainder = divmod(len(nodes), num_routers)
        assert remainder == 0
        
        # Create the routers in the torus
        routers = [
            Router(router_id=i, latency=router_latency)
            for i in range(num_routers)
        ]
        network.routers = routers
        
        # link counter to set unique link ids
        link_count = 0
        
        # Create the ext links
        ext_links = []
        for (i, node) in enumerate(nodes):
            cntrl_level, router_id = divmod(i, num_routers)
            assert cntrl_level < cntrls_per_router
            ext_links.append(
                ExtLink(
                    link_id=link_count,
                    ext_node=node,
                    int_node=routers[router_id],
                    latency=link_latency,
                )
            )
            link_count += 1
        network.ext_links = ext_links
        
        # Create the torus int links
        int_links = []
        # we enumerate the routers for each dimension, 
        # for each router, we create 2*n links, one for each direction
        for i, router in enumerate(routers):
            router_id = i
            coord = []
            for j in range(n):
                coord.append(router_id % k)
                router_id = router_id // k
            for j in range(n):
                coord[j] = (coord[j] + 1) % k
                R_router_id = sum([coord[l] * k**l for l in range(n)])
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=routers[i],
                        dst_node=routers[R_router_id],
                        src_outport="R%d" % j,
                        dst_inport="L%d" % j,
                        latency=link_latency,
                        weight=1,
                        is_wrap=(coord[j] == k-1),
                    )
                )
                link_count += 1
                coord[j] = (coord[j] - 2) % k
                L_router_id = sum([coord[l] * k**l for l in range(n)])
                int_links.append(
                    IntLink(
                        link_id=link_count,
                        src_node=routers[i],
                        dst_node=routers[L_router_id],
                        src_outport="L%d" % j,
                        dst_inport="R%d" % j,
                        latency=link_latency,
                        weight=1,
                        is_wrap=(coord[j] == 0),
                    )
                )
                coord[j] = (coord[j] + 1) % k
                link_count += 1
        network.int_links = int_links
    
    def registerTopology(self, options):
        for i in range(options.num_cpus):
            FileSystemConfig.register_node([i], MemorySize(options.mem_size) // options.num_cpus, i)
        