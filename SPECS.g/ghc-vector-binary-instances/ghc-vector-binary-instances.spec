# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name vector-binary-instances

Name:           ghc-%{pkg_name}
Version:        0.2.1.0
Release:        8%{?dist}
Summary:        Binary and Serialize instances for vector

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-vector-devel
# End cabal-rpm deps

%description
Instances for Binary for the types defined in the vector package, making it
easy to serialize vectors to and from disk. Uses the generic interface to
vectors, so all vector types are supported. Specific instances are provided
for unboxed, boxed and storable vectors.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library
development files.


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
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.2.1.0-8
- 为 Magic 3.0 重建

* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.2.1.0-7
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.2.1.0-5
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct  4 2013 Jens Petersen <petersen@redhat.com> - 0.2.1.0-2
- add static provides to devel (#1007152)

* Thu Sep 12 2013 Jens Petersen <petersen@redhat.com> - 0.2.1.0-1
- simpler summary

* Thu Sep 12 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.2.1.0-0
- spec file generated by cabal-rpm-0.8.3
