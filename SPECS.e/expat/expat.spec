Summary: An XML parser library
Summary(zh_CN.UTF-8): XML 解析库
Name: expat
Version: 2.1.0
Release: 6%{?dist}
Group: System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
Source: http://downloads.sourceforge.net/expat/expat-%{version}.tar.gz
URL: http://www.libexpat.org/
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, automake, libtool, check-devel

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%description -l zh_CN.UTF-8
这是一个 C 语言编写的 XML 解析库。

%package devel
Summary: Libraries and header files to develop applications using expat
Summary(zh_CN.UTF-8): %{name} 的开发包
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: expat = %{version}-%{release}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package static
Summary: expat XML parser static library
Summary(zh_CN.UTF-8): %{name} 的静态库
Group: Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires: expat-devel%{?_isa} = %{version}-%{release}

%description static
The expat-static package contains the static version of the expat library.
Install it if you need to link statically with expat.

%description static -l zh_CN.UTF-8
%{name} 的静态库。

%prep
%setup -q

%build
rm -rf autom4te*.cache
libtoolize --copy --force --automake && aclocal && autoheader && autoconf
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}

rm -f examples/*.dsp
chmod 644 README COPYING Changes doc/* examples/*

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

magic_rpm_clean.sh

%if 0%{?with_check}
%check
make check
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_mandir}/*/*

%files devel
%defattr(-,root,root)
%doc Changes doc examples
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

%files static
%defattr(-,root,root)
%{_libdir}/lib*.a

%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 2.1.0-6
- 为 Magic 3.0 重建

* Thu Oct 29 2015 Liu Di <liudidi@gmail.com> - 2.1.0-5
- 为 Magic 3.0 重建

* Thu Dec 06 2012 Liu Di <liudidi@gmail.com> - 2.1.0-4
- 为 Magic 3.0 重建

* Fri Apr 13 2012 Joe Orton <jorton@redhat.com> - 2.1.0-3
- add -static subpackage (#722647)

* Fri Mar 30 2012 Joe Orton <jorton@redhat.com> - 2.1.0-1
- ship .pc file, move library back to libdir (#808399)

* Mon Mar 26 2012 Joe Orton <jorton@redhat.com> - 2.1.0-1
- update to 2.1.0 (#806602)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  8 2010 Joe Orton <jorton@redhat.com> - 2.0.1-10
- revised fix for CVE-2009-3560 regression (#544996)

* Sun Jan 31 2010 Joe Orton <jorton@redhat.com> - 2.0.1-9
- drop static libraries (#556046)
- add fix for regression in CVE-2009-3560 patch (#544996)

* Tue Dec  1 2009 Joe Orton <jorton@redhat.com> - 2.0.1-8
- add security fix for CVE-2009-3560 (#533174)
- add security fix for CVE-2009-3720 (#531697)
- run the test suite

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.1-5
- Autorebuild for GCC 4.3

* Wed Jan 23 2008 Joe Orton <jorton@redhat.com> 2.0.1-4
- chmod 644 even more documentation (#429806)

* Tue Jan  8 2008 Joe Orton <jorton@redhat.com> 2.0.1-3
- chmod 644 the documentation (#427950)

* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 2.0.1-2
- rebuild

* Wed Aug  8 2007 Joe Orton <jorton@redhat.com> 2.0.1-1
- update to 2.0.1
- fix the License tag
- drop the .la file

* Sun Feb  4 2007 Joe Orton <jorton@redhat.com> 1.95.8-10
- remove trailing dot in Summary (#225742)
- use preferred BuildRoot per packaging guidelines (#225742)

* Tue Jan 30 2007 Joe Orton <jorton@redhat.com> 1.95.8-9
- regenerate configure/libtool correctly (#199361)
- strip DSP files from examples (#186889)
- fix expat.h compilation with g++ -pedantic (#190244)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 1.95.8-8
- restore .la file for apr-util

* Mon Jan 30 2006 Joe Orton <jorton@redhat.com> 1.95.8-7
- move library to /lib (#178743)
- omit .la file (#170031)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Mar  8 2005 Joe Orton <jorton@redhat.com> 1.95.8-6
- rebuild

* Thu Nov 25 2004 Ivana Varekova <varekova@redhat.com> 1.95.8
- update to 1.95.8

* Wed Jun 16 2004 Jeff Johnson <jbj@jbj.org> 1.95.7-4
- add -fPIC (#125586).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun 11 2004 Jeff Johnson <jbj@jbj.org> 1.95.7-2
- fix: malloc failure from dbus test suite (#124747).

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 22 2004 Joe Orton <jorton@redhat.com> 1.95.7-1
- update to 1.95.7, include COPYING file in main package

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Sep 17 2003 Matt Wilson <msw@redhat.com> 1.95.5-6
- rebuild again for #91211

* Tue Sep 16 2003 Matt Wilson <msw@redhat.com> 1.95.5-5
- rebuild to fix gzip'ed file md5sums (#91211)

* Tue Jun 17 2003 Jeff Johnson <jbj@redhat.com> 1.95.5-4
- rebuilt because of crt breakage on ppc64.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 11 2002 Jeff Johnson <jbj@redhat.com> 1.95.5-1
- update to 1.95.5.

* Mon Aug 19 2002 Trond Eivind Glomsrød <teg@redhat.com> 1,95.4-1
- 1.95.4. 1.95.3 was withdrawn by the expat developers.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun  6 2002 Trond Eivind Glomsrød <teg@redhat.com> 1,95.3-1
- 1.95.3

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Mar 22 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Change a prereq in -devel on main package to a req
- License from MIT/X11 to BSD

* Mon Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com>
- 1.95.2

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue Oct 24 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.95.1

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- Create.
