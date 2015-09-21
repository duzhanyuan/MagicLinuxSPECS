# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name entropy

Name:           ghc-%{pkg_name}
Version:        0.3.4.1
Release:        3%{?dist}
Summary:        A platform independent entropy source

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
A platform independent method to obtain cryptographically strong entropy
(RDRAND when available anywhere, urandom on nix, CryptAPI on Windows, patches
welcome). Users looking for cryptographically strong (number-theoretically
sound) PRNGs should see the 'DRBG' package too.


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
%doc README.md


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.3.4.1-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jens Petersen <petersen@redhat.com> - 0.3.4.1-1
- update to 0.3.4.1

* Wed Oct 29 2014 Jens Petersen <petersen@redhat.com> - 0.3.4-1
- update to 0.3.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Jens Petersen <petersen@redhat.com> - 0.2.2.1-4
- drop use of TemplateHaskell from Setup with patch from 0.2.2.2
  so no longer need to restrict arch's (#992363)

* Tue Jul  8 2014 Jens Petersen <petersen@redhat.com> - 0.2.2.1-3
- update to cblrpm-0.8.11
- exclude arm due to TH segfault

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Jens Petersen <petersen@redhat.com> - 0.2.2.1-1
- update to 0.2.2.1
- Setup now uses Template Haskell
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.1-1
- spec file generated by cabal-rpm-0.7.1
