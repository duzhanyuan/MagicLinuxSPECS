Name:           perl-MooseX-Attribute-Chained
Version:        1.0.1
Release:        10%{?dist}
Summary:        Attribute that returns the instance to allow for chaining
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MooseX-Attribute-Chained/
Source0:        http://www.cpan.org/authors/id/P/PE/PERLER/MooseX-Attribute-Chained-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(Try::Tiny)
# for release testing, but they mostly fail
#BuildRequires:  perl(Pod::Coverage::TrustPod)
#BuildRequires:  perl(Test::HasVersion)
#BuildRequires:  perl(Test::Kwalitee)
#BuildRequires:  perl(Test::MinimumVersion)
#BuildRequires:  perl(Test::Pod)
#BuildRequires:  perl(Test::Pod::Coverage)
#BuildRequires:  perl(Test::Portability::Files)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# renamed from perl-MooseX-ChainedAccessors in January 2012
# no explicit provides necessary as this package still contains the old classes
# and rpm automatically detects them
Obsoletes:      perl-MooseX-ChainedAccessors <= 0.02-3.fc17

%?perl_default_filter

%description
MooseX::Attribute::Chained is a Moose Trait which allows for method
chaining on accessors by returning $self on write/set operations.

%prep
%setup -q -n MooseX-Attribute-Chained-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 1.0.1-10
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.0.1-9
- 为 Magic 3.0 重建

* Thu Jun 19 2014 Liu Di <liudidi@gmail.com> - 1.0.1-8
- 为 Magic 3.0 重建

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.0.1-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.0.1-2
- Perl 5.16 rebuild

* Fri Jan 20 2012 Iain Arnell <iarnell@gmail.com> 1.0.1-1
- renamed from perl-MooseX-ChainedAccessors
- specfile regenerated by cpanspec

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.02-2
- Perl mass rebuild

* Sat Apr 02 2011 Iain Arnell <iarnell@gmail.com> 0.02-1
- Specfile autogenerated by cpanspec 1.79.
