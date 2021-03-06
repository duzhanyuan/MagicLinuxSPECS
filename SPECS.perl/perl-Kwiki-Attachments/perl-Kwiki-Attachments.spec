Name:           perl-Kwiki-Attachments
Version:        0.21
Release:        20%{?dist}
Summary:        Kwiki Page Attachments Plugin
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Kwiki-Attachments/
Source0:        http://www.cpan.org/authors/id/S/SU/SUE/Kwiki-Attachments-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Kwiki) >= 0.37
Requires:       perl(Kwiki) >= 0.37
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module gives a Kwiki wiki the ability to upload, store and manage file
attachments on any page. Thumbnails will be created for supported file
types if Imager or Image::Magick is installed. For more information, read
the module POD.

%prep
%setup -q -n Kwiki-Attachments-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.21-20
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 0.21-19
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Liu Di <liudidi@gmail.com> - 0.21-18
- 为 Magic 3.0 重建

* Mon Jun 16 2014 Liu Di <liudidi@gmail.com> - 0.21-17
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.21-16
- 为 Magic 3.0 重建

* Sun Jun 15 2014 Liu Di <liudidi@gmail.com> - 0.21-15
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.21-14
- 为 Magic 3.0 重建

* Sat Jun 14 2014 Liu Di <liudidi@gmail.com> - 0.21-13
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.21-12
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.21-11
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.21-10
- 为 Magic 3.0 重建

* Fri Jun 13 2014 Liu Di <liudidi@gmail.com> - 0.21-9
- 为 Magic 3.0 重建

* Wed Dec 12 2012 Liu Di <liudidi@gmail.com> - 0.21-8
- 为 Magic 3.0 重建

* Sun Jan 29 2012 Liu Di <liudidi@gmail.com> - 0.21-7
- 为 Magic 3.0 重建

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 22 2011 Petr Sabata <contyk@redhat.com> - 0.21-5
- BuildRequire IO::All

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.21-4
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.21-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 28 2010 Steven Pritchard <steve@kspei.com> 0.21-1
- Update to 0.21.

* Mon Dec 20 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-11
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.18-10
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.18-9
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.18-5
Rebuild for new perl

* Fri Jan 04 2008 Ralf Corsépius <rc040203@freenet.de> 0.18-4
- Update License-tag.
- BR: perl(Test::More) (BZ 419631).

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 0.18-3
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 05 2006 Steven Pritchard <steve@kspei.com> 0.18-2
- Minor spec cleanup.

* Tue Mar 07 2006 Steven Pritchard <steve@kspei.com> 0.18-1
- Specfile autogenerated.
