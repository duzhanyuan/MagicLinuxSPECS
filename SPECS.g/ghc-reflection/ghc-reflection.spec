# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name reflection

Name:           ghc-%{pkg_name}
Version:        1.5.1
Release:        4%{?dist}
Summary:        Reifies arbitrary terms into types that can be reflected back into terms

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
# End cabal-rpm deps

%description
This package provides an implementation of the ideas presented in the paper
"Functional Pearl: Implicit Configurations" by Oleg Kiselyov and Chung-chieh
Shan. However, the API has been streamlined to improve performance.

The original paper can be obtained from
<http://www.cs.rutgers.edu/~ccshan/prepose/prepose.pdf>.

For a summary of the approach taken by this library, along with more motivating
examples, see Austin Seipp's tutorial at
<https://www.fpcomplete.com/user/thoughtpolice/using-reflection>.


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
%doc README.markdown examples


%changelog
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 1.5.1-4
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@redhat.com> - 1.5.1-2
- updates urls

* Wed Oct 1 2014 Ricky Elrod <relrod@redhat.com> - 1.5.1-1
- Latest upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.4
- spec file generated by cabal-rpm-0.8.10
