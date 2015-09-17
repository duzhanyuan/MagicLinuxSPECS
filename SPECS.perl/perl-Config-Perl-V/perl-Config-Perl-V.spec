Name:           perl-Config-Perl-V
Version:        0.24
Release:        348%{?dist}
Summary:        Structured data retrieval of perl -V output
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-Perl-V/
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/Config-Perl-V-%{version}.tgz
# Correct example
Patch0:         Config-Perl-V-0.24-Remove-invalid-shellbang.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Optional run-time:
# Digest::MD5 not used at tests
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Conflicts:      perl < 4:5.22.0-347

%description
The command "perl -V" will return you an excerpt from the %%Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.

%prep
%setup -q -n Config-Perl-V-%{version}
%patch0 -p1
chmod -x examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changelog examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jul 01 2015 Petr Pisar <ppisar@redhat.com> 0.24-348
- Specfile autogenerated by cpanspec 1.78.
