[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com//AndreyAndreevich/conan-nats.c/workflows/CI/badge.svg)](https://github.com//AndreyAndreevich/conan-nats.c/actions)
[![Download](https://api.bintray.com/packages/andrbek/conan/nats.c%3Aandrbek/images/download.svg)](https://bintray.com/andrbek/conan/nats.c%3Aandrbek/_latestVersion)

# conan-nats.c

## Basic setup

    $ conan install . nats.c/2.1.0@andrbek/testing
    
## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
      nats.c/2.1.0@andrbek/testing

    [options]
      nats.c:shared=True                              # default is False
      nats.c:no_spin=True                             # default is True
      nats.c:with_tls=True                            # default is False
      nats.c:tls_force_host_verify=True               # default is False
      nats.c:tls_use_openssl_1_1_api=True             # default is False
      nats.c:streaming=True                           # default is False

    [generators]
      cmake

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
