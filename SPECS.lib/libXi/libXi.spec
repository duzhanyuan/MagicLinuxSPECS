%global tarball libXi
#global gitdate 20111222
#global gitversion ae0187c87

Summary: X.Org X11 libXi runtime library
Summary(zh_CN.UTF-8): X.Org X11 libXi 运行库
Name: libXi
Version: 1.7.5
Release: 3%{?gitdate:.%{gitdate}git%{gitversion}}%{dist}
License: MIT
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
URL: http://www.x.org

%if 0%{?gitdate}
Source0:    %{tarball}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
%else
Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2
%endif

BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: pkgconfig(inputproto) >= 2.1.99.6
BuildRequires: libX11-devel >= 1.4.99.1
BuildRequires: libXext-devel
BuildRequires: xmlto asciidoc >= 8.4.5

Requires: libX11 >= 1.4.99.1

%description
X.Org X11 libXi runtime library

%description -l zh_CN.UTF-8
X.Org X11 libXi 运行库。

%package devel
Summary: X.Org X11 libXi development package
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
# required by xi.pc
Requires: xorg-x11-proto-devel
Requires: pkgconfig

%description devel
X.Org X11 libXi development package

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q -n %{tarball}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}

# Disable static library creation by default.
%define with_static 0

%build
autoreconf -v --install || exit 1
%configure --disable-specs \
%if ! %{with_static}
	--disable-static
%endif

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXi.so.6
%{_libdir}/libXi.so.6.1.0

%files devel
%defattr(-,root,root,-)
%if %{with_static}
%{_libdir}/libXi.a
%endif
%{_includedir}/X11/extensions/XInput.h
%{_includedir}/X11/extensions/XInput2.h
%{_libdir}/libXi.so
%{_libdir}/pkgconfig/xi.pc
#%dir %{_mandir}/man3x
%{_mandir}/man3/*.3*

%changelog
* Tue Nov 10 2015 Liu Di <liudidi@gmail.com> - 1.7.5-3
- 为 Magic 3.0 重建

* Sun Nov 01 2015 Liu Di <liudidi@gmail.com> - 1.7.5-2
- 更新到 1.7.5

* Fri Aug 08 2014 Liu Di <liudidi@gmail.com> - 1.7.4-1
- 更新到 1.7.4

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 1.6.1-2
- 为 Magic 3.0 重建

* Thu May 03 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.6.1-1
- libXi 1.6.1

* Thu Mar 08 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.6.0-1
- libXi 1.6

* Wed Feb 15 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.3-1
- libXi 1.5.99.3

* Mon Feb 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-4
- Add requires for libX11 to avoid mismatches when updating

* Fri Jan 27 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-3
- Bump libX11-devel requirement up to what configure actually wants

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.99.2-2.20111222gitae0187c87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.99.2-1.20111222.gitae0187c87
- 1.5.99.2 from git

* Wed Dec 21 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-1
- libXi 1.5.0

* Wed Nov 09 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.99.1-1
- Update to 1.4.99.1 (with XI 2.1 support)

* Tue Oct 11 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-3
- Fix 0001-Handle-unknown-device-classes.patch: missing prototype change for
  copy_classes in XIQueryDevice caused parameter corruption (#744960)

* Wed Aug 17 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-2
- 0001-Handle-unknown-device-classes.patch: don't corrupt memory when a
  server sends unknown device classes.

* Tue Jun 07 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.3-1
- libXi 1.4.3

* Mon Mar 21 2011 Adam Jackson <ajax@redhat.com> 1.4.2-1
- libXi 1.4.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.4.1-1
- libXi 1.4.1

* Wed Nov 03 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-1
- libXi 1.4
- disable spec building, don't think they're of much of much use to our
  users.

* Wed Aug 04 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.2-1
- libXi 1.3.2
  libXi 1.3.1 had a bug in the configure script.

* Mon Aug 02 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.1-1
- libXi 1.3.1

* Tue Feb 02 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3-2
- Remove unnecessary libXau-devel BuildRequires.

* Tue Oct 06 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3-1
- libXi 1.3

* Tue Aug 25 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-11.20090825
- Update to today's git master, requires inputproto 1.9.99.902

* Wed Aug 05 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-10.20090805
- Update to today's git master
- Re-enable parallel builds, the man page makefile is fixed now.

* Tue Aug 04 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-9.20090804
- Update to today's git master

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.99-8.20090723
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.2.99-7.20090723
- Un-require xorg-x11-filesystem

* Thu Jul 23 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-6.20090723
- Update to today's git master

* Thu Jul 16 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-5.20090716
- Update to today's git master

* Mon Jul 13 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-4.20090713
- Update to today's git master
- Add commitid file.

* Sun Jul 12 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-3.20090712
- Update to today's git master

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-2.20090619
- Add missing make-git-snapshot.sh

* Fri Jun 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99-1.20090619
- Update to today's git master

* Thu Feb 26 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.1-1
- libXi 1.2.1 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 03 2008 Adam Jackson <ajax@redhat.com> 1.2.0-1
- libXi 1.2.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.3-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Brian Pepple <bpepple@fedoraproject.org> - 1.1.3-3
- Fix pkconfig type on -devel.

* Fri Jan 11 2008 parag <paragn@fedoraproject.org> 1.1.3-2
- Merge-review #226076
- Removed BR:pkgconfig
- Removed XFree86-libs, xorg-x11-libs XFree86-devel, xorg-x11-devel as Obsoletes
- Removed zero-length AUTHORS README file

* Mon Sep 24 2007 Adam Jackson <ajax@redhat.com> 1.1.3-1
- libXi 1.1.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.1.1-2
- Rebuild for build id

* Wed Jul 11 2007 Adam Jackson <ajax@redhat.com> 1.1.1-1
- libXi 1.1.1

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.4-2
- Don't install INSTALL

* Wed Apr 11 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- libXi 1.0.4

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.0.2-1
- Update to 1.0.2

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.1-3.1
- rebuild

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added "Requires: xorg-x11-proto-devel" to devel package for xi.pc
- Remove package ownership of mandir/libdir/etc.

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Replace "makeinstall" with "make install DESTDIR=..." for (#192721)
- Remove package ownership of mandir/libdir/etc.

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-1
- Update to 1.0.1

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Mike A. Harris <mharris@redhat.com> 1.0.0-2
- Bumped and rebuilt

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXi to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXi to version 0.99.2 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Tue Nov 15 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-3
- Added "BuildRequires: libXau-devel", as build fails without it, but does
  not check for it with ./configure.  Bug (fdo#5065)

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXi to version 0.99.1 from X11R7 RC1
- Updated file manifest to find manpages in "man3x"

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
