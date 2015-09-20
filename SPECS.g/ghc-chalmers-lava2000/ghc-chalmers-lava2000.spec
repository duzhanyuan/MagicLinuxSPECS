# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name chalmers-lava2000

Name:           ghc-%{pkg_name}
Version:        1.4.1
Release:        2%{?dist}
Summary:        Hardware description EDSL

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        README.fedora

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
# End cabal-rpm deps

%description
A hardware description library in Haskell.


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
%{__install} -pm 644 %{SOURCE1} .


%build
%ghc_lib_build


%install
%ghc_lib_install


# cleanup extra data files
%{__mv} %{buildroot}%{_datadir}/%{pkg_name}-%{version}/Doc/tutorial.pdf .
%{__rm} %{buildroot}%{_datadir}/%{pkg_name}-%{version}/INSTALL


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc README README.fedora tutorial.pdf
%{_datadir}/%{pkg_name}-%{version}


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 29 2014 Jens Petersen <petersen@redhat.com> - 1.4.1-1
- update to 1.4.1
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 1.3-4
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 1.3-2
- update with cabal-rpm
- include tutorial again and README files

* Sat Sep 29 2012 Shakthi Kannan <shakthimaan at fedoraproject dot org> - 1.3-1
- Updated to 1.3

* Mon Aug 13 2012 Shakthi Kannan <shakthimaan at fedoraproject dot org> - 1.2.0-1
- spec file template generated by cabal2spec-0.25.5
- Updated to 1.2.0

* Thu Dec 29 2011 Shakthi Kannan <shakthimaan [AT] fedoraproject dot org> - 1.1.2-1
- Updated to use cabal2spec-0.24.1.
- Updated to 1.1.2.

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1.1-12.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 1.1.1-12.1
- rebuild with new gmp

* Fri Jun 24 2011 Jens Petersen <petersen@redhat.com> - 1.1.1-12
- BR ghc-Cabal-devel instead of ghc-prof and use ghc_arches (cabal2spec-0.23.2)

* Thu Mar 10 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 1.1.1-11
- Enable build on sparcv9

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Jens Petersen <petersen@redhat.com> - 1.1.1-9
- update to cabal2spec-0.22.4

* Mon Nov 29 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-8
- bump base to 4 for ghc 7
- update url and drop -o obsoletes

* Sat Sep  4 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-7
- add hscolour and doc obsolete (cabal2spec-0.22.2)

* Tue Jun 29 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-6
- update to cabal2spec-0.22.1

* Mon May 24 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-5
- Keep lava.vhd in datadir so users can find it easily (#546376)
- Improve summary and description

* Fri May 21 2010 Jens Petersen <petersen@redhat.com> - 1.1.1-4
- Include the extra data files as doc files instead in the base package

* Tue Apr 13 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-3
- Removed INSTALL file.
- Gzip tutorial.ps and move it to docdir.
- Move Vhdl folder to docdir.
- Removed chalmers folder.

* Thu Apr 08 2010 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-2
- Initial packaging for Fedora automatically generated by cabal2spec-0.21.3.
- Added BSD license.

* Sun Dec 20 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.1-1
- Added README.fedora, instead of using default README.
- Remove Scripts folder.
- Created patch to remove verification modules that use wrapper scripts.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.1.1

* Mon Dec 14 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.1.0-1
- Upstream fixed LAVADIR path as per recommendation.
- Upstream changed import Lava2000 to Lava.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.1.0

* Thu Dec 10 2009 Shakthi Kannan <shakthimaan [AT] gmail dot com> - 1.0.2-1
- Set LAVADIR path with sed.
- Initial packaging for Fedora automatically generated by cabal2spec for 1.0.2
