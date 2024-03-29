%global mfx_abi 1
%global mfx_version %{mfx_abi}.35
%global __provides_exclude_from ^%{_libdir}/mfx/libmfx_.*\\.so$

Name:       intel-mediasdk
Epoch:      1
Version:    23.2.2
Release:    1%{?dist}
Summary:    Hardware-accelerated video processing on Intel integrated GPUs library
URL:        http://mediasdk.intel.com
License:    MIT
ExclusiveArch:  x86_64

Source0:    https://github.com/Intel-Media-SDK/MediaSDK/archive/%{name}-%{version}.tar.gz
Patch0:     https://patch-diff.githubusercontent.com/raw/Intel-Media-SDK/MediaSDK/pull/2998.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  libdrm-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libva-devel
BuildRequires:  libX11-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  wayland-devel

Obsoletes:  libmfx < %{mfx_version}
Provides:   libmfx = %{mfx_version}
Provides:   libmfx%{_isa} = %{mfx_version}

%description
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition.

%package    devel
Summary:    SDK for hardware-accelerated video processing on Intel integrated GPUs
Provides:   libmfx-devel = %{mfx_version}
Provides:   libmfx%{_isa}-devel = %{mfx_version}
Requires:   %{name}%{_isa} = %{epoch}:%{version}-%{release}

%description devel
Intel Media SDK provides a plain C API to access hardware-accelerated video
decode, encode and filtering on Intel Gen graphics hardware platforms.
Implementation written in C++ 11 with parts in C-for-Media (CM).

Supported video encoders: HEVC, AVC, MPEG-2, JPEG, VP9 Supported video decoders:
HEVC, AVC, VP8, VP9, MPEG-2, VC1, JPEG Supported video pre-processing filters:
Color Conversion, Deinterlace, Denoise, Resize, Rotate, Composition.

%package tracer
Summary:    Dump the calls of an application to the Intel Media SDK library
Requires:   %{name}%{_isa} = %{version}-%{release}

%description tracer
Media SDK Tracer is a tool which permits to dump logging information from the
calls of the application to the Media SDK library. Trace log obtained from this
tool is a recommended information to provide to Media SDK team on submitting
questions and issues.

%prep
%autosetup -p1 -n MediaSDK-%{name}-%{version}

%build
%cmake \
    -DBUILD_DISPATCHER=ON \
    -DBUILD_SAMPLES=OFF \
    -DBUILD_TESTS=ON \
    -DBUILD_TOOLS=OFF \
    -DENABLE_OPENCL=ON \
    -DENABLE_WAYLAND=ON \
    -DENABLE_X11=ON \
    -DENABLE_X11_DRI3=ON \
    -DMFX_ENABLE_KERNELS=ON \
    -DUSE_SYSTEM_GTEST=ON

%cmake_build

%install
%cmake_install

%check
%cmake_build -- test

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.rst
%{_libdir}/libmfx.so.%{mfx_abi}
%{_libdir}/libmfx.so.%{mfx_version}
%{_libdir}/libmfx-tracer.so.%{mfx_abi}
%{_libdir}/libmfx-tracer.so.%{mfx_version}
%{_libdir}/libmfxhw64.so.%{mfx_abi}
%{_libdir}/libmfxhw64.so.%{mfx_version}
%{_libdir}/mfx/libmfx_*_hw64.so
%{_datadir}/mfx/plugins.cfg

%files devel
%{_includedir}/mfx
%{_libdir}/libmfx.so
%{_libdir}/libmfx-tracer.so
%{_libdir}/libmfxhw64.so
%{_libdir}/pkgconfig/libmfx.pc
%{_libdir}/pkgconfig/libmfxhw64.pc
%{_libdir}/pkgconfig/mfx.pc

%files tracer
%{_bindir}/mfx-tracer-config
%{_libdir}/libmfx-tracer.so
%{_libdir}/libmfx-tracer.so.%{mfx_abi}
%{_libdir}/libmfx-tracer.so.%{mfx_version}

%changelog
* Tue May 23 2023 Simone Caronni <negativo17@gmail.com> - 1:23.2.2-1
- Update to 23.2.2.

