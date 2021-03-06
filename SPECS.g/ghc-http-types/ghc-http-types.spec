# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name http-types

%bcond_with tests

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        0.8.5
Release:        5%{?dist}
Summary:        Generic HTTP types for Haskell

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-quickcheck-instances-devel
%endif
# End cabal-rpm deps

%description
Generic HTTP types for Haskell for both client and server code.


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
%{_docdir}/%{name}-%{version}/LICENSE

%files devel -f %{name}-devel.files
%doc README


%changelog
* Fri Dec 04 2015 Liu Di <liudidi@gmail.com> - 0.8.5-5
- 为 Magic 3.0 重建

* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.8.5-4
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.8.5-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 28 2014 Jens Petersen <petersen@redhat.com> - 0.8.5-1
- update to 0.8.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.8.0-4
- update to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.8.0-2
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.8.0-1
- update to 0.8.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.7.3.0.1-1
- update to 0.7.3.0.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.6.11-2
- change prof BRs to devel

* Wed Jun 13 2012 Jens Petersen <petersen@redhat.com> - 0.6.11-1
- update to 0.6.11

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.6.10-1
- update to 0.6.10

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 0.6.9-2
- rebuild

* Sat Mar  3 2012 Jens Petersen <petersen@redhat.com> - 0.6.9-1
- update to 0.6.9

* Thu Jan  5 2012 Jens Petersen <petersen@redhat.com> - 0.6.8-1
- update to 0.6.8 and cabal2spec-0.25.2

* Tue Oct 25 2011 Jens Petersen <petersen@redhat.com> - 0.6.5.1-1.1
- rebuild against new gmp

* Thu Oct 13 2011 Jens Petersen <petersen@redhat.com> - 0.6.5.1-1
- update to 0.6.5.1

* Wed Sep 14 2011 Jens Petersen <petersen@redhat.com> - 0.6.5-2
- rebuild against newer ghc-rpm-macros

* Thu Jun 30 2011 Jens Petersen <petersen@redhat.com> - 0.6.5-1
- BSD
- depends on blaze-builder and case-insensitive

* Thu Jun 30 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.6.5-0
- initial packaging for Fedora automatically generated by cabal2spec-0.24
