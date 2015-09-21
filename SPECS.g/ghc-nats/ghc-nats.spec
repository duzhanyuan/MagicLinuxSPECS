# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name nats

Name:           ghc-%{pkg_name}
Version:        0.2
Release:        3%{?dist}
Summary:        Haskell 98 natural numbers

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-hashable-devel
# End cabal-rpm deps

%description
Natural numbers implemented in Haskell 98.


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
%doc README.markdown


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.2-3
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jens Petersen <petersen@redhat.com> - 0.2-1
- update to 0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Jens Petersen <petersen@redhat.com> - 0.1.2-1
- initial package

* Tue Feb 25 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.2
- spec file generated by cabal-rpm-0.8.10
