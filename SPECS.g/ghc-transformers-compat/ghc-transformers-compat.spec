# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name transformers-compat

Name:           ghc-%{pkg_name}
Version:        0.3.3.4
Release:        6%{?dist}
Summary:        Compatibility shim exposing the new types from newer transformers

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
This package includes backported versions of types that were added to
transformers in transformers 0.3 and 0.4 for users who need strict transformers
0.2 or 0.3 compatibility to run on old versions of the platform, but also need
those types.

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
cabal-tweak-flag three True


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
%doc README.markdown


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.3.3.4-6
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.3.3.4-4
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 7 2014 Ricky Elrod <relrod@redhat.com> - 0.3.3.4-2
- Use the cabal flag "three"

* Sat Jul 5 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.3.3.4-1
- spec file generated by cabal-rpm-0.8.90
