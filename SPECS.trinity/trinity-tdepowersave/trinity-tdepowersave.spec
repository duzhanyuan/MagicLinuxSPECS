#
# spec file for package tdepowersave (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.0.1
%endif
%define tde_pkg tdepowersave
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.7.3
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}.3
Summary:	Power management applet for Trinity
Summary(zh_CN.UTF-8): TDE 下的电源管理小程序
Group:		Applications/Utilities
Group(zh_CN.UTF-8): 应用程序/工具
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9

BuildRequires:	cmake libtool
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# UDEV support
%define with_tdehwlib 1
BuildRequires:	libudev-devel

# XSCREENSAVER support
#  Disabled on RHEL4
%define with_xscreensaver 1
BuildRequires:	libXScrnSaver-devel

# ACL support
BuildRequires:	libacl-devel

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%define with_gamin 1
BuildRequires:	gamin-devel

Obsoletes:		trinity-kpowersave < %{version}-%{release}
Provides:		trinity-kpowersave = %{version}-%{release}


%description
TDEPowersave is a TDE systray applet which allows to control the power 
management settings and policies of your computer.

Current feature list:
 * support for ACPI, APM and PMU
 * trigger suspend to disk/ram and standby
 * switch cpu frequency policy (between: performance, dynamic and powersave)
 * applet icon with information about AC state, battery fill and battery
   (warning) states
 * applet tooltip with information about battery fill and remaining battery 
   time/percentage
 * autosuspend (to suspend the machine if the user has been inactive for a 
   defined time)
 * a global configurable blacklist with programs which prevent autosuspend
   (e.g. videoplayer and cd burning tools)
 * trigger lock screen and select the lock method
 * KNotify support
 * online help
 * localisations for many languages
 
TDEPowersave supports schemes with following configurable specific 
settings for:
 * screensaver
 * DPMS
 * autosuspend
 * scheme specific blacklist for autosuspend
 * notification settings


%description -l zh_CN.UTF-8
TDE 下的电源管理小程序。

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
	
if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DCONFIG_INSTALL_DIR="%{tde_confdir}" \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build
magic_rpm_clean.sh
%find_lang %{tde_pkg} || :


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_tdeappdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

# Disables automatic poweroff, make sure we match both "kpowersave" and "tdepowersave"
if [ $1 = 1 ] && [ -r /etc/acpi/actions/power.sh ]; then
  %__cp -f "/etc/acpi/actions/power.sh" "/etc/acpi/actions/power.sh.tdepowersavebackup"
  %__sed -i "/etc/acpi/actions/power.sh" -e "s|kpowersave|powersave|"
fi

%postun
update-desktop-database %{tde_tdeappdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

if [ $1 = 0 ] && [ -r "/etc/acpi/actions/power.sh.tdepowersavebackup" ]; then
  %__mv -f "/etc/acpi/actions/power.sh.tdepowersavebackup" "/etc/acpi/actions/power.sh"
fi


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/tdepowersave
%{tde_libdir}/libtdeinit_tdepowersave.la
%{tde_libdir}/libtdeinit_tdepowersave.so
%{tde_tdelibdir}/tdepowersave.la
%{tde_tdelibdir}/tdepowersave.so
%{tde_tdeappdir}/tdepowersave.desktop
%{tde_datadir}/apps/tdepowersave/
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/autostart/tdepowersave-autostart.desktop
%{tde_confdir}/tdepowersaverc

%lang(cs) %{tde_tdedocdir}/HTML/cs/tdepowersave/
%lang(de) %{tde_tdedocdir}/HTML/de/tdepowersave/
%lang(en) %{tde_tdedocdir}/HTML/en/tdepowersave/
%lang(fi) %{tde_tdedocdir}/HTML/fi/tdepowersave/
%lang(hu) %{tde_tdedocdir}/HTML/hu/tdepowersave/
%lang(nb) %dir %{tde_tdedocdir}/HTML/nb
%lang(nb) %{tde_tdedocdir}/HTML/nb/tdepowersave/


%changelog
* Sat Nov 14 2015 Liu Di <liudidi@gmail.com> - 2:0.7.3-1.3
- 为 Magic 3.0 重建

* Thu Nov 05 2015 Liu Di <liudidi@gmail.com> - 2:0.7.3-1.2
- 为 Magic 3.0 重建

* Thu Oct 15 2015 Liu Di <liudidi@gmail.com> - 2:0.7.3-1.1
- 为 Magic 3.0 重建

* Thu Jul 04 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.7.3-1
- Initial release for TDE 14.0.0
