# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name pureMD5

Name:           ghc-%{pkg_name}
Version:        2.1.2.1
Release:        8%{?dist}
Summary:        Pure Haskell MD5 digest implementation

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-tagged-devel
# End cabal-rpm deps

%description
A Haskell-only implementation of the MD5 digest (hash) algorithm.
This now supports the crypto-api class interface.


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
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 2.1.2.1-8
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 2.1.2.1-7
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 2.1.2.1-5
- update urls

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Jens Petersen <petersen@redhat.com> - 2.1.2.1-2
- add static provides to devel

* Tue Sep 10 2013 Jens Petersen <petersen@redhat.com> - 2.1.2.1-1
- simpler summary

* Tue Sep 10 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 2.1.2.1-0
- spec file generated by cabal-rpm-0.8.3

* Sat Oct 30 2010 Ben Boeckel <mathstuf@gmail.com> - 2.1.0.2-1
- Update to 2.1.0.2

* Mon Oct 18 2010 Ben Boeckel <mathstuf@gmail.com> - 2.1.0.1-1
- Update to 2.1.0.1

* Thu Sep 23 2010 Ben Boeckel <mathstuf@gmail.com> - 2.1.0.0-1
- Update to 2.1.0.0

* Sat Sep 04 2010 Ben Boeckel <mathstuf@gmail.com> - 1.1.0.0-1
- Initial package

* Sat Sep  4 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 1.1.0.0-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.2
