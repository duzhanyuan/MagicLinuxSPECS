%global gem_name hoe

Summary:    	Hoe is a simple rake/rubygems helper for project Rakefiles
Name:       	rubygem-%{gem_name}
Version:    	3.14.0
Release:    	2%{?dist}
Group:      	Development/Languages
License:    	MIT
URL:        	http://rubyforge.org/projects/seattlerb/
Source0:    	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Rescue Hoe.spec task when Manifest.txt
# seattlerb-Bugs-28571
Patch0:		rubygem-hoe-3.0.6-rescue-missing-Manifest.patch

Requires:	ruby(release)
BuildRequires:	ruby(release)

Requires:   	rubygems >= 1.3.6
Requires:   	rubygem(rake)      >= 0.8.7
#Requires:       rubygem(minitest)  >= 1.7.0
BuildRequires:  rubygems-devel >= 1.3.6
# %%check
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(rake)
#BuildRequires:	rubygem(rubyforge)
BuildArch:  	noarch
Provides:   	rubygem(%{gem_name}) = %{version}

%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps generate
rubygems and includes a dynamic plug-in system allowing for easy
extensibility. Hoe ships with plug-ins for all your usual project
tasks including rdoc generation, testing, packaging, and deployment.
Plug-ins Provided:
* Hoe::Clean
* Hoe::Debug
* Hoe::Deps
* Hoe::Flay
* Hoe::Flog
* Hoe::Inline
* Hoe::Package
* Hoe::Publish
* Hoe::RCov
* Hoe::Signing
* Hoe::Test
See class rdoc for help. Hint: ri Hoe

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# Patches
%patch0 -p0

# Allow rake 0.9
sed -i \
	-e '/rake/s|~> 0\.8|>= 0.8.7|' \
	-e '/rake/s|< 11\.0|< 12\.0|' \
	lib/hoe.rb \
	Rakefile

# Allow RubyInline 3.8.4
sed -i -e '/RubyInline/s|~> 3\.9|>= 3.8.4|' \
	lib/hoe/inline.rb

# Allow rake-compiler 0.8.0 and above
sed -i -e '/rake-compiler/s|~> 0\.7|>= 0.7|' \
	lib/hoe/compiler.rb

# For old minitest
%if 0%{?fedora} < 21
sed -i -e 's|Mini[tT]est::Test|MiniTest::Unit::TestCase|' \
	test/test_hoe*.rb
%endif

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

pushd .%{gem_instdir}

# Umm...
%_fixperms .

popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{_prefix}/* \
	%{buildroot}%{_prefix}/

chmod 0644 %{buildroot}%{gem_dir}/cache/*gem

find %{buildroot}/%{gem_instdir}/bin -type f | xargs chmod 0755
find %{buildroot}/%{_bindir} -type f | xargs chmod 0755

chmod 0755 %{buildroot}/%{gem_instdir}/template/bin/file_name.erb
# Don't remove template files
#rm -f %{buildroot}/%{gem_instdir}/template/.autotest.erb

%check
pushd .%{gem_instdir}

# ???
sed -i -e '/maglev\?/d' test/test_hoe_debug.rb

# Save original Rakefile
sed -i.isolate -e \
	'/Hoe\.plugin :isolate/d' Rakefile
# Make sure that hoe currently building are loaded
export RUBYLIB=$(pwd)/lib

rake test -v --trace

mv Rakefile{.isolate,}
popd

%files
%defattr(-, root, root, -)
%{_bindir}/sow
%dir %{gem_instdir}/
%{gem_instdir}/bin/
%{gem_instdir}/lib/
%{gem_instdir}/template/
%if 0%{?fedora} <= 20
%{gem_cache}
%else
%exclude	%{gem_cache}
%endif
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_spec}
%doc %{gem_instdir}/[A-Z]*

%files	doc
%defattr(-,root,root,-)
%if 0%{?fedora} <= 20
%{gem_instdir}/.autotest
%{gem_instdir}/.gemtest
%{gem_instdir}/test/
%else
%exclude	%{gem_instdir}/.autotest
%exclude	%{gem_instdir}/.gemtest
%exclude	%{gem_instdir}/test/
%endif
%{gem_docdir}

%changelog
* Thu Sep 24 2015 Liu Di <liudidi@gmail.com> - 3.14.0-2
- 为 Magic 3.0 重建

* Sun Sep 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.14.0-1
- 3.14.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.13.1-1
- 3.13.1

* Fri Oct  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.13.0-1
- 3.13.0

* Fri Jun  6 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.12.0-1
- 3.12.0

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.11.0-1
- 3.11.0

* Mon Mar 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.0-1
- 3.10.0

* Sat Feb 15 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.0-1
- 3.9.0

* Wed Jan 29 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.8.1-1
- 3.8.1

* Tue Dec 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.3-1
- 3.7.3

* Thu Dec 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.2-1
- 3.7.2

* Fri Aug 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.1-1
- 3.7.1

* Thu Aug 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.7.0-1
- 3.7.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.6.0-1
- 3.6.0

* Thu Apr 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.3-2
- 3.5.3

* Wed Apr  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.2-1
- 3.5.2

* Thu Mar  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-2
- F-19: Rebuild for ruby 2.0.0

* Mon Mar  4 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-1
- 3.5.1

* Fri Jan 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.0-1
- 3.5.0

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Tue Jan  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- A Happy New Year
- 3.3.0

* Thu Oct 11 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Wed Sep 12 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Tue Aug 14 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 31 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.0.6-1
- 3.0.6

* Tue Jan 24 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.5-5
- Require rubyforge again

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.5-4
- Rebuild against ruby 1.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.5-1
- 2.12.5

* Sun Dec  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.4-1
- 2.12.4

* Fri Sep  9 2011 Mamoru Tasaka <mtasaka@fedroaproject.org> - 2.12.3-1
- 2.12.3

* Sun Aug 28 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.2-1
- 2.12.2

* Thu Aug 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.0-2
- Fix glob order issue under test/

* Thu Aug 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.12.0-1
- 2.12.0

* Sun Jul  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.10.0-1
- 2.10.0

* Sun Jun 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.9.6-1
- 2.9.6

* Sun Apr  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.9.4-1
- 2.9.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.1-1
- 2.9.1

* Wed Feb  2 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.9.0-1
- 2.9.0

* Fri Dec 10 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.8.0-1
- 2.8.0

* Sat Nov 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.7.0-2
- 2.7.0

* Fri Sep 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-3
- Rescue Hoe.spec task when Manifest.txt is missing

* Sat Sep  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-2
- Kill unneeded patch

* Fri Sep  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.2-1
- 2.6.2
- Drop development dependency
- Split documentation files

* Sat Jun  5 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.1-1
- 2.6.1

* Thu Jun  3 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-3
- Use upstreamed patch for rubyforge-without-account.patch
- Fix test failure related to glob
  (build failed with Matt's mass build, also failed on koji)

* Wed Apr 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.6.0-1
- 2.6.0
- gemcutter dependency dropped

* Thu Mar  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.0-3
- Enable test
- Some cleanups

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> 2.5.0-2
- Updated the dependency on rubygem-rubyforge to >= 2.0.3.

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> 2.5.0-1
- Added dependency on rubygem-gemcutter >= 0.2.1.
- Added dependency on rubygem-minitest >= 1.4.2.
- Release 2.5.0 of Hoe.

* Sat Aug  8 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.3-1
- Release 2.3.3 of Hoe.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul  1 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.2-1
- Release 2.3.2 of Hoe.

* Fri Jun 26 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.3.1-1
- Release 2.3.1 of Hoe.

* Thu Jun 18 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.2.0-1
- Release 2.2.0 of Hoe.

* Mon Jun 15 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.1.0-1
- Release 2.1.0 of Hoe.

* Wed Jun  3 2009 Darryl L. Pierce <dpierce@redhat.com> - 2.0.0-1
- Release 2.0.0 of Hoe.

* Fri Apr 17 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.12.2-1
- Release 1.12.2 of Hoe.

* Wed Apr  1 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.12.1-1
- Release 1.12.1 of Hoe.

* Tue Mar 17 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.11.0-1
- Release 1.11.0 of Hoe.

* Tue Mar 10 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.10.0-1
- Release 1.10.0 of Hoe.

* Fri Feb 27 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.9.0-1
- Release 1.9.0 of Hoe.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.8.3-1
- Release 1.8.3 of Hoe.

* Mon Oct 27 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.2-1
- Release 1.8.2 of Hoe.

* Thu Oct 23 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.1-2
- Last build failed.

* Thu Oct 23 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.1-1
- Release 1.8.1 of the gem.

* Mon Oct 13 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.8.0-1
- Release 1.8.0 of the gem.

* Tue Jul 01 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.7.0-1
- Release 1.7.0 of the gem.

* Wed Jun 18 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.6.0-1
- Release 1.6.0 of the gem.

* Mon Jun 09 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.3-2
- Fixed the dependency for the newer version of rubygem-rubyforge.

* Tue Jun 03 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.3-1
- New release of Hoe.

* Wed May 14 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-6
- Fixed the build, which failed only on devel.

* Wed May 14 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-5
- First official build.

* Mon May 12 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-4
- Update for Fedora 8 and 9.

* Tue Apr 29 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-3
- Fixed the license to read MIT.

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-2
- Updated the spec to comply with Ruby packaging guidelines.

* Fri Apr 18 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.5.1-1
- Initial package
