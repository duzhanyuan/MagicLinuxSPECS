# Generated from metaclass-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name metaclass


Summary: Adds a metaclass method to all Ruby objects
Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 5%{?dist}
Group: Development/Languages
# https://github.com/floehopper/metaclass/issues/1
License: MIT
URL: http://github.com/floehopper/metaclass
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Make the test suite support MiniTest 5.x.
# https://github.com/floehopper/metaclass/commit/cff40cbace639d3b66d7913d99e74e56f91905b8
Patch0: rubygem-metaclass-0.0.4-Move-to-Minitest-5.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Adds a metaclass method to all Ruby objects


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# test_helper.rb currently references bundler, so it is easier to avoid
# its usage at all.
sed -i '/require "bundler\/setup"/ d' test/test_helper.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/metaclass.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test


%changelog
* Fri Nov 13 2015 Liu Di <liudidi@gmail.com> - 0.0.4-5
- 为 Magic 3.0 重建

* Wed Nov 04 2015 Liu Di <liudidi@gmail.com> - 0.0.4-4
- 为 Magic 3.0 重建

* Thu Sep 24 2015 Liu Di <liudidi@gmail.com> - 0.0.4-3
- 为 Magic 3.0 重建

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.1-1
- Update to metaclass 0.0.4.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.1-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.1-5
- Build for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.1-3
- Move README.md into -doc subpackage and properly mark.

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.1-2
- Clarified license.

* Mon Oct 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.1-1
- Initial package
