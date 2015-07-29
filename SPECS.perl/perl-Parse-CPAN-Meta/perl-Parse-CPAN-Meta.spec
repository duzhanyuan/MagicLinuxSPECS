Name:           perl-Parse-CPAN-Meta
# dual-lifed module needs to match the epoch in perl.spec
Epoch:          1
Version:        1.4414
Release:        5%{?dist}
Summary:        Parse META.yml and META.json CPAN meta-data files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parse-CPAN-Meta/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.011
# CPAN::Meta needs Parse::CPAN::Meta
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
%endif
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(JSON::PP) >= 2.27200
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(JSON::PP) >= 2.27200
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Parse::CPAN::Meta is a parser for META.json and META.yml files, using
JSON::PP and/or CPAN::Meta::YAML.

%prep
%setup -q -n Parse-CPAN-Meta-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1:1.4414-5
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 1:1.4414-4
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4414-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr  8 2014 Paul Howarth <paul@city-fan.org> - 1:1.4414-2
- Don't BR: CPAN::Meta & CPAN::Meta::Requirements when bootstrapping

* Wed Mar 12 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.4414-1
- Upstream update.
- Reflect upstream R:/BR:-changes.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 1:1.4404-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:1.4404-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Petr Pisar <ppisar@redhat.com> - 1:1.4404-4
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4404-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1:1.4404-2
- Perl 5.16 rebuild

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 1:1.4404-1
- update to latest upstream version

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 1:1.4403-1
- update to latest upstream version

* Wed Feb 08 2012 Iain Arnell <iarnell@gmail.com> 1:1.4402-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.4401-2
- Perl mass rebuild

* Wed Feb 16 2011 Iain Arnell <iarnell@gmail.com> 1:1.4401-1
- update to latest upstream version (removes Module::Load::Conditional dep)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4400-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 1:1.4400-1
- update to latest upstream version

* Fri Feb 04 2011 Iain Arnell <iarnell@gmail.com> 1:1.4200-2
- install to vendorlib again

* Fri Jan 28 2011 Iain Arnell <iarnell@gmail.com> 1:1.4200-1
- Specfile autogenerated by cpanspec 1.78.
- bump epoch to match that in perl.spec
- install to privlib, not vendorlib

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-2
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.40-1
- new upstream version

* Thu Jul 30 2009 Jesse Keating <jkeating@redhat.com> - 1.39-2
- Bump for F12 mass rebuild

* Sun Jun 14 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.39-1
- auto-update to 1.39 (by cpan-spec-update 0.01)

* Mon Apr 27 2009 Ralf Corsépius <corsepiu@fedoraproject> - 0.05-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Steven Pritchard <steve@kspei.com> 0.04-1
- Update to 0.04.
- Update Source0 URL.
- Add version to Test::More dep.
- LICENSE and README went away.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.03-1
- Specfile autogenerated by cpanspec 1.75.
- BR Test::More.