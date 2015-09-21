# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name executable-path

Name:           ghc-%{pkg_name}
Version:        0.0.3
Release:        10%{?dist}
Summary:        Find out the full path of an executable

License:        Public Domain
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
The documentation of "System.Environment.getProgName" says that
"However, this is hard-to-impossible to implement on some non-Unix OSes,
so instead, for maximum portability, we just return the leaf name
of the program as invoked." This library tries to provide the missing path.


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
* Sun Sep 20 2015 Liu Di <liudidi@gmail.com> - 0.0.3-10
- 为 Magic 3.0 重建

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Jens Petersen <petersen@fedoraproject.org> - 0.0.3-8
- cblrpm refresh

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.0.3-4
- update to new simplified Haskell Packaging Guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.0.3-2
- update with cabal-rpm

* Sat Sep  8 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.0.3-1
- spec file template generated by cabal2spec-0.25.5

* Tue May 10 2011 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 0.0.2-1
- License is PublicDomain

* Tue May 10 2011 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 0.0.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.22.7
