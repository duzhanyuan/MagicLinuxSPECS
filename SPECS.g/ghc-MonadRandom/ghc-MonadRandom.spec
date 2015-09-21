# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name MonadRandom

Name:           ghc-%{pkg_name}
Version:        0.3.0.1
Release:        3%{?dist}
Summary:        Random-number generation monad

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
MonadRandom is a random number generation Monad.
It provides support for computations which consume random values.


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
%doc CHANGES.markdown


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.3.0.1-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.3.0.1-1
- update to 0.3.0.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov  1 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.1.12-1
- Updated to new upstream 0.1.12

* Thu Aug 29 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.1.11-1
- Updated to new upstream 0.1.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Jens Petersen <petersen@redhat.com> - 0.1.9-2
- update to new simplified Haskell Packaging Guidelines

* Tue May 21 2013 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.1.9-1
- Updated to new upstream 0.1.9

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.1.8-1
- Updated to new upstream 0.1.8

* Sun Nov 18 2012 Jens Petersen <petersen@redhat.com> - 0.1.6-2
- update with cabal-rpm
- correct license tag to MIT

* Tue Jun 12 2012 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 0.1.6-1
- Added BuildRequires.
- Spec file template generated by cabal2spec-0.25.5.
