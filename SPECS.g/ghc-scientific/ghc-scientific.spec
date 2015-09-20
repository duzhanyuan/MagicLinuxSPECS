# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name scientific

Name:           ghc-%{pkg_name}
Version:        0.3.3.1
Release:        2%{?dist}
Summary:        Arbitrary-precision floating-point numbers represented using scientific notation

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-text-devel
# End cabal-rpm deps

%description
A 'Scientific' number is an arbitrary-precision floating-point number
represented using scientific notation.

A scientific number with coefficient 'c' and base10Exponent 'e' corresponds
to the 'Fractional' number: 'fromInteger c * 10 ^^ e'

Its primary use-case is to serve as the target of parsing floating point
numbers. Since the textual representation of floating point numbers use
scientific notation they can be efficiently parsed to a 'Scientific' number.


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


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 1 2014 Ricky Elrod <relrod@redhat.com> - 0.3.3.1-1
- Latest upstream version.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Ricky Elrod <relrod@redhat.com> - 0.3.2.1-1
- Bump to 0.3.2.1

* Sat Mar 15 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.0.2-1
- spec file generated by cabal-rpm-0.8.10