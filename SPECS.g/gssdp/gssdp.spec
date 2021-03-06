Name:          gssdp
Version:       0.14.7
Release:       4%{?dist}
Summary:       Resource discovery and announcement over SSDP

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/%{name}/0.14/%{name}-%{version}.tar.xz

BuildRequires: dbus-glib-devel
BuildRequires: GConf2-devel
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel >= 1.36
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: NetworkManager-devel
BuildRequires: pkgconfig
BuildRequires: vala-tools >= 0.20

Requires: dbus

%description
GSSDP implements resource discovery and announcement over SSDP and is part 
of gUPnP.  GUPnP is an object-oriented open source framework for creating 
UPnP devices and control points, written in C using GObject and libsoup. The 
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libsoup-devel
Requires: glib2-devel
Requires: pkgconfig

%description devel
Files for development with gssdp.

%package utils
Summary: Various GUI utuls for %{name}
Group: Applications/System
Requires: %{name} = %{version}-%{release}

%description utils
This package contains GUI utilies for %{name}.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING README NEWS
%dir %{_datadir}/gssdp
%{_libdir}/libgssdp-1.0.so.*
%{_libdir}/girepository-1.0/GSSDP-1.0.typelib

%files devel
%{_libdir}/libgssdp-1.0.so
%{_libdir}/pkgconfig/gssdp-1.0.pc
%{_includedir}/gssdp-1.0
%{_datadir}/gir-1.0/GSSDP-1.0.gir
%{_datadir}/vala/vapi/gssdp*

%files utils
%{_bindir}/gssdp-device-sniffer
%{_datadir}/gssdp/gssdp-device-sniffer.ui

%files docs
%{_datadir}/gtk-doc/html/%{name}

%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.14.7-4
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 0.14.7-3
- 为 Magic 3.0 重建

* Fri Apr 11 2014 Liu Di <liudidi@gmail.com> - 0.14.7-2
- 为 Magic 3.0 重建

* Tue Feb  4 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.7-1
- 0.14.7 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.7.news

* Sun Nov  3 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.6-1
- 0.14.6 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.6.news

* Mon Sep  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.5-1
- 0.14.5 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.5.news

* Tue Jul 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.4-1
- 0.14.4 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.4.news

* Thu May 30 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.3-1
- 0.14.3 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.3.news

* Tue Mar  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.2-1
- 0.14.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.2.news

* Sat Feb 23 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.1-1
- 0.14.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.1.news

* Wed Feb 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.14.0
- 0.14.0 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.14/gssdp-0.14.0.news

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.13.2-1
- 0.13.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.13/gssdp-0.13.2.news

* Mon Oct 29 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.13.1-1
- 0.13.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.13/gssdp-0.13.1.news

* Sun Oct  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.13.0-1
- 0.13.0 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.13/gssdp-0.13.0.news

* Tue Aug 28 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.2.1-2
- Enable vala bindings

* Tue Aug 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.2.1-1
- 0.12.2.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/gssdp-0.12.2.1.news

* Sun Aug 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.2-1
- 0.12.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/gssdp-0.12.2.news

* Thu Jul 19 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.1-4
- Split utils out to a sub package to reduce libs deps. RHBZ #840689

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.12.1-1
- 0.12.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/gssdp-0.12.1.news

* Tue Nov 08 2011 Adam Jackson <ajax@redhat.com> - 0.12.0-2
- Rebuild to break bogus libpng dep

* Fri Sep  2 2011 Zeeshan Ali <zeenix@redhat.com> - 0.12.0-1
- 0.12.0 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.12/gssdp-0.12.0.news

* Fri Aug  5 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.2-1
- 0.11.2 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.11/gssdp-0.11.2.news

* Sun Jul 17 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.1-1
- 0.11.1 release
- http://ftp.gnome.org/pub/GNOME/sources/gssdp/0.11/gssdp-0.11.1.news

* Thu Jun 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.11.0-1
- 0.11.0 release

* Sat Apr  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.10.0-1
- 0.10.0 stable release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.2-1
- Update to 0.9.2

* Thu Dec  2 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.1-1
- Update to 0.9.1

* Fri Nov 12 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.0-1
- Update to 0.9.0

* Wed Sep 29 2010 jkeating - 0.8.0-3
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> 0.8.0-2
- Rebuild against newer gobject-introspection

* Fri Sep 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0-1
- Update to 0.8.0

* Tue Aug 17 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-6
- Update source URL

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 0.7.2-5
- Rebuild with new gobject-introspection

* Mon Jun 21 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-4
- Fix the build with introspection enabled

* Wed Jun 16 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-3
- Drop gir-devel and gtk-doc requirements

* Sun Apr 11 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-2
- Enable gobject introspection support

* Fri Apr  9 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.2-1
- Update to 0.7.2

* Mon Feb 15 2010 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-2
- Add patch to fix DSO linking. Fixes bug 564764

* Fri Dec  4 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.7.1-1
- Update to 0.7.1

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.7.0-2
- Remove unneeded libglade BR

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.7.0-1
- Update to 0.7.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.4-3
- Move docs to noarch subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.4-1
- New upstream release

* Thu Dec 18 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-3
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-2
- Fix summary

* Mon Oct 27 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.3-1
- New upstream version

* Sun Aug 31 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.2-1
- New upstream version

* Tue Aug 26 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-4
- Move glade files from devel to main rpm

* Tue Aug 12 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-3
- Patch to fix the build in rawhide

* Fri Aug 8 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-2
- Updates based on feedback

* Mon May 19 2008 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.1-1
- Initial package 
