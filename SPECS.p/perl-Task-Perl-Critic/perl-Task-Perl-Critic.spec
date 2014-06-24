# This file is licensed under the terms of GNU GPLv2+.
Name:           perl-Task-Perl-Critic
Version:        1.008
Release:        8%{?dist}
Summary:        Install everything Perl::Critic
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Task-Perl-Critic/
Source0:        http://www.cpan.org/authors/id/T/TH/THALJEF/Task-Perl-Critic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module::Build) >= 0.38
# Other requires from META.yml are not needed at build and check time. There
# is no code, no provided modules. Do not BuildRequire them.
# Tests only:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(criticism) >= 1.02
Requires:       perl(Perl::Critic) >= 1.117
Requires:       perl(Perl::Critic::Bangs) >= 1.00
Requires:       perl(Perl::Critic::Compatibility) >= 1.000
Requires:       perl(Perl::Critic::Dynamic) >= 0.05
Requires:       perl(Perl::Critic::Itch)
Requires:       perl(Perl::Critic::Lax) >= 0.007
Requires:       perl(Perl::Critic::Moose)
Requires:       perl(Perl::Critic::More) >= 1.000
Requires:       perl(Perl::Critic::Nits) >= 1.000000
Requires:       perl(Perl::Critic::PetPeeves::JTRAMMELL) >= 0.01
Requires:       perl(Perl::Critic::Pulp) >= 3
Requires:       perl(Perl::Critic::Storable)
Requires:       perl(Perl::Critic::StricterSubs) >= 0.03
# Perl::Critic::Swift: 1.000003 is decimal notion for 1.0.3 version
Requires:       perl(Perl::Critic::Swift) >= 1.0.3
Requires:       perl(Perl::Critic::Tics) >= 0.005
Requires:       perl(Test::Perl::Critic) >= 1.02
Requires:       perl(Test::Perl::Critic::Progressive) >= 0.03

%description
This module does nothing but act as a placeholder. See Task.

%prep
%setup -q -n Task-Perl-Critic-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.008-8
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.008-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.008-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.008-2
- Perl 5.16 rebuild

* Thu Jan 19 2012 Petr Pisar <ppisar@redhat.com> - 1.008-1
- 1.008 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.007-2
- Perl mass rebuild

* Tue Jan 25 2011 Petr Pisar <ppisar@redhat.com> 1.007-1
- Specfile autogenerated by cpanspec 1.78.
- Do not BuildRequire run-time dependencies, they are not used at build and
  check time indeed.
- Remove BuildRoot stuff
- Remove explicit defattr 

