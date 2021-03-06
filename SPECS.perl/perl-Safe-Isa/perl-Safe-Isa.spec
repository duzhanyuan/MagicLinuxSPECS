Name:           perl-Safe-Isa
Version:	1.000005
Release:	3%{?dist}
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Safe-Isa/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
How many times have you found yourself writing:

  if ($obj->isa('Something')) {

and then shortly afterwards cursing and changing it to:

  if (Scalar::Util::blessed($obj) and $obj->isa('Something')) {

Right. That's why this module exists.

%prep
%setup -q -n Safe-Isa-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.000005-3
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.000005-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.000005-1
- 更新到 1.000005

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.000003-5
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000003-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.000003-2
- Perl 5.18 rebuild

* Fri Apr 19 2013 Iain Arnell <iarnell@gmail.com> 1.000003-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 08 2012 Iain Arnell <iarnell@gmail.com> 1.000002-1
- Specfile autogenerated by cpanspec 1.79.
