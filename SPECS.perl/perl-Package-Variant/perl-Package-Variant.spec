Name:           perl-Package-Variant
Version:        1.003002
Release:        1%{?dist}
Summary:        Parameterizable packages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Package-Variant/
Source0:        http://www.cpan.org/authors/id/M/MS/MSTROUT/Package-Variant-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Import::Into) >= 1
BuildRequires:  perl(Module::Runtime) >= 0.013
BuildRequires:  perl(strictures) >= 2
# Optional runtime
BuildRequires:  perl(Sub::Name)
# Tests only
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Recommends:     perl(Sub::Name)

%description
This module allows you to build packages that return different variations
depending on what parameters are given.

%prep
%setup -q -n Package-Variant-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Sep 01 2015 Petr Šabata <contyk@redhat.com> - 1.003002-1
- 1.003002 bump
- Update upstream URL
- Modernize the spec

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.002002-2
- Perl 5.22 rebuild

* Wed Nov 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.002002-1
- 1.002002 bump
- Update URL

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.001003-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 1.001003-1
- update to latest upstream version

* Wed Feb 20 2013 Iain Arnell <iarnell@gmail.com> 1.001002-2
- R/BR perl(Sub::Name)

* Sun Feb 17 2013 Iain Arnell <iarnell@gmail.com> 1.001002-1
- Specfile autogenerated by cpanspec 1.79.