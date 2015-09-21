# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name parallel

Name:           ghc-%{pkg_name}
# part of haskell-platform
Version:        3.2.0.4
Release:        3%{?dist}
Summary:        Parallel programming library

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
# End cabal-rpm deps

%description
This package provides a library for parallel programming.


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
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 3.2.0.4-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug  8 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.4-1
- update to 3.2.0.4

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.3-35
- update to cblrpm-0.8.11

* Mon Mar 31 2014 Jens Petersen <petersen@redhat.com> - 3.2.0.3-34
- update to 3.2.0.3 with cabal-rpm

* Tue Mar 20 2012 Jens Petersen <petersen@redhat.com> - 3.2.0.2-1
- update to 3.2.0.2

* Sun Mar 18 2012 Jens Petersen <petersen@redhat.com> - 3.1.0.1-9
- update to cabal2spec-0.25

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.1.0.1-7.3
- rebuild with new gmp without compat lib

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.1.0.1-7.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 3.1.0.1-7.1
- rebuild with new gmp

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-7
- ghc_arches replaces ghc_excluded_archs

* Mon Jun 20 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-6
- BR ghc-Cabal-devel and use ghc_excluded_archs

* Fri May 27 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-5
- update to cabal2spec-0.23: add ppc64

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.0.1-4
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Jens Petersen <petersen@redhat.com> - 3.1.0.1-2
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 3.1.0.1-1
- update to 3.1.0.1
- update url and drop -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-4
- add hscolour and doc obsolete (cabal2spec-0.22.2)

* Sun Jun 27 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-3
- sync cabal2spec-0.22.1

* Tue Apr 27 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-2
- rebuild against ghc-6.12.2

* Wed Mar 24 2010 Jens Petersen <petersen@redhat.com> - 2.2.0.1-1
- update to 2.2.0.1 for haskell-platform-2010.1.0.0
- new dep on deepseq

* Thu Jan 21 2010 Jens Petersen <petersen@redhat.com> - 1.1.0.1-2
- BSD license
- summary and description
- note part of haskell-platform-2009.2.0.2

* Thu Jan 21 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.1.0.1-1
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
