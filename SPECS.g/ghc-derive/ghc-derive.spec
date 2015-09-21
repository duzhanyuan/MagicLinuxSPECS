# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name derive

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           ghc-%{pkg_name}
Version:        2.5.22
Release:        3%{?dist}
Summary:        Derive instances for data types

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-syb-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-uniplate-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
# End cabal-rpm deps

%description
Derive is a library and a tool for deriving instances for Haskell programs.
It is designed to work with custom derivations, SYB and Template Haskell
mechanisms.  The tool requires GHC, but the generated code is portable.


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


%files devel -f %{name}-devel.files
%doc README.md
%{_bindir}/%{pkg_name}


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 2.5.22-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 03 2015 Jens Petersen <petersen@redhat.com> - 2.5.22-1
- update to 2.5.22

* Mon Sep 01 2014 Jens Petersen <petersen@redhat.com> - 2.5.16-1
- update to 2.5.16
- refresh to cblrpm-0.8.11

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 2.5.11-3
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 25 2013 Jens Petersen <petersen@redhat.com> - 2.5.11-2
- rebuild

* Tue Mar 12 2013 Jens Petersen <petersen@redhat.com> - 2.5.11-1
- update to 2.5.11

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 2.5.8-7
- update with cabal-rpm

* Fri Nov  2 2012 Jens Petersen <petersen@redhat.com> - 2.5.8-6
- use ghc_arches_with_ghci for template-haskell

* Sat Aug 11 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> -2.5.8-5
- rebuild for libffi

* Wed Jul 18 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 2.5.8-4
- rebuild

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 2.5.8-3
- rebuild

* Mon Jun 18 2012 Jens Petersen <petersen@redhat.com> - 2.5.8-2
- move the derive program to the devel subpackage for now (#831038)

* Sun May  6 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 2.5.8-1
- spec file template generated by cabal2spec-0.25.5
- License is BSD
