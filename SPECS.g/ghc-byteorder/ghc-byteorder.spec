# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name byteorder

Name:           ghc-%{pkg_name}
Version:        1.0.4
Release:        7%{?dist}
Summary:        Exposes the native endianness or byte ordering of the system

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros

%description
This package is for working with the native byte-ordering of the system.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE
%{_docdir}/%{name}-%{version}/LICENSE

%files devel -f %{name}-devel.files


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 1.0.4-7
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 1.0.4-5
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jens Petersen <petersen@redhat.com> - 1.0.4-1
- update to 1.0.4

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 1.0.3-3
- update to new simplified Haskell Packaging Guidelines

* Thu Feb 07 2013 Ben Boeckel <mathstuf@gmail.com> - 1.0.3-2
- Initial import into Fedora

* Sat Jan 12 2013 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 1.0.3-1
- spec file generated by cabal-rpm-0.6.6
