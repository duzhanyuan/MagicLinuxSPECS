Name:           perl-HTML-Tidy
Version:	1.56
Release:	2%{?dist}
Summary:        (X)HTML cleanup in a Perl object
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Tidy/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/HTML-Tidy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# needed by webtidy to fetch URLs
Requires:       perl(LWP::Simple)

# use base 'Exporter';
Requires:       perl(Exporter)

# non-perl
BuildRequires:  libtidyp-devel
# core
BuildRequires: perl(ExtUtils::MakeMaker) 
BuildRequires: perl(Test::Builder) 
BuildRequires: perl(Test::More) 
# test
BuildRequires: perl(Test::Pod) 
BuildRequires: perl(Test::Pod::Coverage)

%{?perl_default_filter}

%description
HTML::Tidy is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user 
looking to migrate, see the section "Converting from HTML::Lint".

%prep
%setup -q -n HTML-Tidy-%{version}

find .  -type f -exec chmod -c -x                              {} +
find .  -type f -exec perl -pi -e 's/\r//'                     {} +
find t/ -type f -exec perl -pi -e 's|^#!perl|#!/usr/bin/perl|' {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} + 
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README* t/
%{perl_vendorarch}/auto/HTML/
%{perl_vendorarch}/HTML/
%{_bindir}/webtidy
%{_mandir}/man3/HTML::Tidy.3pm*
%{_mandir}/man3/HTML::Tidy::Message.3pm*

%changelog
* Sat Oct 03 2015 Liu Di <liudidi@gmail.com> - 1.56-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 1.56-1
- 更新到 1.56

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 1.54-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 1.54-7
- 为 Magic 3.0 重建

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1.54-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.54-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 30 2010 Paul Howarth <paul@city-fan.org> - 1.54-1
- Update to 1.54
- Build against libtidyp rather than libtidy
- License changed from "same as Perl" to Artistic 2.0
- Drop old patch, no longer needed
- README changed to README.markdown
- Add dependencies on perl(Exporter) and perl(LWP::Simple)
- Use %%{?perl_default_filter}

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.08-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.08-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 13 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.08-3
- bump

* Thu Oct 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.08-2
- apply patch from rt tracker
- misc spec cleanups

* Fri May 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.08-1
- Specfile autogenerated by cpanspec 1.71.
