%global with_python3 1
%global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")

# we have a circular (build) dependency with the (new) pytest package
# when generating the docs or running the testsuite
%global with_docs 1
%global run_check 1

%global pytest_version 2.3.1

Name:           python-py
Version:	1.4.30
Release:	3%{?dist}
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
Summary(zh_CN.UTF-8): 交叉 python 路径，INI 解析，代码，日志等的库
Group:          Development/Languages
Group(zh_CN.UTF-8): 开发/语言
License:        MIT and Public Domain
#               main package: MIT, except: doc/style.css: Public Domain
URL:            http://pylib.readthedocs.org/
Source:         http://pypi.python.org/packages/source/p/py/py-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python-setuptools
%if 0%{?with_docs}
%if 0%{?rhel} > 6 || 0%{?fedora}
BuildRequires:  python-sphinx
%else
BuildRequires:  python-sphinx10
%endif # fedora
%endif # with_docs
%if 0%{?run_check}
BuildRequires:  pytest >= %{pytest_version}
%endif # run_check
%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?run_check}
BuildRequires:  python3-pytest >= %{pytest_version}
%endif # run_check
%endif # with_python3

# needed by the testsuite
BuildRequires:  subversion


%description
The py lib is a Python development support library featuring the
following tools and modules:

  * py.path: uniform local and svn path objects
  * py.apipkg: explicit API control and lazy-importing
  * py.iniconfig: easy parsing of .ini files
  * py.code: dynamic code generation and introspection
  * py.path: uniform local and svn path objects

%description -l zh_CN.UTF-8
交叉 python 路径，INI 解析，代码，日志等的库.

%if 0%{?with_python3}
%package -n python3-py
Summary:        Library with cross-python path, ini-parsing, io, code, log facilities
Summary(zh_CN.UTF-8): 交叉 python 路径，INI 解析，代码，日志等的库
Requires:       python3-setuptools

%description -n python3-py
The py lib is a Python development support library featuring the
following tools and modules:

  * py.path: uniform local and svn path objects
  * py.apipkg: explicit API control and lazy-importing
  * py.iniconfig: easy parsing of .ini files
  * py.code: dynamic code generation and introspection
  * py.path: uniform local and svn path objects

%description -n python3-py -l zh_CN.UTF-8
交叉 python 路径，INI 解析，代码，日志等的库
%endif # with_python3

%prep
%setup -q -n py-%{version}

# remove shebangs and fix permissions
find -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;

%if 0%{?with_python3}
cp -a . %{py3dir}
%endif # with_python3


%build
%{__python} setup.py build

%if 0%{?with_docs}
%if 0%{?rhel} > 6 || 0%{?fedora}
make -C doc html PYTHONPATH=$(pwd)
%else
make -C doc html SPHINXBUILD=sphinx-1.0-build PYTHONPATH=$(pwd)
%endif # fedora
%endif # with_docs

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif # with_python3

# remove hidden file
rm -rf doc/_build/html/.buildinfo
magic_rpm_clean.sh

