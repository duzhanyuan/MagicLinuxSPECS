# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name language-ecmascript

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.15.2
Release:        8%{?dist}
Summary:        JavaScript parser and pretty-printer library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-uniplate-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
Tools for working with ECMAScript 3 (popularly known as JavaScript).
Includes a parser, pretty-printer, tools for working with source tree
annotations and an arbitrary instance.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%check
%if %{with tests}
%cabal test
%endif


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc CHANGELOG


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.15.2-8
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr  3 2015 Jens Petersen <petersen@redhat.com> - 0.15.2-6
- rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.15.2-5
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.15.2-3
- F21 rebuild

* Mon Nov 18 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.15.2-2
- Move CHANGELOG to devel subpackage.
- Remove reference to CHANGELOG from description.

* Fri Oct 25 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.15.2-1
- spec file generated by cabal-rpm-0.8.5
