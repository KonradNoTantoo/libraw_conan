from conans import ConanFile, CMake, AutoToolsBuildEnvironment, tools
import os


class LibrawConan(ConanFile):
    name = "libraw"
    version = "0.19.5"
    folder_name = "LibRaw-{}".format(version)
    license = "LGPL2"
    author = "konrad"
    url = "https://github.com/KonradNoTantoo/libraw_conan"
    description = "LibRaw is a library for reading RAW files obtained from digital photo cameras (CRW/CR2, NEF, RAF, DNG, and others)."
    topics = ("RAW", "image", "camera", "conan")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt"

    def copy_file_to_source(self, name):
        file_content = tools.load(name)
        path_to_source = os.path.join(self.source_folder, self.folder_name, name)
        tools.save(path_to_source, file_content)

    def source(self):
        tarball_path = "https://www.libraw.org/data/LibRaw-{}.tar.gz".format(self.version)
        tools.get(tarball_path)

        if self.settings.compiler == "Visual Studio":
            self.copy_file_to_source("CMakeLists.txt")

    def build(self):
        if self.settings.compiler == "Visual Studio":
            cmake = CMake(self)
            cmake.configure(source_folder=self.folder_name)
            cmake.build()
        else:
            with tools.chdir(self.folder_name):
                env_build = AutoToolsBuildEnvironment(self)
                env_build.configure() 
                env_build.make()

    def package(self):
        self.copy("libraw/*.h", dst="include", src=self.folder_name, keep_path=False)
        self.copy("*/libraw.dll", dst="bin", keep_path=False)
        self.copy("*/libraw.so", dst="lib", keep_path=False)
        self.copy("lib/*.pdb", dst="lib", keep_path=False)
        self.copy("lib/*.exp", dst="lib", keep_path=False)
        self.copy("lib/*.lib", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["libraw"]
        else:
            self.cpp_info.libs = ["libraw.so"]

