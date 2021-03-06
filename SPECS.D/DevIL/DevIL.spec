Name:           DevIL
Version:        1.7.8
Release:        15%{?dist}
Summary:        A cross-platform image library
Summary(zh_CN.UTF-8): 一个跨平台的图像库
Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:        LGPLv2
URL:            http://openil.sourceforge.net/
Source0:        http://downloads.sourceforge.net/openil/%{name}-%{version}.tar.gz
Patch0:         DevIL-1.7.5-allegropicfix.patch
Patch1:         DevIL-1.7.5-il_endian_h.patch
Patch2:         DevIL-1.7.8-CVE-2009-3994.patch
Patch3: 	DevIL-1.7.8-libpng15.patch
Patch4:         DevIL-1.7.8-gcc5.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  allegro-devel
BuildRequires:  lcms-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libXext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  jasper-devel
BuildRequires:  SDL-devel => 1.2.5

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is easy for a
developer to learn and use. Ultimate control of images is left to the
developer, so unnecessary conversions, etc. are not performed. DevIL utilizes
a simple, yet powerful, syntax. DevIL can load, save, convert, manipulate,
filter and display a wide variety of image formats.

%description -l zh_CN.UTF-8
一个跨平台的图像库。

%package devel
Summary:        Development files for DevIL
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:       %{name} = %{version}-%{release}, pkgconfig
Requires(post): info
Requires(preun): info

%description devel
Development files for DevIL

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package ILUT
Summary:        The libILUT component of DevIL
Summary(zh_CN.UTF-8): %{name} 的 libILUT 组件
Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
Requires:       %{name} = %{version}-%{release}

%description ILUT
The libILUT component of DevIL

%description ILUT -l zh_CN.UTF-8
%{name} 的 libILUT 组件。

%package ILUT-devel
Summary:        Development files for the libILUT component of DevIL
Summary(zh_CN.UTF-8): ILUT 的开发包
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:       %{name}-ILUT = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       pkgconfig allegro-devel libGLU-devel

%description ILUT-devel
Development files for the libILUT component of DevIL

%description ILUT-devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q -n devil-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
iconv -f iso8859-1 CREDITS -t utf8 > CREDITS.conv
touch -r CREDITS CREDITS.conv
mv CREDITS.conv CREDITS
chmod -x src-IL/src/il_*.c
sed -i 's|png12|png16|g' configure

%build
%ifarch x86_64
DISABLE_SSE="--disable-sse3"
%endif
%ifarch %{ix86}
DISABLE_SSE="--disable-sse --disable-sse2 --disable-sse3"
%endif
%configure --enable-ILU --enable-ILUT --disable-static --disable-allegrotest \
	   $DISABLE_SSE
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|LD_RUN_PATH|DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_infodir}/dir
magic_rpm_clean.sh

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/DevIL_manual.info %{_infodir}/dir 2> /dev/null || :
%preun devel
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/DevIL_manual.info %{_infodir}/dir 2> /dev/null || :
fi

%post ILUT -p /sbin/ldconfig
%postun ILUT -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_bindir}/ilur
%{_libdir}/libIL.so.*
%{_libdir}/libILU.so.*
%doc AUTHORS ChangeLog COPYING CREDITS README TODO


%files devel
%defattr(-,root,root,-)
%{_libdir}/libIL.so
%{_libdir}/libILU.so
%{_libdir}/pkgconfig/IL.pc
%{_libdir}/pkgconfig/ILU.pc
%dir %{_includedir}/IL
%{_includedir}/IL/devil_cpp_wrapper.hpp
%{_includedir}/IL/il.h
%{_includedir}/IL/ilu.h
%{_includedir}/IL/ilu_region.h
%{_infodir}/DevIL_manual.info.gz


%files ILUT
%defattr(-,root,root,-)
%{_libdir}/libILUT.so.*


%files ILUT-devel
%defattr(-,root,root,-)
%{_libdir}/libILUT.so
%{_libdir}/pkgconfig/ILUT.pc
%{_includedir}/IL/ilut.h


%changelog
* Sat Nov 07 2015 Liu Di <liudidi@gmail.com> - 1.7.8-15
- 为 Magic 3.0 重建

* Thu Oct 29 2015 Liu Di <liudidi@gmail.com> - 1.7.8-14
- 为 Magic 3.0 重建

