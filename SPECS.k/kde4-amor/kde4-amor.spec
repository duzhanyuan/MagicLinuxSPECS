#define svn_number rc1
%define real_name amor

%define kde4_enable_final_bool ON

Name: kde4-%{real_name}
Summary: Amusing misuse of resources
Summary(zh_CN.UTF-8): 显示资源使用情况
License: GPL v2 or Later
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
URL: http://ktorrent.org
Version: 4.14.3
Release: 4%{?dist}
%define rversion %version
Source0:  http://download.kde.org/stable/%{rversion}/src/%{real_name}-%{rversion}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= %{version}
BuildRequires: qt4-xmlpatterns-devel >= 4.8.4

%description
Amusing Misuse of Resources animation that sits on top of the curent window.

%description -l zh_CN.UTF-8
在当前窗口的顶端显示资源使用情况。

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
%{kde4_iconsdir}/hicolor/*
%{kde4_xdgappsdir}/*.desktop
%{kde4_appsdir}/*
%{kde4_htmldir}/en/*
%{kde4_dbus_interfacesdir}/*
%{kde4_mandir}/*

%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 4.14.3-4
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 4.14.3-3
- 为 Magic 3.0 重建

* Wed Dec 31 2014 Liu Di <liudidi@gmail.com> - 4.14.3-2
- 更新到 4.14.3

* Fri Oct 31 2014 Liu Di <liudidi@gmail.com> - 4.14.2-2
- 更新到 4.14.2

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-2
- 更新到 4.13.3

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 4.13.2-2
- 更新到 4.13.2

* Thu May 22 2014 Liu Di <liudidi@gmail.com> - 4.13.1-2
- 为 Magic 3.0 重建

* Mon Apr 28 2014 Liu Di <liudidi@gmail.com> - 4.13.0-2
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.9.3-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
