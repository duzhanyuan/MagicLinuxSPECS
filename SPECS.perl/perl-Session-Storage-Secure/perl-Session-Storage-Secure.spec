Name:           perl-Session-Storage-Secure
Version:        0.010
Release:        6%{?dist}
Summary:        Encrypted, expiring, compressed, serialized session data with integrity
License:        ASL 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Session-Storage-Secure/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Session-Storage-Secure-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Math::Random::ISAAC::XS)
BuildRequires:  perl(MIME::Base64) >= 3.12
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike::Base) >= 0.16
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(String::Compare::ConstantTime)
# Tests:
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tolerant)
BuildRequires:  perl(version)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
This module implements a secure way to encode session data. It is primarily
intended for storing session data in browser cookies, but could be used
with other back-end storage where security of stored session data is
important.

%prep
%setup -q -n Session-Storage-Secure-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.010-6
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.010-5
- 为 Magic 3.0 重建

* Thu Sep 17 2015 Liu Di <liudidi@gmail.com> - 0.010-4
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.22 rebuild

* Fri Oct 10 2014 Petr Pisar <ppisar@redhat.com> 0.010-1
- Specfile autogenerated by cpanspec 1.78.
