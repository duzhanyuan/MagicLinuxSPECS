%global	gem_name	rspec
%global	rpmgem_name	rspec2

# Disable all auto-requires, specify version2 dependency
# explicitly
%global	__requires_exclude_from %{gem_spec}

Summary:	Behaviour driven development (BDD) framework for Ruby
Name:		rubygem-%{rpmgem_name}
Version:	2.14.1
Release:	7%{?dist}

Group:		Development/Languages
License:	MIT
URL:		http://rspec.info
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	rubygem(rspec2-core)
Requires:	rubygem(rspec2-mocks)
Requires:	rubygem(rspec2-expectations)
Requires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby(release)

BuildArch:	noarch
Provides:	rubygem(%{rpmgem_name}) = %{version}-%{release}
Obsoletes:	rubygem-rspec < 2.14.1-3

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.  

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:		rubygem-rspec-doc < 2.14.1-3

%description	doc
This package contains documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem specification %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%files
%dir	%{gem_instdir}
%{gem_instdir}/lib
%license	%{gem_instdir}/License.txt
%doc	%{gem_instdir}/README.md
%exclude %{gem_cache}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}


%changelog
* Fri Nov 13 2015 Liu Di <liudidi@gmail.com> - 2.14.1-7
- 为 Magic 3.0 重建

* Wed Nov 04 2015 Liu Di <liudidi@gmail.com> - 2.14.1-6
- 为 Magic 3.0 重建

* Thu Sep 24 2015 Liu Di <liudidi@gmail.com> - 2.14.1-5
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.1-3
- Rename to rspec2, cleanup

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 16 2013 Mamoru TASAKA <mtasaka@fedoraproject.og> - 2.14.1-1
- 2.14.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.0-1
- 2.13.0

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 2.12.0-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.0-1
- Update to Rspec 2.12.0

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.11.0-1
- Update to Rspec 2.11.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 05 2012 Vít Ondruch <bkabrda@redhat.com> - 2.8.0-1
- Update to RSpec 2.8.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 07 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.1-1
- Update from Marek Goldmann <mgoldman@redhat.com>
  - Updated to 1.3.1
  - Patch to make it work with Rake >= 0.9.0.beta.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 16 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-2
- Removed 404 URL in the description (bug 515042)

* Fri Apr 09 2010 Michael Stahnke <stahnma@fedpraproject.org> - 1.3.0-1
- Updated to 1.3.0

* Wed Dec 09 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.9-1
- New Version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.7-1
- New Version

* Fri Mar 27 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.2-1
- New Version 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 08 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.11-1
- New Version

* Mon Nov 03 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-3
- Updating to require ruby(abi)

* Mon Oct 13 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-1
- New version

* Wed May 14 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.3-1
- Initial package
