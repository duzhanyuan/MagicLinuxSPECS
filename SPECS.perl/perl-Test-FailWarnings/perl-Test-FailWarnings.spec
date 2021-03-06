Name:           perl-Test-FailWarnings
Version:        0.008
Release:        6%{?dist}
Summary:        Add test failures if warnings are caught
License:        ASL 2.0 

URL:            http://search.cpan.org/dist/Test-FailWarnings/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

# tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Script)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More's
fail() calls. It is designed to be used with done_testing, when you don't
need to know the test count in advance.

%prep
%setup -q -n Test-FailWarnings-%{version}

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
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.008-6
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.008-5
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.008-4
- 为 Magic 3.0 重建

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 0.008-3
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.008-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.008-1
- Update to 0.008

* Sun Sep 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.007-1
- Update to 0.007

* Sun Aug 25 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.006-1
- Update to 0.006

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Petr Pisar <ppisar@redhat.com> - 0.005-2
- Perl 5.18 rebuild

* Wed May 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.005-1
- Update to 0.005

* Fri May 03 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.003-2
- Take into account review comments (#957466)

* Sun Apr 28 2013 Emmanuel Seyman <emmanuel@seyman.fr> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
