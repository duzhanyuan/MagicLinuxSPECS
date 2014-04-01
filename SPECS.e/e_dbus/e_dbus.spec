Summary:        Wrappers around D-Bus for EFL based applications
Summary(zh_CN.UTF-8): 基于 EFL 的程序的 D-Bus 接口
Name:           e_dbus
Version:	1.7.10
Release:        1%{?dist}
Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:        MIT
URL:            http://www.enlightenment.org/
Source0:        http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
BuildRequires:  ecore-devel 
BuildRequires:  evas-devel
BuildRequires:  dbus-devel
BuildRequires:  pkgconfig

%description
Basic convenience wrappers around D-Bus to ease integrating D-Bus with EFL based
applications.

%description -l zh_CN.UTF-8
基于 EFL 的程序的 D-Bus 接口。

%package        devel
Summary:        Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:       %{name} = %{version}-%{release} 
Requires:       dbus-devel ecore-devel evas-devel pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
make V=1 %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_bindir}/%{name}_*
#chrpath --delete %{buildroot}%{_bindir}/e-notify-send
#chrpath --delete %{buildroot}%{_libdir}/*.so.*
find %{buildroot} -name '*.la' -delete
magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README ChangeLog
#%{_bindir}/e-notify-send
%{_libdir}/*.so.*
#%{_datadir}/e_dbus/logo.png

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Mar 27 2014 Liu Di <liudidi@gmail.com> - 1.7.10-1
- 更新到 1.7.10

* Thu Nov 07 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.9-1
- Update to 1.7.9

* Tue Sep 24 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.8-1
- Update to 1.7.8

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7.7-1
- upstream release 1.7.7

* Wed May 15 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7.6-1
- upstream release 1.7.6

* Tue Jan 01 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.7.4-1
- initial spec