* Wed Apr 19 2023 Simone Caronni <negativo17@gmail.com> - 1:23.2.0-1
- Update to 23.2.0.

* Thu Apr 13 2023 Simone Caronni <negativo17@gmail.com> - 1:23.1.6-1
- Update to 23.1.6.

* Sat Mar 11 2023 Simone Caronni <negativo17@gmail.com> - 1:23.1.3-1
- Update to 23.1.3.

* Fri Feb 24 2023 Simone Caronni <negativo17@gmail.com> - 1:23.1.2-1
- Update to 23.1.2.

* Fri Feb 10 2023 Simone Caronni <negativo17@gmail.com> - 1:23.1.1-1
- Update to 23.1.1.

* Mon Jan 30 2023 Simone Caronni <negativo17@gmail.com> - 1:23.1.0-1
- Update to 23.1.0.

* Sun Dec 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.6.4-1
- Update to 22.6.4.

* Fri Nov 18 2022 Simone Caronni <negativo17@gmail.com> - 1:22.6.3-1
- Update to 22.6.3.

* Mon Oct 24 2022 Simone Caronni <negativo17@gmail.com> - 1:22.6.0-1
- Update to 22.6.0.

* Tue Oct 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.5.4-1
- Update to 22.5.4.

* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 1:22.5.3-1
- Update to 22.5.3.

* Wed Aug 17 2022 Simone Caronni <negativo17@gmail.com> - 1:22.5.2-1
- Update to 22.5.2.

* Tue Aug 09 2022 Simone Caronni <negativo17@gmail.com> - 1:22.5.1-1
- Update to 22.5.1.

* Thu Jul 21 2022 Simone Caronni <negativo17@gmail.com> - 1:22.5.0-1
- Update to 22.5.0.

* Mon Jul 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.4.4-1
- Update to 22.4.4.

* Thu Jun 09 2022 Simone Caronni <negativo17@gmail.com> - 1:22.4.3-1
- Update to 22.4.3.

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 1:22.4.2-1
- Update to 22.4.2.

* Sun Apr 24 2022 Simone Caronni <negativo17@gmail.com> - 1:22.4.0-1
- Update to 22.4.0.

* Mon Apr 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.3.0-2
- Split configuration for the various branches.

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 1:22.3.0-1
- Update to 22.3.0.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 1:22.2.2-1
- Update to 22.2.2.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 1:22.2.1-1
- Update to 22.2.1.

* Thu Feb 03 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.0-1
- Update to 22.1.0.

* Mon Dec 27 2021 Simone Caronni <negativo17@gmail.com> - 1:21.4.3-1
- Update to 21.4.3.

* Mon Oct 25 2021 Simone Caronni <negativo17@gmail.com> - 1:21.3.5-1
- Update to 21.3.5.

* Sat Sep 04 2021 Simone Caronni <negativo17@gmail.com> - 1:21.3.3-1
- Update to 21.3.3.

* Sun Aug 15 2021 Simone Caronni <negativo17@gmail.com> - 1:21.3.1-1
- Update to 21.3.1.

* Wed Jun 23 2021 Simone Caronni <negativo17@gmail.com> - 1:21.2.2-1
- Update to 21.2.2.

* Mon Apr 05 2021 Simone Caronni <negativo17@gmail.com> - 1:21.1.3-1
- Update to 21.1.3.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 1:21.1.1-1
- Update to 21.1.1.

* Thu Oct 29 2020 Simone Caronni <negativo17@gmail.com> - 1:20.3.1-1
- Update to 20.3.1.

* Fri May 15 2020 Simone Caronni <negativo17@gmail.com> - 20.1.1-1
- Update to 20.1.1.
- Allow building on CentOS/RHEL 7.

* Fri Apr 10 2020 Dominik Mierzejewski <rpm@greysector.net> 20.1.0-1
- update to 20.1.0 (#1786892)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-2
- Add missing Obsoletes: and Requires:
- Add license text and docs

* Fri Oct 11 2019 Dominik Mierzejewski <rpm@greysector.net> 19.3.0-1
- initial build
