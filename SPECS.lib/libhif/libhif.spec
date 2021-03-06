Summary:   Simple package library built on top of hawkey and librepo
Summary(zh_CN.UTF-8): 在 hawkey 和 librepo 上构建的简单包库
Name:      libhif
Version: 0.2.1
Release: 3%{?dist}
License:   LGPLv2+
URL:       https://github.com/hughsie/libhif
Source0:   http://people.freedesktop.org/~hughsient/releases/libhif-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.16.1
BuildRequires: libtool
BuildRequires: docbook-utils
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: hawkey-devel >= 0.4.6
BuildRequires: rpm-devel >= 4.11.0
BuildRequires: librepo-devel >= 1.1.5
BuildRequires: libsolv-devel

%description
This library provides a simple interface to hawkey and librepo and is currently
used by PackageKit and rpm-ostree.

%description -l zh_CN.UTF-8
在 hawkey 和 librepo 上构建的简单包库。

%package devel
Summary: GLib Libraries and headers for libhif
Summary(zh_CN.UTF-8): %{name} 的开发包
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
GLib headers and libraries for libhif.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q

%build
%configure \
        --enable-gtk-doc \
        --disable-static \
        --disable-silent-rules

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libhif*.la
magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md AUTHORS NEWS COPYING
%{_libdir}/libhif.so.1*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/libhif.so
%{_libdir}/pkgconfig/libhif.pc
%dir %{_includedir}/libhif
%{_includedir}/libhif/*.h
%{_datadir}/gtk-doc
%{_datadir}/gir-1.0/*.gir

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 0.2.1-3
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 0.2.1-2
- 为 Magic 3.0 重建

* Thu Jul 30 2015 Liu Di <liudidi@gmail.com> - 0.2.1-1
- 更新到 0.2.1

* Mon Apr 13 2015 Liu Di <liudidi@gmail.com> - 0.2.0-1
- 更新到 0.2.0

* Sun Apr 05 2015 Liu Di <liudidi@gmail.com> - 0.1.2-6
- 为 Magic 3.0 重建

* Sun Aug 10 2014 Liu Di <liudidi@gmail.com> - 0.1.2-5
- 为 Magic 3.0 重建

* Mon Jul 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.2-4
- Rebuilt for hawkey soname bump

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sat Jul 19 2014 Kalev Lember <kalevlember@gmail.com> 0.1.2-2
- Fix a PK crash with locally mounted iso media (#1114207)

* Thu Jul 17 2014 Richard Hughes <richard@hughsie.com> 0.1.2-1
- Update to new upstream version
- Add HifContext accessor in -private for HifState
- Add name of failing repository
- Create an initial sack in HifContext
- Error if we can't find any package matching provided name
- Fix a mixup of HifStateAction and HifPackageInfo
- Improve rpm callback handling for packages in the cleanup state
- Only set librepo option if value is set
- Respect install root for rpmdb Packages monitor

* Mon Jun 23 2014 Richard Hughes <richard@hughsie.com> 0.1.1-1
- Update to new upstream version
- Fix a potential crash when removing software
- Only add system repository if it exists
- Pass install root to hawkey

* Tue Jun 10 2014 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial version for Fedora package review

