%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:       gammu
Version:	1.36.7
Release:        1%{?dist}
Summary:        Command Line utility to work with mobile phones
Summary(zh_CN.UTF-8): 操作手机的命令行工具

Group:          Applications/System
Group(zh_CN.UTF-8): 应用程序/系统
License:        GPLv2+
URL:            http://wammu.eu/gammu/
Source0:        http://sourceforge.net/projects/gammu/files/%{name}/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf, gettext, cmake
%ifnarch s390 s390x
BuildRequires:  libusb1-devel
%endif
BuildRequires:  doxygen
BuildRequires:  libdbi-devel, libcurl-devel
# Enabling bluetooth fonction
BuildRequires:  bluez-libs-devel
# Enabling Database sms fonction
BuildRequires:  postgresql-devel, mysql-devel
BuildRequires:  glib2-devel libgudev1-devel

Requires:       bluez, dialog


%package    libs
Summary:    Libraries files for %{name}
Summary(zh_CN.UTF-8): %{name} 的运行库
Group:      System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库

%package -n     python-%{name}
Summary:    Python bindings for Gammu
Summary(zh_CN.UTF-8): %{name} 的 Python 绑定
Group:      Development/Languages
Group(zh_CN.UTF-8): 开发/语言

BuildRequires:  python2-devel
Obsoletes:      python-%{name} <= 0.28

Requires:       %{name} = %{version}-%{release}

%package    devel
Summary:    Development files for %{name}   
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:      Development/Libraries
Group(zh_CN.UTF-8): 开发/库

Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-libs = %{version}-%{release}
Requires:   pkgconfig

%description
Gammu is command line utility and library to work with mobile phones
from many vendors.
Support for different models differs, but basic functions should work
with majority of them. Program can work with contacts,
messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc.
It also supports daemon mode to send and receive SMSes.

%description -l zh_CN.UTF-8
支持多种手机的命令行工具和库。

%description    libs
The %{name}-libs package contains libraries files that used by %{name}

%description libs -l zh_CN.UTF-8
%{name} 的运行库。

%description -n python-%{name}
Python bindings for Gammu library.
It currently does not support all Gammu features,
but range of covered functions is increasing,
if you need some specific, feel free to use bug tracking system for feature 
requests.

%description -n python-%{name} -l zh_CN.UTF-8
%{name} 的 Python 绑定。

%description    devel
The %{name}-devel  package contains Header and libraries files for
developing applications that use %{name}

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q

sed -i 's|${INSTALL_LIB_DIR}|%{_libdir}|' CMakeLists.txt libgammu/CMakeLists.txt \
                              smsd/CMakeLists.txt gammu/CMakeLists.txt

%build
mkdir build
pushd build
%cmake                  \
    -DENABLE_BACKUP=ON      \
    -DWITH_NOKIA_SUPPORT=ON     \
    -DWITH_Bluez=ON         \
    -DWITH_IrDA=ON          \
    -DINSTALL_UDEV_RULES=ON \
    -DWITH_SYSTEMD=ON       \
    -DINSTALL_GNAPPLET=ON       \
    -DINSTALL_MEDIA=ON       \
    -DINSTALL_PHP_EXAMPLES=ON       \
    -DINSTALL_BASH_COMPLETION=ON       \
    -DINSTALL_DOC=ON       \
    -DINSTALL_LOC=ON       \
    ../
make
popd

##fix lines ending 
#for docs in \
#   docs/develop/{protocol/'*',sounds/*,sms/'*'}    \
#   docs/develop/{*.htm,*.txt}          \
#   docs/user/*.* ; do
#   sed -e 's/\r//' -i $docs
#done


%install
make -C build  install DESTDIR=$RPM_BUILD_ROOT

# Install config file
install -pm 0644 docs/config/smsdrc %{buildroot}%{_sysconfdir}/gammu-smsdrc 

magic_rpm_clean.sh
%find_lang %{name} || :
%find_lang lib%{name} || :
cat lib%{name}.lang >> %{name}.lang


%post -n %{name}-libs -p /sbin/ldconfig

