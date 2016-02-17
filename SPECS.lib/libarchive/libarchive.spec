Name:           libarchive
Version: 3.1.2
Release:        7%{?dist}
Summary:        A library for handling streaming archive formats 
Summary(zh_CN.UTF-8): 处理流归档格式的库

Group:          System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:        BSD
URL:            http://www.libarchive.org/
Source0:        http://www.libarchive.org/downloads/libarchive-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires: bison
BuildRequires: sharutils
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: e2fsprogs-devel
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libunistring-devel


%description
Libarchive is a programming library that can create and read several different 
streaming archive formats, including most popular tar variants, several cpio 
formats, and both BSD and GNU ar variants. It can also write shar archives and 
read ISO9660 CDROM images and ZIP archives.

%description -l zh_CN.UTF-8
处理流归档格式的库，包括流行的 tar 格式，一些 cpio 格式，以及 BSD 和 GNU ar 格式。
它也可以写 shar 文档并读取 ISO9660 CD 镜像和 ZIP 归档。

%package        devel
Summary:        Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q -n %{name}-%{version}


%build
%configure --disable-static --disable-bsdtar --disable-bsdcpio
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
iconv -f latin1 -t utf-8 < NEWS > NEWS.utf8; cp NEWS.utf8 NEWS
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'
magic_rpm_clean.sh

%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README NEWS
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Sat Feb 06 2016 Liu Di <liudidi@gmail.com> - 3.1.2-7
- 为 Magic 3.0 重建

* Sat Feb 06 2016 Liu Di <liudidi@gmail.com> - 3.1.2-6
- 为 Magic 3.0 重建

* Mon Nov 09 2015 Liu Di <liudidi@gmail.com> - 3.1.2-5
- 为 Magic 3.0 重建

* Sat Oct 31 2015 Liu Di <liudidi@gmail.com> - 3.1.2-4
- 为 Magic 3.0 重建

* Wed Jul 09 2014 Liu Di <liudidi@gmail.com> - 3.1.2-3
- 更新到 3.1.2

* Wed Jul 09 2014 Liu Di <liudidi@gmail.com> - 3.0.2-3
- 为 Magic 3.0 重建

* Fri Dec 07 2012 Liu Di <liudidi@gmail.com> - 3.0.2-2
- 为 Magic 3.0 重建

* Mon Nov 14 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.0-0.1.a
- Update to 3.0.0a (alpha release)

* Mon Sep  5 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.8.5-1
- Update to 2.8.5

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.8.4-2
- Rebuild for new xz-libs

* Wed Jun 30 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.8.4-1
- Update to 2.8.4

* Fri Jun 25 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.8.3-2
- Fix ISO9660 reader data type mismatches (#597243)

* Tue Mar 16 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.8.3-1
- Update to 2.8.3

* Mon Mar  8 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.8.1-1
- Update to 2.8.1

* Fri Feb  5 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Wed Jan  6 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.7.902a-1
- Update to 2.7.902a

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.7.1-2
- rebuilt with new openssl

* Fri Aug  7 2009 Tomas Bzatek <tbzatek@redhat.com> 2.7.1-1
- Update to 2.7.1
- Drop deprecated lzma dependency, libxz handles both formats

* Mon Jul 27 2009 Tomas Bzatek <tbzatek@redhat.com> 2.7.0-3
- Enable XZ compression format

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 12 2009 Tomas Bzatek <tbzatek@redhat.com> 2.7.0-1
- Update to 2.7.0

* Fri Mar  6 2009 Tomas Bzatek <tbzatek@redhat.com> 2.6.2-1
- Update to 2.6.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tomas Bzatek <tbzatek@redhat.com> 2.6.1-1
- Update to 2.6.1

* Thu Jan  8 2009 Tomas Bzatek <tbzatek@redhat.com> 2.6.0-1
- Update to 2.6.0

* Mon Dec 15 2008 Tomas Bzatek <tbzatek@redhat.com> 2.5.904a-1
- Update to 2.5.904a

* Tue Dec  9 2008 Tomas Bzatek <tbzatek@redhat.com> 2.5.903a-2
- Add LZMA support

* Mon Dec  8 2008 Tomas Bzatek <tbzatek@redhat.com> 2.5.903a-1
- Update to 2.5.903a

* Tue Jul 22 2008 Tomas Bzatek <tbzatek@redhat.com> 2.5.5-1
- Update to 2.5.5

* Wed Apr  2 2008 Tomas Bzatek <tbzatek@redhat.com> 2.4.17-1
- Update to 2.4.17

* Wed Mar 18 2008 Tomas Bzatek <tbzatek@redhat.com> 2.4.14-1
- Initial packaging
