# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name dataenc

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        0.14.0.7
Release:        4%{?dist}
Summary:        Data encoding library

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
# End cabal-rpm deps

%description
Data encoding library currently providing Base16, Base32, Base32Hex, Base64,
Base64Url, Base85, Python string escaping, Quoted-Printable, URL encoding,
uuencode, xxencode, and yEncoding.


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
* Fri Dec 04 2015 Liu Di <liudidi@gmail.com> - 0.14.0.7-4
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.14.0.7-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 29 2014 Jens Petersen <petersen@redhat.com> - 0.14.0.7-1
- update to 0.14.0.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.14.0.5-4
- update to cblrpm-0.8.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.14.0.5-2
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.14.0.5-1
- update to 0.14.0.5

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 07 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.4-1
- update to 0.14.0.4

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-3
- change prof BRs to devel

* Thu Mar 22 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-2
- add license to ghc_files

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.14.0.3-1
- update to 0.14.0.3 and cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14.0.2-1.3
- rebuild with new gmp without compat lib

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14.0.2-1.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 0.14.0.2-1.1
- rebuild with new gmp

* Wed Aug 17 2011 Jens Petersen <petersen@redhat.com> - 0.14.0.2-1
- update to 0.14.0.2

* Tue Jun 21 2011 Jens Petersen <petersen@redhat.com> - 0.14-2
- BR ghc-Cabal-devel instead of ghc-prof (cabal2spec-0.23.2)

* Fri Mar 11 2011 Jens Petersen <petersen@redhat.com> - 0.14-1
- update to 0.14

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.13.0.5-2
- Enable build on sparcv9

* Tue Feb 15 2011 Jens Petersen <petersen@redhat.com> - 0.13.0.5-1
- update to 0.13.0.5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Jens Petersen <petersen@redhat.com> - 0.13.0.4-3
- update to cabal2spec-0.22.4

* Thu Nov 25 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.4-2
- update url

* Mon Nov  1 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.4-1
- update to 0.13.0.4

* Thu Aug 19 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.3-1
- update to 0.13.0.3
- build with hscolour and ghc-rpm-macros-0.8.1

* Sat Jun 26 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-3
- sync cabal2spec-0.22

* Sat Apr 24 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-2
- rebuild against ghc-6.12.2
- condition ghc_lib_package

* Sat Jan 23 2010 Jens Petersen <petersen@redhat.com> - 0.13.0.2-1
- BSD license
- summary and description from hackage

* Sat Jan 23 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.13.0.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.21.1