%postun -n %{name}-libs -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/README.rst
%doc %{_docdir}/%{name}/ChangeLog 
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/examples
%{_bindir}/%{name}*
%{_bindir}/jadmaker
%{_mandir}/man1/*.gz
%{_mandir}/man5/*.gz
%{_mandir}/man7/*.gz
#%{_mandir}/cs/man1/*.gz
#%{_mandir}/cs/man5/*.gz
#%{_mandir}/cs/man7/*.gz
%{_datadir}/%{name}
%{_sysconfdir}/udev/rules.d/69-gammu-acl.rules
%{_unitdir}/gammu-smsd.service
%{_datadir}/bash-completion/completions/gammu
%{_sysconfdir}/gammu-smsdrc

%files      libs
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n       python-%{name}
%defattr(-,root,root,-)
#%{python_sitearch}/%{name}

%files      devel
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/manual
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}


%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 1.36.6-6
- 为 Magic 3.0 重建

* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 1.36.6-5
- 为 Magic 3.0 重建

* Thu Oct 29 2015 Liu Di <liudidi@gmail.com> - 1.36.6-4
- 更新到 1.36.6

* Mon Jul 14 2014 Liu Di <liudidi@gmail.com> - 1.33.0-3
- 为 Magic 3.0 重建

* Wed Jan 22 2014 Sérgio Basto <sergio@serjux.com> - 1.33.0-2
- Rebuild for newer libdbi

* Sat Sep 07 2013 Sérgio Basto <sergio@serjux.com> - 1.33.0-1
- Update to lastest release. 
- Pack all docs.
- fixed W: mixed-use-of-spaces-and-tabs with vim :retab 

* Sat Aug 31 2013 Sérgio Basto <sergio@serjux.com> - 1.30.0-1
- Add BuildRequires glib2-devel libgudev1-devel  
- Change mysql to mariadb.
- Thu Sep 29 2011 Karel Volny <kvolny@redhat.com>
  - Update release.
  - Patch gammu-1.26.1-exec.patch no longer needed.
  - Some docs are no longer present.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.26.1-8
- Update bluez run time requirements

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.26.1-6
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 31 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.26.1-4
- Remove -Werror* from build flags. Needs real fix.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 10 2010 Dan Horák <dan[at]danny.cz> - 1.26.1-2
- build without USB on s390(x)
- fixed FTBFS #555451

* Thu Dec 03 2009 Xavier Lamien <laxathom@fedoraproject.org> - 1.26.1-1
- Update release.

* Fri Aug 21 2009 Xavier Lamien <laxathom@fedorarproject.org> - 1.25.92-1
- Update release.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.25.0-2
- rebuilt with new openssl

* Thu Aug 13 2009 Xavier Lamien <laxathom@fedorarproject.org> - 1.25.0-1
- Update release.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.24.0-2
- Build with $RPM_OPT_FLAGS, use %%cmake macro.

* Wed Apr 29 2009 Xavier Lamien <lxtnow@gmail.com> - 1.24.0-1
- Update release.

* Tue Apr 14 2009 Xavier Lamien <lxtnow@gmail.com> - 1.23.92-1
- Update release.

* Sun Apr 12 2009 Xavier Lamien <lxntow@gmail.com> - 1.23.1-1
- Update release.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Xavier Lamien <lxtnow@gmail.com> - 1.22.94-1
- Update release.

* Mon Jan 26 2009 Xavier Lamien <lxtnow@gmail.com> - 1.22.90-3
- Make _libdir in a good shape.

* Mon Jan 26 2009 Tomas Mraz <tmraz@redhat.com> - 1.22.90-2
- rebuild with new openssl and mysql

* Sun Jan 11 2009 Xavier Lamien <lxtnow[at]gmail.com> - 1.22.90-1
- Update release.

* Tue Dec 30 2008 Jan ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.22.1-2
- Update release.
- -DENABLE_SHARED=ON replaced by -DBUILD_SHARED_LIBS=ON

* Sat Oct 11 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.21.0-1
- Update release.

* Thu Sep 11 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.20.90-2
- Rebuild against new libbluetooth.

* Mon Aug 25 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.20.90-1
- Update release.

* Mon Aug 25 2008 Xavier Lamien <lxntow[at]gmail.com> - 1.20.0-1
- Update release.

* Mon Jun 02 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.19.0-2
- Added Require dialog.

* Thu Apr 17 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.19.0-1
- Updated Release.

* Fri Feb 29 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.18.91-1
- Updated Release.

* Thu Feb 28 2008 Xavier Lamien <lxtnow[at]gmail.com> - 1.18.0-1
- Updated Release.

* Sat Jan 26 2008 Xavier Lamien < lxtnow[at]gmail.com > - 1.17.92-1
- Updated Release.
- Included new binary file.

* Sat Dec 22 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.17.0-1
- Updated Release.

* Fri Oct 12 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.13.0-1
- Updated Release.

* Wed Aug 01 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.12.92-1
- Updated Release.

* Wed Jul 25 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.12.91-1
- Updated Release.

* Thu May 24 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.11.0-1
- Updated release.

* Wed May 23 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.10.6-1
- Updated release.

* Tue May 08 2007 Xavier Lamien < lxtnow[at]gmail.com > - 1.10.0-1
- Initial RPM release.
