Name:           perl-CGI-Application-FastCGI
Version:        0.02
Release:        19%{?dist}
Summary:        For using CGI::Application under FastCGI
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Application-FastCGI/
Source0:        http://www.cpan.org/authors/id/N/NA/NAOYA/CGI-Application-FastCGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(CGI)
BuildRequires:  perl(CGI::Application)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI) >= 0.6
BuildRequires:  perl(Test::More)
Requires:       perl(CGI::Application)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Inherit this module instead of CGI::Application if you want to run your cgi
programs based on CGI::Application under FastCGI.

%prep
%setup -q -n CGI-Application-FastCGI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.02-19
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.02-18
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.02-17
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.02-16
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-15
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-14
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.02-12
- 为 Magic 3.0 重建

* Thu Jun 12 2014 Liu Di <liudidi@gmail.com> - 0.02-11
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.02-10
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.02-9
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.02-8
- 为 Magic 3.0 重建

* Wed Jan 11 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.02-7
- Clean up spec file

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.02-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.02-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.02-4
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Dec 12 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.02-3
- Add perl(CGI) to BuildRequires (#660828).

* Sun Jul 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.02-2
- Add perl(CGI::Application) to Requires

* Fri Mar 05 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
