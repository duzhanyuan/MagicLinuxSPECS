Name:           perl-Plack-Middleware-MethodOverride
Version:        0.15
Release:        4%{?dist}
Summary:        Override REST methods to Plack apps via POST
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Plack-Middleware-MethodOverride/
Source0:        http://www.cpan.org/authors/id/D/DW/DWHEELER/Plack-Middleware-MethodOverride-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Plack) >= 0.9929
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(URI)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This Plack middleware allows your apps to override any HTTP method over POST.
Specifically, you can provide a query parameter named "x-tunneled-method"
or a header named "x-http-method-override" (as used by Google's APIs).
Either way, the overriding works only via POST requests, not GET.

%prep
%setup -q -n Plack-Middleware-MethodOverride-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Plack*
%{_mandir}/man3/Plack*

%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 0.15-4
- 为 Magic 3.0 重建

* Tue Nov 03 2015 Liu Di <liudidi@gmail.com> - 0.15-3
- 为 Magic 3.0 重建

* Tue Sep 15 2015 Liu Di <liudidi@gmail.com> - 0.15-2
- 为 Magic 3.0 重建

* Wed Aug 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.15-1
- Update to 0.15

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-2
- Perl 5.22 rebuild

* Sun Mar 29 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.14-1
- Update to 0.14

* Sun Mar 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.13-1
- Update to 0.13

* Sun Feb 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.12-1
- Update to 0.12
- Use the %%license tag

* Sun Jan 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.11-1
- Update to 0.11

* Thu Dec 04 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.10-2
- Remove BRs perl(Test::Builder) and perl(Test::Pod::Coverage)
  as they are not used (#1169358)

* Sat Nov 29 2014 Emmanuel Seyman <emmanuel@seyman.fr> 0.10-1
- Specfile autogenerated by cpanspec 1.78.
