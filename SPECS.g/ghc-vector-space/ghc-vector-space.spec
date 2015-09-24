# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name vector-space

Name:           ghc-%{pkg_name}
Version:        0.8.6
Release:        8%{?dist}
Summary:        Vector and affine spaces, linear maps, and derivatives

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-Boolean-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-NumInstances-devel
# End cabal-rpm deps

%description
Classes and generic operations for vector spaces and affine spaces.
It also defines a type of infinite towers of generalized derivatives.
A generalized derivative is a linear transformation rather than one of
the common concrete representations (scalars, vectors, matrices, ...).


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
%doc COPYING
%{_docdir}/%{name}-%{version}/COPYING

%files devel -f %{name}-devel.files


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.8.6-8
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.8.6-6
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-2
- update to new simplified Haskell Packaging Guidelines

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-1
- update to 0.8.6

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Jens Petersen <petersen@redhat.com> - 0.8.4-1
- update to 0.8.4

* Mon Aug 06 2012 Ben Boeckel <mathstuf@gmail.com> - 0.8.2-1
- Update to 0.8.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-4
- change prof BRs to devel

* Fri Mar 23 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-3
- add license to ghc_files

* Wed Jan  4 2012 Jens Petersen <petersen@redhat.com> - 0.7.6-2
- update to cabal2spec-0.25.2

* Mon Oct 24 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.7.6-1.1
- rebuild with new gmp without compat lib

* Mon Oct  3 2011 Jens Petersen <petersen@redhat.com> - 0.7.6-1
- update to 0.7.6

* Sat Jul 09 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7.3-2
- Update to cabal2spec-0.24

* Mon Jun 20 2011 Ben Boeckel <mathstuf@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Sat Sep 04 2010 Ben Boeckel <mathstuf@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri Sep 03 2010 Ben Boeckel <mathstuf@gmail.com> - 0.5.9-1
- Initial package

* Fri Sep  3 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.5.9-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2