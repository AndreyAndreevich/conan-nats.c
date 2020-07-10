#!/usr/bin/env python
# -*- coding: utf-8 -*
import shutil
import os
from conans import ConanFile, tools, CMake

class civetwebConan(ConanFile):
    name = "nats.c"
    version = '2.1.0'
    license = "MIT"
    url = "https://github.com/AndreyAndreevich/conan-nats.c"
    homepage = "https://github.com/nats-io/nats.c"
    description = "NATS Streaming - C Client"
    author = "l.a.r.p@yandex.ru"
    topics = ("conan", "nats.c", "nats")
    exports = ("LICENSE.md", "README.md")
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared"                    : [True, False],
        "no_spin"                   : [True, False],
        "with_tls"                  : [True, False],
        "tls_force_host_verify"     : [True, False],
        "tls_use_openssl_1_1_api"   : [True, False],
        "streaming"                 : [True, False]
    }
    default_options = {
        "shared"                    : False,
        "no_spin"                   : True,
        "with_tls"                  : False,
        "tls_force_host_verify"     : False,
        "tls_use_openssl_1_1_api"   : False,
        "streaming"                 : False
    }

    _source_subfolder   = "source_subfolder"
    _build_subfolder    = "build_subfolder"

    exports_sources = (_source_subfolder, "CMakeLists.txt")

    def source(self):
        tools.get('%s/archive/v%s.zip' % (self.homepage, self.version))
        os.rename('nats.c-%s' % self.version, self._source_subfolder)
        os.rename(os.path.join(self._source_subfolder, 'CMakeLists.txt'
                               ), os.path.join(self._source_subfolder,
                                               'CMakeListsOriginal.txt'))
        shutil.move('CMakeLists.txt',
                    os.path.join(self._source_subfolder,
                                 'CMakeLists.txt'))

    def config_options(self):
        pass

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["NATS_BUILD_NO_SPIN"] = self.options.no_spin
        cmake.definitions["NATS_BUILD_WITH_TLS"] = self.options.with_tls
        cmake.definitions["NATS_BUILD_TLS_FORCE_HOST_VERIFY"] = self.options.tls_force_host_verify
        cmake.definitions["NATS_BUILD_TLS_USE_OPENSSL_1_1_API"] = self.options.tls_use_openssl_1_1_api
        cmake.definitions["NATS_BUILD_STREAMING"] = self.options.streaming
        cmake.definitions["NATS_BUILD_LIB_SHARED"] = self.options.shared
        cmake.definitions["NATS_BUILD_LIB_STATIC"] = not self.options.shared
        cmake.definitions["NATS_BUILD_STATIC_EXAMPLES"] = True
        cmake.configure(build_folder=self._build_subfolder, source_folder=self._source_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib", dst="bin", src="lib")
        self.copy("*.so", dst="bin", src="lib")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

        if self.settings.os == 'Linux':
            self.cpp_info.libs.extend(["dl", "rt", "pthread"])
