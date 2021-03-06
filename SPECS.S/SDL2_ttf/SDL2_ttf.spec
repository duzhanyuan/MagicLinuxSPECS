Name:		SDL2_ttf
Version:	2.0.12
Release:	9%{?dist}
Summary:	TrueType font rendering library for SDL2
Summary(zh_CN.UTF-8): SDL2 的 TrueType 字体渲染库
Group:		System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库
License:	zlib
URL:		http://www.libsdl.org/projects/SDL_ttf/
Source0:	http://www.libsdl.org/projects/SDL_ttf/release/%{name}-%{version}.tar.gz
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL2
applications.
%description -l zh_CN.UTF-8
SDL2 的 TrueType 字体渲染库。

%package devel
Summary:	Development files for %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:		Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SDL2-devel%{?_isa} >= 2.0

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%prep
%setup -q
rm -rf external
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt COPYING.txt

%build
%configure --disable-dependency-tracking --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
magic_rpm_clean.sh

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.txt CHANGES.txt COPYING.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Nov 13 2015 Liu Di <liudidi@gmail.com> - 2.0.12-9
- 为 Magic 3.0 重建

* Wed Nov 04 2015 Liu Di <liudidi@gmail.com> - 2.0.12-8
- 为 Magic 3.0 重建

* Wed Sep 30 2015 Liu Di <liudidi@gmail.com> - 2.0.12-7
- 为 Magic 3.0 重建

* Mon Sep 07 2015 Liu Di <liudidi@gmail.com> - 2.0.12-6
- 为 Magic 3.0 重建

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 2 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.12-2
- delete external directory to drop bundles
- do not own /usr/include/SDL2
- fix unused-direct-shlib-dependency

* Mon Nov 25 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.12-1
- initial package
