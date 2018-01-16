# -*- coding: utf-8 -*-

"""
Turret's Scout module for active reconaicance.

In order to gain insight into its environment and/or its targets, turret can
perform active reconaicance.

In this case environment includes, but is not limited to:
- The system Turret is running on (processes, hardware, users, etc.)
- The network the system is located in (other nodes in the network, IP
  addresses, DNS servers, DHCP configuration).
- Nodes to which Turret has been pointed (IP addresses and domain names).

Active means Turret will send out packets to probe for the presence of other
systems and to detect the OS, services, configuration, etc. of this other
system. This mode will allow Turret to gain information faster and more
accurate, but will also be detectable. In some settings this might not be a
problem, other settings might place constrains of the network load and other
settings might want to reduce detectability to a minimum. Scout has multiple
preset configurations to deal with all these scenarios.

By itself, Scout will not run as a background process, but will only perform
the desired reconaicance. As such, Scout can be easility integrated in other
toolchains, export its data to a variaty of output formats. These include,
but are not limited to, JSON, XML, SQL databases and Elasticsearch.
"""

from turret.scout.core import recon  # noqa: F401
