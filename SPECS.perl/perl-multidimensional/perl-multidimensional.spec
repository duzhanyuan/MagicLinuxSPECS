Name:           perl-multidimensional
Version:	0.011
Release:	3%{?dist}
Summary:        Disables multidimensional array emulation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/multidimensional/
Source0:        http://www.cpan.org/authors/id/I/IL/ILMARI/multidimensional-%{version}.tar.gz
# Lexical::SealRequireHints is only necessary for perl < 5.12
Patch0:         no-Lexical-SealRequireHints.patch
BuildRequires:  perl(B::Hooks::OP::Check) >= 0.19
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(XSLoader)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Perl's multidimensional array emulation stems from the days before the language
had references, but these days it mostly serves to bite you when you typo a
hash slice by using the $ sigil instead of @.

This module lexically makes using multidimensional array emulation a fatal error
at compile time.

%prep
%setup -q -n multidimensional-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
RELEASE_TESTING=1 

%files
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/multidimensional*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.011-3
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.011-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.011-1
- 更新到 0.011

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.010-11
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.010-10
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.010-9
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.010-8
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.010-7
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.010-6
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.010-5
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.010-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Petr Pisar <ppisar@redhat.com> - 0.010-3
- Perl 5.16 rebuild

* Thu May 10 2012 Iain Arnell <iarnell@gmail.com> 0.010-2
- drop unnecessary perl buildrequire

* Mon Apr 09 2012 Iain Arnell <iarnell@gmail.com> 0.010-1
- Specfile autogenerated by cpanspec 1.79.
- remove Lexical::SealRequireHints dependency
