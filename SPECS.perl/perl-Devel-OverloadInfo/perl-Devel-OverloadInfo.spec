Name:		perl-Devel-OverloadInfo
Version:	0.004
Release:	1%{?dist}
Summary:	Introspect overloaded operators
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Devel-OverloadInfo/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IL/ILMARI/Devel-OverloadInfo-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(overload)
BuildRequires:	perl(Package::Stash) >= 0.14
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(parent)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.88
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Devel::OverloadInfo returns information about overloaded operators for a
given class (or object), including where in the inheritance hierarchy the
overloads are declared and where the code implementing it is.

%prep
%setup -q -n Devel-OverloadInfo-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::OverloadInfo.3*

%changelog
* Fri Aug 14 2015 Paul Howarth <paul@city-fan.org> - 0.004-1
- Update to 0.004
  - Document that existence of undef 'fallback' varies between perl versions
  - Add tests for empty, inherited-only and no overloading
  - Add is_overloaded() function

* Thu Aug 13 2015 Paul Howarth <paul@city-fan.org> - 0.003-1
- Update to 0.003
  - Return an empty hash instead of undef for classes with no overloads
  - Work around overload inheritance corruption before 5.16 (CPAN RT#106379)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.002-3
- Perl 5.22 rebuild

* Fri Nov  7 2014 Paul Howarth <paul@city-fan.org> - 0.002-2
- Sanitize for Fedora submission

* Mon Nov  3 2014 Paul Howarth <paul@city-fan.org> - 0.002-1
- Initial RPM version