Name: libasyncns
Version: 0.8
Release: 7%{?dist}
Summary: Asynchronous Name Service Library
Summary(zh_CN.UTF-8): 异步名称服务库
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
Source0: http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
License: LGPLv2+
Url: http://0pointer.de/lennart/projects/libasyncns/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%description -l zh_CN.UTF-8
异步名称服务库。

%package devel
Summary: Development Files for libasyncns Client Development
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development Files for libasyncns Client Development

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm -rf $RPM_BUILD_ROOT/usr/share/doc/libasyncns/
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 0.8-7
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 0.8-6
- 为 Magic 3.0 重建

* Thu Jul 10 2014 Liu Di <liudidi@gmail.com> - 0.8-5
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 0.8-4
- 为 Magic 3.0 重建

* Thu Jan 05 2012 Liu Di <liudidi@gmail.com> - 0.8-3
- 为 Magic 3.0 重建

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 16 2009 Lennart Poettering <lpoetter@redhat.com> 0.8-1
- New release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New release

* Fri Oct 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New release

* Sat Aug 23 2008 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New release

* Sun Jul 27 2008 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- Initial packaging
