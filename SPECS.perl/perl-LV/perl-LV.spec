Name:           perl-LV
Version:        0.006
Release:        5%{?dist}
Summary:        Perl module to make lvalue subroutines easy and practical
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/LV/
Source0:        http://www.cpan.org/authors/id/T/TO/TOBYINK/LV-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Sentinel)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.47
BuildRequires:  perl(Variable::Magic)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module makes lvalue subroutines easy and practical to use. It's
inspired by the lvalue module which is sadly problematic because of the
existence of another module on CPAN called Lvalue.

%prep
%setup -q -n LV-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes CONTRIBUTING COPYRIGHT CREDITS README
%license LICENSE
%{perl_vendorlib}/LV*
%{_mandir}/man3/LV*

%changelog
* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.006-5
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.006-3
- Perl 5.22 rebuild

* Wed Sep 10 2014 Emmanuel Seyman <emmanuel@seyman.fr> 0.006-2
- Take into account review feedback (#1139009)

* Wed Sep 03 2014 Emmanuel Seyman <emmanuel@seyman.fr> 0.006-1
- Initial specfile, based on the one autogenerated by cpanspec 1.78.