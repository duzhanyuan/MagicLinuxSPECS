#define svn_number rc1
%define real_name kbruch

%define kde4_enable_final_bool OFF

Name: kde4-%{real_name}
Summary: Exercise Fractions and Percentages
Summary(zh_CN.UTF-8): 分数和百分数练习
License: GPL v2 or Later
Group: User Interface/Desktops
Group(zh_CN.UTF-8): 用户界面/桌面
URL: http://ktorrent.org
Version: 4.13.3
Release: 1%{?dist}
Source0: http://download.kde.org/stable/%{version}/src/%{real_name}-%{version}.tar.xz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: cmake >= 2.6.2
BuildRequires: gettext
BuildRequires: libkdelibs4-devel >= 4.0.82


%description
Exercise Fractions and Percentages

%description -l zh_CN.UTF-8
分数和百分数练习

%prep
%setup -q -n %{real_name}-%{version}

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
#%{kde4_libdir}/*.so.*
#%{kde4_plugindir}/*
%{kde4_iconsdir}/hicolor/*
%{kde4_xdgappsdir}/*.desktop
%{kde4_appsdir}/*
%{kde4_kcfgdir}/*.kcfg
#%{kde4_servicesdir}/*
#%{kde4_servicetypesdir}/*
#%{kde4_configdir}/*
%{kde4_htmldir}/en/*
%{kde4_mandir}/*

%if 0
%files devel
%defattr(-,root,root,-)
%{kde4_includedir}/*
%{kde4_libdir}/*.so
%endif

%changelog
* Fri Jul 18 2014 Liu Di <liudidi@gmail.com> - 4.13.3-1
- 更新到 4.13.3

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 4.13.2-1
- 更新到 4.13.2

* Mon May 26 2014 Liu Di <liudidi@gmail.com> - 4.13.1-1
- 更新到 4.13.1

* Thu Apr 24 2014 Liu Di <liudidi@gmail.com> - 4.13.0-2
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 4.9.3-2
- 为 Magic 3.0 重建

* Tue Aug 11 2009 Ni Hui <shuizhuyuanluo@126.com> - 3.2.3-1mgc
- 更新至 3.2.3
- 拆出开发包
- 己丑  六月廿一
