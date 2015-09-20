# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name tf-random

Name:           ghc-%{pkg_name}
Version:        0.5
Release:        3%{?dist}
Summary:        High-quality splittable pseudorandom number generator

# main license is BSD
# brg_types.h is BSD and optionally GPL+
# C code by Doug Whiting is Public Domain
License:        BSD and Public Domain
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-time-devel
# End cabal-rpm deps

%description
This package contains an implementation of a high-quality splittable
pseudorandom number generator. The generator is based on a cryptographic hash
function built on top of the ThreeFish block cipher. See the paper /Splittable
Pseudorandom Number Generators Using Cryptographic Hashing/ by Claessen, Pałka
for details and the rationale of the design.

The package provides the following:

* A splittable PRNG that implements the standard 'System.Random.RandomGen'
class.

* The generator also implements an alternative version of the
'System.Random.TF.Gen.RandomGen' class (exported from "System.Random.TF.Gen"),
which requires the generator to return pseudorandom integers from the full
32-bit range, and contains an n-way split function.

* An alternative version of the 'Random' class is provided, which is linked to
the new 'RandomGen' class, together with 'Random' instances for some integral
types.

* Two functions for initialising the generator with a non-deterministic seed:
one using the system time, and one using the '/dev/urandom' UNIX special file.

The package uses an adapted version of the reference C implementation of
ThreeFish from the reference package of the Skein hash function
(<https://www.schneier.com/skein.html>), originally written by Doug Whiting.

Please note that even though the generator provides very high-quality
pseudorandom numbers, it has not been designed with cryptographic applications
in mind.


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
# for haddock
export LANG=en_US.utf8
%ghc_lib_build


%install
%ghc_lib_install

rm %{buildroot}/%{_pkgdocdir}/LICENSE


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE LICENSE.tf LICENSE.brg


%files devel -f %{name}-devel.files
%doc ChangeLog


%changelog
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar  3 2015 Jens Petersen <petersen@redhat.com> - 0.5-2
- some of the C code is Public Domain (#1196960)

* Fri Feb 27 2015 Jens Petersen <petersen@redhat.com> - 0.5-1
- improve filelists

* Mon Feb  9 2015 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.5
- spec file generated by cabal-rpm-0.9.3