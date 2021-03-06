Name:           perl-constant-defer
Version:	6
Release:	4%{?dist}
Summary:        Constant subs with deferred value calculation
Summary(zh_CN.UTF-8): 常量子程序的延迟计算
License:        GPLv3+
Group:          Development/Libraries
Group(zh_CN.UTF-8): 开发/库
URL:            http://search.cpan.org/dist/constant-defer/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/constant-defer-%{version}.tar.gz
BuildArch:      noarch
# The inc/my_pod2html is not called
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
# Run-Time:
BuildRequires:  perl(Carp)
# Tests:
BuildRequires:  perl(Devel::FindRef)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optionals tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Carp)

%description
constant::defer creates a subroutine which on the first call runs given
code to calculate its value, and on the second and subsequent calls just
returns that value, like a constant. The value code is discarded once run,
allowing it to be garbage collected.

%description -l zh_CN.UTF-8
常量子程序的延迟计算。

%prep
%setup -q -n constant-defer-%{version}
chmod -x examples/*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
magic_rpm_clean.sh

%check
make test

%files
%doc Changes COPYING examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 6-4
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 6-3
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 6-2
- 为 Magic 3.0 重建

* Fri May 08 2015 Liu Di <liudidi@gmail.com> - 6-1
- 更新到 6

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 5-8
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 5-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 5-2
- Perl 5.16 rebuild

* Wed Apr 25 2012 Petr Pisar <ppisar@redhat.com> 5-1
- Specfile autogenerated by cpanspec 1.78.
