Name:           perl-HTTP-Lite
Version:        2.3
Release:        8%{?dist}
Summary:        Lightweight HTTP implementation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTTP-Lite/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/HTTP-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::Pod)
%endif
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
HTTP::Lite is a stand-alone lightweight HTTP/1.1 implementation for perl. It is
not intended as a replacement for the fully-features LWP module. Instead, it is
intended for use in situations where it is desirable to install the minimal
number of modules to achieve HTTP support, or where LWP is not a good candidate
due to CPU overhead, such as slower processors. HTTP::Lite is also
significantly faster than LWP.

%prep
%setup -q -n HTTP-Lite-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
# most real tests require network access - ignore "skipping test on this
# platform" messages
%if !%{defined perl_bootstrap}
RELEASE_TESTING=1 
%endif

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 2.3-8
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 2.3-7
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 2.3-6
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.3-4
- rebuild for Perl 5.14.1
- apply experimental bootstrap macro

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.3-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Dec 16 2010 Iain Arnell <iarnell@gmail.com> 2.3-1
- update to latest upstream version

* Thu May 13 2010 Iain Arnell <iarnell@gmail.com> 2.2-2
- bump for rebuild against perl 5.12.0

* Thu May 06 2010 Iain Arnell 2.2-1
- Specfile autogenerated by cpanspec 1.78.