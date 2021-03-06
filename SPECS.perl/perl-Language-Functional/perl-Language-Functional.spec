Name:           perl-Language-Functional
Version:        0.05
Release:        8%{?dist}
Summary:        Module which makes Perl slightly more functional
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Language-Functional/
Source0:        http://www.cpan.org/authors/id/L/LB/LBROCARD/Language-Functional-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Tie::Array)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(InfiniteList\\)

%description
Perl already contains some functional-like functions, such as map and grep.
The purpose of this module is to add other functional-like functions to
Perl, such as foldl and foldr, as well as the use of infinite lists.

%prep
%setup -q -n Language-Functional-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.05-8
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.05-7
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.05-6
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.05-5
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.05-4
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.05-3
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Petr Pisar <ppisar@redhat.com> - 0.05-1
- 0.05 bump
- Remove RPM 4.8 filter

* Mon Jul 25 2011 Petr Pisar <ppisar@redhat.com> - 0.04-3
- RPM 4.9 dependency filtering added

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 0.04-2
- Perl mass rebuild

* Tue Jun 14 2011 Petr Pisar <ppisar@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot and defattr stuff
- Do not provides private module InfiniteList
- Fix any() and all() implementation (CPAN RT #20698)
