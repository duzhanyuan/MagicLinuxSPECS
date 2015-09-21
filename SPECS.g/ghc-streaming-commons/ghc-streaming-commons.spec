# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name streaming-commons

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        0.1.10.0
Release:        3%{?dist}
Summary:        Common lower-level functions for streaming data libraries

License:        MIT
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-zlib-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps

%description
Provides low-dependency functionality commonly needed by various streaming data
libraries, such as conduit and pipes.


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
# remove bundled zlib headers
mv include/text_cbits.h .
rm include/*
mv text_cbits.h include/


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
%doc README.md


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.1.10.0-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 03 2015 Jens Petersen <petersen@redhat.com> - 0.1.10.0-1
- update to 0.1.10.0

* Fri Dec 12 2014 Jens Petersen <petersen@redhat.com> - 0.1.7.3-1
- update to 0.1.7.3

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Jens Petersen <petersen@redhat.com> - 0.1.2-3
- enable tests: cblrpm-0.8.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Jens Petersen <petersen@redhat.com> - 0.1.2-1
- shorten summary
- exclude bundled zlib headers

* Thu Apr 24 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2
- spec file generated by cabal-rpm-0.8.11
