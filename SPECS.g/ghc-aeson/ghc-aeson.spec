# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name aeson

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.8.0.2
Release:        3%{?dist}
Summary:        Fast JSON parsing and encoding

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
# for archs without ghci
Patch1:         aeson-disable-TH.patch

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-test-framework-devel
BuildRequires:  ghc-test-framework-hunit-devel
BuildRequires:  ghc-test-framework-quickcheck2-devel
%endif
# End cabal-rpm deps

%description
A JSON parsing and encoding library optimized for ease of use and
high performance.  Aeson was the father of Jason in Greek mythology.


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
%ifnarch %{ghc_arches_with_ghci}
%patch1 -p1 -b .orig
%endif


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
%doc README.markdown examples


%changelog
* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0.2-3
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.2-1
- update to 0.8.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-2
- disable TH module on arch's without ghci

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-1
- update to 0.6.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-2
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-1
- update to 0.6.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-5
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-3
- rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-2
- rebuild

* Sun May  6 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-1
- update to 0.6.0.2
- build needs ghci

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-2
- depends on dlist for ghc > 7.2

* Mon Feb 27 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-1
- BSD license
- doc files

* Mon Feb 27 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4