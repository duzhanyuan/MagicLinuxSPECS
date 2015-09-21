# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name conduit-extra

%bcond_with tests

Name:           ghc-%{pkg_name}
Version:        1.1.7.0
Release:        4%{?dist}
Summary:        Conduit adapters for common libraries

License:        MIT
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-builder-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-hspec-devel
%endif
# End cabal-rpm deps
Obsoletes:      ghc-attoparsec-conduit < 1.2
Obsoletes:      ghc-blaze-builder-conduit < 1.2
Obsoletes:      ghc-network-conduit < 1.2
Obsoletes:      ghc-zlib-conduit < 1.2

%description
The conduit package itself maintains relative small dependencies. The purpose
of this package is to collect commonly used utility functions wrapping other
library dependencies, without depending on heavier-weight dependencies.
The basic idea is that this package should only depend on haskell-platform
packages and conduit.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      ghc-attoparsec-conduit-devel < 1.2
Obsoletes:      ghc-blaze-builder-conduit-devel < 1.2
Obsoletes:      ghc-network-conduit-devel < 1.2
Obsoletes:      ghc-zlib-conduit-devel < 1.2

%description devel
This package provides the Haskell %{pkg_name} library development files.


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


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 1.1.7.0-4
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar  4 2015 Jens Petersen <petersen@redhat.com> - 1.1.7.0-2
- obsolete attoparsec-conduit, blaze-builder-conduit, network-conduit, and
  zlib-conduit

* Wed Mar  4 2015 Jens Petersen <petersen@fedoraproject.org> - 1.1.7.0-1
- update to 1.1.7.0

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 1.0.0.1-3
- update urls

* Fri Sep 12 2014 Jens Petersen <petersen@redhat.com> - 1.0.0.1-2
- disable haddock and no ghc-conduit-extra.files

* Fri Sep 12 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.0.0.1-1
- spec file generated by cabal-rpm-0.9.1