* Sun Mar 01 2015 Liu Di <liudidi@gmail.com> - 1.7.8-13
- 为 Magic 3.0 重建

* Tue Apr 29 2014 Liu Di <liudidi@gmail.com> - 1.7.8-12
- 为 Magic 3.0 重建

* Tue Apr 29 2014 Liu Di <liudidi@gmail.com> - 1.7.8-11
- 为 Magic 3.0 重建

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec  4 2009 Hans de Goede <hdegoede@redhat.com> 1.7.8-4
- Fix DICOM Processing Buffer Overflow Vulnerability CVE-2009-3994 (#542700)

* Fri Aug 21 2009 Hans de Goede <hdegoede@redhat.com> 1.7.8-3
- Switch Source0 to respun upstream tarbal (added a missing header)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar  9 2009 Hans de Goede <hdegoede@redhat.com> 1.7.8-1
- Update to latest upstream: 1.7.8

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Hans de Goede <hdegoede@redhat.com> 1.7.7-1
- Update to latest upstream: 1.7.7

* Mon Jan 19 2009 Hans de Goede <hdegoede@redhat.com> 1.7.5-2
- Fix missing symbols (rh 480269)
- Fix off by one error in CVE-2008-5262 check (rh 479864)

* Tue Jan 13 2009 Hans de Goede <hdegoede@redhat.com> 1.7.5-1
- Update to latest upstream: 1.7.5
- Add patch to fix CVE-2008-5262

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6.8-0.15.rc2
- Autorebuild for GCC 4.3

* Sun Jan 13 2008 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.14.rc2
- Patch to fix headers for gcc 4.3, see BZ #428527. (Thanks to Hans de Goede)

* Wed Aug 22 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.13.rc2
- Release bump for F8 mass rebuild
- Added patch to fix BZ #253639

* Tue Aug 07 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.12.rc2
- Split libILUT into separate package. See BZ #250734
- Removed some old provides:
- Convert the CREDITS to UTF8
- Updated license field due to new guidelines

* Tue Jan 02 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.11.rc2
- Added patch to fix endian issues with some SGI files. Courtesy of Scott A.
  Friedman (BZ #220417)

* Thu Sep 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.10.rc2
- Upgrade to 1.6.8-rc2
- Added libICE-devel buildrequire
- Dropped DevIL-1.6.8-rc1-64bit.patch, fixed upstream
- Updated allegropicfix.patch for new version
- Updated and split header fixes into separate files for easier maintenance

* Mon Aug 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.9.rc1
- Release bump for FC6 mass rebuild

* Fri Jun 09 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.8.rc1
- Added patch courtesy of Hans de Goede to fix crashes on 64bit systems

* Wed May 31 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.7.rc1
- Added libGLU-devel to buildrequires
- Dropped libGL-devel from requires for devel package

* Sun May 28 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.6.rc1.iss
- Dropped xorg-x11-devel as a buildrequire
- Dropped zlib-devel as a buildrequire
- Dropped xorg-x11-devel as a require for the devel package
- Added libGL-devel and libGLU-devel as requires for devel package
- Dropped superfluous documentation from devel package
- Added provides to offer lower case alias in preparation for probable
  policy change
- Replace autoconf generated config.h in devel package to avoid potential
  define collisions
- Replace source URL with primary sf site, rather than a mirror
- Fix ilu_region.h to use IL\il.h and not ilu_internal.h and roll into
  a single patch incorporating previous header fixes.

* Sat May 27 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.5.rc1.iss
- Added patch to stop linking against alleg_unsharable, otherwise non PIC code
  is included in the library
- Use %%{?dist} for most recent changelog entry - avoids incoherent changelog
  versions if %%{?dist} macro is missing or different.

* Fri May 26 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.4.rc1.iss
- Made zlib-devel and xorg-x11-devel explicit buildrequires
- Corrected release name format to 0.%%{X}.%%{alphatag} from 0.%%{alphatag}.%%{X}
- Added -q to %%setup
- Added %%{version}-%%{release} to provides field

* Sun May 21 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.RC1.3.iss
- Use Fedora's libtool, seems to fix rpaths problem on x86_64.

* Sun May 14 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.RC1.2.iss
- Now compiled against allegro

* Sat May 13 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.6.8-0.RC1.1.iss
- Initial Release