%check
# disable failing Subversion checks for now
%if 0%{?run_check}
PYTHONPATH=%{buildroot}%{python_sitelib} \
LC_ALL="en_US.UTF-8" \
py.test -r s -k"-TestWCSvnCommandPath" testing
%if 0%{?with_python3}
pushd %{py3dir}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
LC_ALL="en_US.UTF-8" \
py.test-%{python3_version} -r s -k"-TestWCSvnCommandPath" testing
popd
%endif # with_python3
%endif # run_check

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README.txt
%if 0%{?with_docs}
%doc doc/_build/html
%endif # with_docs
%{python_sitelib}/*


%if 0%{?with_python3}
%files -n python3-py
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE README.txt
%if 0%{?with_docs}
%doc doc/_build/html
%endif # with_docs
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Thu Nov 12 2015 Liu Di <liudidi@gmail.com> - 1.4.30-3
- 为 Magic 3.0 重建

* Mon Nov 02 2015 Liu Di <liudidi@gmail.com> - 1.4.30-2
- 为 Magic 3.0 重建

* Tue Sep 08 2015 Liu Di <liudidi@gmail.com> - 1.4.30-1
- 更新到 1.4.30

* Tue Jun 17 2014 Liu Di <liudidi@gmail.com> - 1.4.18-2
- 为 Magic 3.0 重建

* Sun Nov 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.18-1
- Update to 1.4.18.

* Mon Oct  7 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.17-2
- Only run tests from the 'testing' subdir in %%check.

* Fri Oct  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.17-1
- Update to 1.4.17.

* Thu Oct  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.16-1
- Update to 1.4.16.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.15-1
- Update to 1.4.15.
- Disable failing Subversion checks for now.

* Wed Jun 12 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.14-2
- Use python-sphinx for rhel > 6 (rhbz#973321).
- Update URL.
- Fix changelog entry with an incorrect date (rhbz#973325).

* Sat May 11 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.14-1
- Update to 1.4.14.

* Sat Mar  2 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.13-1
- Update to 1.4.13.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.12-1
- Update to 1.4.12.

* Sat Oct 27 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.11-1
- Update to 1.4.11.

* Sun Oct 21 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.10-2
- Re-enable doc building and testsuite.
- Minor testsuite fixes.

* Sun Oct 21 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.10-1
- Update to 1.4.10.

* Fri Oct 12 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.9-8
- Re-enable doc building and testsuite.

* Thu Oct 11 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.9-7
- Add conditional for sphinx on rhel.
- Remove rhel logic from with_python3 conditional.

* Wed Oct 10 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.9-6
- Re-enable doc building and testsuite.

* Sat Aug  4 2012 David Malcolm <dmalcolm@redhat.com> - 1.4.9-5
- Temporarily disable docs and testsuite.

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.4.9-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.9-2
- Re-enable doc building and testsuite.

* Thu Jun 14 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.9-1
- Update to 1.4.9.

* Sat Jun  9 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.8-2
- Re-enable doc building and testsuite.

* Wed Jun  6 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.8-1
- Update to 1.4.8.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.7-2
- Re-enable doc building and testsuite.

* Wed Feb  8 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.7-1
- Update to 1.4.7.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.6-2
- Re-enable doc building and testsuite.

* Sat Dec 17 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.6-1
- Update to 1.4.6.
- Remove %%prerelease macro.
- Temporarily disable docs and testsuite.

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-4
- Rebuilt for glibc bug#747377

* Sat Sep  3 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.5-3
- Fix: python3 dependencies.

* Tue Aug 30 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.5-2
- Re-enable doc building and testsuite.

* Sat Aug 27 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.5-1
- Update to 1.4.5.

* Thu Aug 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.4-2
- Re-enable doc building and testsuite.

* Thu Aug 11 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.4-1
- Update to 1.4.4.
- Upstream provides a .zip archive only.
- pytest and pycmd are separate packages now. 
- Disable building html docs und the testsuite to break the circular
  build dependency with pytest.
- Update summary and description.
- Remove BRs no longer needed.
- Create a Python 3 subpackage.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 18 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.4-1
- Update to 1.3.4

* Fri Aug 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.3-2
- Add dependency on python-setuptools (see bz 626808).

* Sat Jul 31 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.3-1
- Update to 1.3.3.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 10 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.2-1
- Update to 1.3.2.
- Do cleanups already in %%prep to avoid inconsistent mtimes between
  source files and bytecode.

* Sat May 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- Update to 1.3.1.

* Sat May  8 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.0-1
- Update to 1.3.0.
- Remove some backup (.orig) files.

* Sun Feb 14 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.1-1
- Update to 1.2.1.

* Wed Jan 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.0-1
- Update to 1.2.0.
- Adjust summary and %%description.
- Use %%global instead of %%define.

* Sat Nov 28 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.1-1
- Update to 1.1.1.

* Sat Nov 21 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.0-1
- Update to 1.1.0. Upstream reorganized the package's structure and
  cleaned up the install process, so the specfile could be greatly
  simplified.
- Dropped licenses for files no longer present from the License tag.

* Thu Aug 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.2-1
- Update to 1.0.2.
- One failing test is no longer part of the testsuite, thus needs not
  to be skipped anymore.
- Some developer docs are missing this time in upstream's tarfile, so
  cannot be moved to %%{_docdir}

* Thu Aug 13 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.0-1
- Update to 1.0.0.
- Re-enable SVN tests in %%check.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-1.b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.0-0.b8
- Update to 1.0.0b8.
- Remove patches applied upstream.
- Greenlets have been removed upstream. So, package is noarch and
  - installs to %%{python_sitelib} again
  - %%ifarch sections have been removed.
- Don't remove files used by the testsuite for now.
- Add dependency on python-pygments, pylint and pexpect (for the
  testsuite).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 14 2009 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-6
- Use system doctest module again, as this wasn't the real cause of
  the test failure. Instead, remove the failing test for now.

* Fri Dec 12 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-5
- Add patch from trunk fixing a subversion 1.5 problem (pylib
  issue66).
- Don't replace doctest compat module (pylib issue67).

* Fri Nov 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-4
- Use dummy_greenlet on ppc and ppc64.

* Tue Oct  7 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-3
- Replace compat modules by stubs using the system modules instead.
- Add patch from trunk fixing a timing issue in the tests.

* Tue Sep 30 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-2
- Update license information.
- Fix the tests.

* Sun Sep  7 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.2-1
- Update to 0.9.2.
- Upstream now uses setuptools and installs to %%{python_sitearch}.
- Remove %%{srcname} macro.
- More detailed information about licenses.

* Thu Aug 21 2008 Thomas Moschny <thomas.moschny@gmx.de> - 0.9.1-1
- New package.
