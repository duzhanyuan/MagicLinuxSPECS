#define svn_number rc1
%define real_name libkdeedu

%define kde4_enable_final_bool OFF

Name: libkdeedu4
Summary: KDEedu's lib
Summary(zh_CN.UTF-8): KDEEdu 组件所需的库文件
License: GPL v2 or Later
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
URL: http://ktorrent.org
Version: 4.14.3
Release: 3%{?dist}
%define rversion %version
Source0: http://download.kde.org/stable/%{rversion}/src/%{real_name}-%{rversion}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82


%description
KDEedu's lib

%description -l zh_CN.UTF-8
KDEEdu 组件所需的库文件

%package devel
Summary: Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发文件
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}

%description devel
Contains the development files.

%description devel -l zh_CN.UTF-8
%{name} 的开发文件。包含 libbtcore 的开发文件。

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

%clean
rm -rf %{buildroot} %{_builddir}/%{buildsubdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
#%{kde4_bindir}/*
%{kde4_libdir}/*.so*
#%{kde4_plugindir}/*
%{kde4_iconsdir}/hicolor/*
#%{kde4_xdgappsdir}/*.desktop
%{kde4_appsdir}/*
#%{kde4_kcfgdir}/*.kcfg
#%{kde4_servicesdir}/*
#%{kde4_servicetypesdir}/*
#%{kde4_configdir}/*
#%{kde4_htmldir}/en/*

%files devel
%defattr(-,root,root,-)
%{kde4_includedir}/*
%{kde4_libdir}/*.so
%{kde4_libdir}/cmake/*
%{kde4_libdir}/*.a

%changelog
* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 4.14.3-3
- 为 Magic 3.0 重建

* Tue Dec 30 2014 Liu Di <liudidi@gmail.com> - 4.14.3-2
- 更新到 4.14.3

* Thu Oct 23 2014 Liu Di <liudidi@gmail.com> - 4.14.2-2
- 更新到 4.14.2

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-2
- 为 Magic 3.0 重建

* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-1
- 更新到 4.13.3

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 4.13.2-1
- 更新到 4.13.2

* Fri May 23 2014 Liu Di <liudidi@gmail.com> - 4.13.1-1
- 更新到 4.13.1

* Thu Apr 24 2014 Liu Di <liudidi@gmail.com> - 4.13.0-2
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.9.3-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
