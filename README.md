# Turret

[![PyPi package](https://img.shields.io/pypi/v/turret.svg)][pypi]
[![Travis status](https://img.shields.io/travis/VanJanssen/turret.svg)][travis]
[![Documentation](https://img.shields.io/readthedocs/turret.svg)][documentation]
[![Dependencies](https://pyup.io/repos/github/VanJanssen/turret/shield.svg)][pyup]
[![Test coverage]( https://img.shields.io/codecov/c/github/vanjanssen/turret.svg)][codecov]

[pypi]: https://pypi.python.org/pypi/turret/
[travis]: https://travis-ci.org/VanJanssen/turret/
[documentation]: https://turret.readthedocs.io/en/latest/
[pyup]: https://pyup.io/repos/github/VanJanssen/turret/
[codecov]: https://codecov.io/gh/VanJanssen/turret

Turret is Python library and application that can help managing and securing
computer networks. The application provides users with a CLI and web interface
to discover, visualize and analyze the devices found on the network, and allows
linking multiple nodes running turret to increase coverage. The library allows
other developers to use Turret's core functionality in their own applications,
or provide extensions to Turret's functionality.

Turret is still under development, and most features are not yet implemented.
Planned features include:

- Lightweight, able to run smooth on low end hardware such as a Raspberry Pi.
- Uniform wrappers around common network tools such as Nmap with multiple
  output conversions and configuration presets.
- Both a Command Line Interface and a web application. Both should cover all
  features of Turret.
- The ability to create a graphical, interactive map of the network layout.
- Manage nodes known to Turret by specifying their requirements and desired
  state.
- Provide defensive capabilities for nodes managed by Turret, both passive
  (detection) and active (prevention).
- Provide offensive capabilities to aid penetration testing of the managed
  infrastructure, but also to deter attackers or reclaim compromised nodes.
