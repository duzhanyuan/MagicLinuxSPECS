#define svn_number rc1
%define real_name filelight

%define kde4_enable_final_bool ON

Name: kde4-%{real_name}
Summary: Graphical disk usage statistics
Summary(zh_CN.UTF-8): 图形化的磁盘使用统计
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
Version: 4.14.3
Release: 2%{?dist}
License: LGPL
URL: http://extragear.kde.org/apps/kipi
%define rversion %version
Source0:  http://download.kde.org/stable/%{rversion}/src/%{real_name}-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82

%description
Graphical disk usage statistics.

%description -l zh_CN.UTF-8
图形化的磁盘使用统计。

%prep
%setup -q -n %{real_name}-%{rversion}

%build
mkdir build
cd build
%cmake_kde4 ..

make %{?_smp_mflags}

%install
cd build
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

magic_rpm_clean.sh

%clean_kde4_desktop_files

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{kde4_bindir}/*
%{kde4_plugindir}/*
%{kde4_appsdir}/*
%{kde4_xdgappsdir}/*.desktop
%{kde4_servicesdir}/*
%{kde4_htmldir}/en/*
%{kde4_configdir}/*
%{kde4_iconsdir}/*

%changelog
* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 4.14.3-2
- 为 Magic 3.0 重建

* Tue Dec 30 2014 Liu Di <liudidi@gmail.com> - 4.14.3-1
- 更新到 4.14.3

* Thu Oct 23 2014 Liu Di <liudidi@gmail.com> - 4.14.2-1
- 更新到 4.14.2

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-1
- 更新到 4.13.3

* Wed Jun 18 2014 Liu Di <liudidi@gmail.com> - 4.13.2-1
- 更新到 4.13.2

* Fri May 23 2014 Liu Di <liudidi@gmail.com> - 4.13.1-1
- 更新到 4.13.1

* Wed Apr 23 2014 Liu Di <liudidi@gmail.com> - 4.13.0-2
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.9.3-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
