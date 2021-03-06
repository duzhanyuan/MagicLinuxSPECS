Name:           pkcs11-helper
Version:        1.10
Release:        6%{?dist}
Summary:        A library for using PKCS#11 providers
Summary(zh_CN.UTF-8): 使用 PKCS#11 的库

Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:        GPLv2 or BSD
URL:            http://www.opensc-project.org/opensc/wiki/pkcs11-helper
Source0:        http://downloads.sourceforge.net/opensc/pkcs11-helper-%{version}.tar.bz2

BuildRequires:  doxygen graphviz
BuildRequires:  openssl-devel

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications using a simple API and optional OpenSSL
engine. The library allows using multiple PKCS#11 providers at the same time,
enumerating available token certificates, or selecting a certificate directly
by serialized id, handling card removal and card insert events, handling card
re-insert to a different slot, supporting session expiration and much more all
using a simple API. 

%description -l zh_CN.UTF-8
使用 PKCS#11 的库。

%package        devel
Summary:        Development files for pkcs11-helper
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:       %{name} = %{version}-%{release}
Requires:       openssl-devel
# for /usr/share/aclocal
Requires:       automake

%description    devel
This package contains header files and documentation necessary for developing
programs using the pkcs11-helper library.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q


%build
%configure --disable-static --enable-doc
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# Use %%doc to install documentation in a standard location
mkdir apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/api/ apidocdir/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/

# Remove libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS ChangeLog COPYING* README THANKS
%{_libdir}/libpkcs11-helper.so.*


%files devel
%doc apidocdir/*
%{_includedir}/pkcs11-helper-1.0/
%{_libdir}/libpkcs11-helper.so
%{_libdir}/pkgconfig/libpkcs11-helper-1.pc
%{_datadir}/aclocal/pkcs11-helper-1.m4
%{_mandir}/man8/pkcs11-helper-1.8*


%changelog
* Sun Feb 14 2016 Liu Di <liudidi@gmail.com> - 1.10-6
- 为 Magic 3.0 重建

* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.10-5
- 为 Magic 3.0 重建

* Sun Nov 01 2015 Liu Di <liudidi@gmail.com> - 1.10-4
- 为 Magic 3.0 重建

* Thu Jul 23 2015 Liu Di <liudidi@gmail.com> - 1.10-3
- 为 Magic 3.0 重建

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Kalev Lember <kalevlember@gmail.com> - 1.10-1
- Update to 1.10

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 17 2011 Kalev Lember <kalevlember@gmail.com> - 1.09-1
- Update to 1.09

* Sun Jun 19 2011 Kalev Lember <kalev@smartlink.ee> - 1.08-1
- Update to 1.08
- Clean up the spec file for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 Kalev Lember <kalev@smartlink.ee> - 1.07-5
- use System Environment/Libraries group for main package
- removed R: pkgconfig from devel subpackage

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.07-4
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-2
- Make devel package depend on automake for /usr/share/aclocal

* Tue Jun 23 2009 Kalev Lember <kalev@smartlink.ee> - 1.07-1
- Initial RPM release.
