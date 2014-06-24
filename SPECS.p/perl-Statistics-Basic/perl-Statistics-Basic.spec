Name:           perl-Statistics-Basic
Version:        1.6607
Release:        8%{?dist}
Summary:        A collection of very basic statistics modules
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Statistics-Basic/
Source0:        http://www.cpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Number::Format) >= 1.42
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Number::Format) >= 1.42

# Remove underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Number::Format\\)$

%description
use Statistics::Basic qw(:all);

my $median = median( 1,2,3 );
my $mean   = mean(  [1,2,3]); # array refs are ok too

my $variance = variance( 1,2,3 );
my $stddev   = stddev(   1,2,3 );

my $correlation = correlation( [1 .. 3], [1 .. 3] );


%prep
%setup -q -n Statistics-Basic-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.6607-8
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 1.6607-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6607-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.6607-2
- Perl 5.16 rebuild

* Thu Jan 26 2012 Petr Pisar <ppisar@redhat.com> - 1.6607-1
- 1.6607 bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6602-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6602-5
- add new filter

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.6602-4
- Perl mass rebuild

* Wed Feb 16 2011 Petr Pisar <ppisar@redhat.com> - 1.6602-3
- Version unversioned Provides

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6602-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Petr Pisar <ppisar@redhat.com> 1.6602-1
- Specfile autogenerated by cpanspec 1.78.
- Remove BuildRoot stuff
- Install into perl core directory
- Description from README
