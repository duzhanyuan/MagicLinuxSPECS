# This file is lincesed under the terms of GNU GPLv2+.
Name:           perl-Perl-Critic-Tics
Version:        0.006
Release:        7%{?dist}
Summary:        Policies for things that make me wince
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Perl-Critic-Tics/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Perl-Critic-Tics-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Perl::Critic) >= 1.07
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Violation)
# Tests only:
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# Plug-in into perlcritics. Require it.
Requires:       perl(Perl::Critic) >= 1.07
Requires:       perl(Perl::Critic::Violation)

%description
The Perl-Critic-Tics distribution includes extra policies for Perl::Critic
to address a fairly random assortment of things that make me (rjbs) wince.

%prep
%setup -q -n Perl-Critic-Tics-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.006-7
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.006-6
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Petr Pisar <ppisar@redhat.com> - 0.006-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.006-2
- Perl mass rebuild

* Tue Jan 25 2011 Petr Pisar <ppisar@redhat.com> 0.006-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Remove explicit defattr