# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name case-insensitive

%bcond_with tests

Name:           ghc-%{pkg_name}
# part of haskell-platform
Version:        1.1.0.3
Release:        3%{?dist}
Summary:        Case insensitive string comparison

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-text-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
%endif
# End cabal-rpm deps

%description
The module 'Data.CaseInsensitive' provides the 'CI' type constructor which can
be parameterised by a string-like type like: 'String', 'ByteString', 'Text',
etc.. Comparisons of values of the resulting type will be insensitive to cases.


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
%doc README.markdown


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 1.1.0.3-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Jens Petersen <petersen@redhat.com> - 1.1.0.3-1
- update to 1.1.0.3

* Thu Jun 19 2014 Jens Petersen <petersen@redhat.com> - 1.0.0.1-3
- update packaging to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 Jens Petersen <petersen@redhat.com> - 1.0.0.1-1
- update to 1.0.0.1 (now part of Haskell Platform 2013.2)
- update spec file to cabal-rpm-0.8.0

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 1.0-1
- update to 1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 06 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.3-1
- update to 0.4.0.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-5
- change prof BRs to devel

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-4
- rebuild

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-3
- rebuild

* Wed Mar  7 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-2
- rebuild

* Thu Jan  5 2012 Jens Petersen <petersen@redhat.com> - 0.4.0.1-1
- update to 0.4.0.1 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3.0.1-1.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.3.0.1-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.3.0.1-1.1
- rebuild with new gmp

* Sat Oct  8 2011 Jens Petersen <petersen@redhat.com> - 0.3.0.1-1
- update to 0.3.0.1
- depends on hashable

* Tue Sep 13 2011 Jens Petersen <petersen@redhat.com> - 0.2.0.2-2
- rebuild against newer ghc-rpm-macros

* Thu Aug 11 2011 Jens Petersen <petersen@redhat.com> - 0.2.0.2-1
- update to  0.2.0.2

* Thu Jun 30 2011 Jens Petersen <petersen@redhat.com> - 0.2.0.1-1
- BSD
- depends on text

* Thu Jun 30 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.2.0.1-0
- initial packaging for Fedora automatically generated by cabal2spec-0.24
