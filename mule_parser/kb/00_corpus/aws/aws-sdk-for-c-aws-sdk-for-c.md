# AWS SDK for C++: AWS SDK for C++

**Source:** [https://docs.aws.amazon.com/sdk-for-cpp/latest/api/root/html/index.html](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/root/html/index.html)

---

| ## AWS SDK for C++## AWS SDK for C++ Version 1.11.827 | 

[The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface for Amazon Web Services (AWS). It is meant to be performant and fully functioning with low- and high-level SDKs, while minimizing dependencies and providing platform portability (Windows, OSX, Linux, and mobile).]

AWS SDK for C++ is now in General Availability and recommended for production use. We invite our customers to join the development efforts by submitting pull requests and sending us feedback and ideas via GitHub Issues.

Clone this repository with submodules

`<BUILD_DIR>` with your build directory name:Build the project:

**_NOTE:_** BUILD_ONLY is an optional flag used to list only the services you are using. Building the whole SDK can take a long time. Also, check out the list of [CMake parameters](md_docs_2_c_make___parameters.html)

To compile in Linux, you must have the header files for libcurl, libopenssl. The packages are typically available in your package manager.

Debian based Linux distributions example: `sudo apt-get install libcurl-dev`

RPM based Linux distributions example: `sudo [yum|dnf|zypper] install libcurl-devel`

Zlib is **optional** and only required if you enable **request compression** for specific AWS services that support gzip/deflate encoding.

`-DENABLE_ZLIB_REQUEST_COMPRESSION=ON` — enables gzip/deflate request compression (disabled by default).If you do not enable this option, **zlib is not required** at build time. If you do enable it, install zlib as follows:

`sudo apt-get install zlib1g-dev``sudo yum install zlib-devel` or `sudo dnf install zlib-devel`**Reference:**

Building for macOS is largely the same as building on a *nix system except for how the system consumes the curl dependency and compilers.

You must install the [xcode command line tools](https://mac.install.guide/commandlinetools/4.html). This is required for Apple clang and gcc. This also installs libcurl as well.

:warning: If you are using macOS Sonoma, there is a

[known issue](https://github.com/aws/aws-sdk-cpp/issues/2804)where using libcurl version 8.4.0 on macOS can lead to issues.[This issue is being tracked with curl and Apple](https://github.com/curl/curl/issues/12525). In the meanwhile, please use an updated version of[curl from Homebrew](https://formulae.brew.sh/formula/curl). You can include this in your project via the CMAKE_PREFIX_PATH.cmake -DCMAKE_PREFIX_PATH="/opt/homebrew/opt/curl/" \-DAUTORUN_UNIT_TESTS=OFF \-DBUILD_ONLY="s3" \-DCMAKE_INSTALL_PREFIX="~/sdk-install" \..

To build for Android, add `-DTARGET_ARCH=ANDROID` to your CMake command line. Currently, we support Android APIs from 19 to 28 with Android NDK 19c, and we are using the built-in CMake toolchain file supplied by Android NDK, assuming you have the appropriate environment variables (ANDROID_NDK) set.

Building for Android on Windows requires some additional setup. In particular, you will need to run CMake from a Visual Studio developer command prompt (2015 or higher). Additionally, you will need 'git' and 'patch' in your path. If you have Git installed on a Windows system, then the patch is likely found in a sibling directory (.../Git/usr/bin/). Once you've verified these requirements, your CMake command line will change slightly to use nmake:

Nmake builds targets in a serial fashion. To make things quicker, we recommend installing JOM as an alternative to nmake and then changing the CMake invocation to:

You can download and install aws-sdk-cpp using the [vcpkg](https://github.com/Microsoft/vcpkg) dependency manager: 

git clone https://github.com/Microsoft/vcpkg.git cd vcpkg ./bootstrap-vcpkg.sh ./vcpkg integrate install ./vcpkg install aws-sdk-cpp

 The aws-sdk-cpp port in vcpkg is kept up to date by Microsoft team members and community contributors. If the version is out of date, please [create an issue or pull request](https://github.com/Microsoft/vcpkg) on the vcpkg repository.

You can download and install aws-sdk-cpp using [Conan](https://conan.io/). Use the following command: 

conan install --requires="aws-sdk-cpp/[*]" --build="aws-*"

 The aws-sdk-cpp Conan recipe is kept up to date by JFrog's Conan team members and community contributors. If the version is out of date, please [create an issue or pull request](https://github.com/conan-io/conan-center-index) on the ConanCenterIndex repository.

For information about maintenance and support for SDK major versions and our underlying dependencies, see the following in the AWS SDKs and Tools Shared Configuration and Credentials Reference Guide

The best way to interact with our team is through GitHub. You can open a [discussion](https://github.com/aws/aws-sdk-cpp/discussions/new/choose) for guidance questions or an [issue](https://github.com/aws/aws-sdk-cpp/issues/new/choose) for bug reports or feature requests.

You may also find help on community resources such as [StackOverFlow](https://stackoverflow.com/) with the tag [#aws-sdk-cpp](https://stackoverflow.com/questions/tagged/aws-sdk-cpp). If you have a support plan with [AWS Support](https://aws.amazon.com/premiumsupport/), you can also create a new support case.

Please make sure to check out our resources too before opening an issue: