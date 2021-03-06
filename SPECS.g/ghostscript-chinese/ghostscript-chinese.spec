%define common_desc \
ghostscript font configuration files for Chinese fonts.

%define common_desz_zh \
中文字体的 ghostscript 字体配置文件。

%define gsdir            %{_datadir}/ghostscript/conf.d
%define umingver         0.2.20080216.1
%define ukaiver          0.2.20080216.1
%define zenheiver        0.9.45

Name:           ghostscript-chinese
Version:	0.3.1
Release:        3%{?dist}
Summary:        Ghostscript Chinese fonts configuration files
Summary(zh_CN.UTF-8): Ghostscript 中文字体配置文件 
Group:          User Interface/X
Group(zh_CN.UTF-8): 用户界面/X
License:        GPLv2+
URL:            http://www.freedesktop.org/wiki/Software/CJKUnifonts
Source0:        http://pwu.fedorapeople.org/ghostscript-chinese/ghostscript-chinese-%{version}.tar.gz
BuildArch:      noarch

#BuildRequires:
Provides:     cjkuni-fonts-ghostscript = %{version}
Obsoletes:    cjkuni-fonts-ghostscript < 0.2.20080216.1-45
%description
%common_desc

%description -l zh_CN.UTF-8
%common_desc_zh

%package zh_CN
Summary:      Ghostscript Simplified Chinese fonts configuration files
Summary(zh_CN.UTF-8): Ghostscript 简单中文字体配置文件 
Group:        User Interface/X
Group(zh_CN.UTF-8): 用户界面/X
Requires:     ghostscript
Requires:     wqy-zenhei-fonts >= %{zenheiver}
Requires:     ghostscript-chinese = %{version}-%{release}

%description zh_CN
%common_desc

For Simplified Chinese.

%description zh_CN -l zh_CN.UTF-8
%common_desc_zh

简体中文设置。

%package zh_TW
Summary:      Ghostscript Traditional Chinese fonts configuration files
Summary(zh_CN.UTF-8): Ghostscript 繁体中文字体配置文件
Group:        User Interface/X
Group(zh_CN.UTF-8): 用户界面/X
Requires:     ghostscript
Requires:     cjkuni-uming-fonts = %{umingver}
Requires:     cjkuni-ukai-fonts = %{ukaiver}
Requires:     ghostscript-chinese = %{version}-%{release}

%description zh_TW
%common_desc

For Traditional Chinese.

%description zh_TW -l zh_CN.UTF-8
%common_desc_zh

繁体中文版本。

%prep
%setup -q -c -n %{name}-%{version}


%build
%{nil}


%install
install -m 0755 -d %{buildroot}%{gsdir}

#Note modify the absolute path of zenhei fonts in ghostscript files.
for gscid in `ls *.zh_CN`
do
    cat $gscid | sed --expression='s/###zenheiloc###/\/usr\/share\/fonts\/wqy-zenhei/g' > tmp_gs
    mv tmp_gs $gscid
    install -m 0644 -p $gscid %{buildroot}%{gsdir}
done

#Note modify the absolute path of uming/ukai fonts in ghostscript files.
for gscid in `ls *.zh_TW`
do
    cat $gscid | sed --expression='s/###ukailoc###/\/usr\/share\/fonts\/cjkuni-ukai/g' --expression='s/###umingloc###/\/usr\/share\/fonts\/cjkuni-uming/g' > tmp_gs
    mv tmp_gs $gscid
    install -m 0644 -p $gscid %{buildroot}%{gsdir}
done
magic_rpm_clean.sh

%files
%defattr(-,root,root,-)
%doc COPYING
%doc README

%files zh_CN
%defattr(-,root,root,-)
%{gsdir}/FAPIcidfmap.zh_CN
%{gsdir}/cidfmap.zh_CN
%{gsdir}/CIDFnmap.zh_CN

%files zh_TW
%defattr(-,root,root,-)
%{gsdir}/FAPIcidfmap.zh_TW
%{gsdir}/cidfmap.zh_TW
%{gsdir}/CIDFnmap.zh_TW



%changelog
* Sun Nov 08 2015 Liu Di <liudidi@gmail.com> - 0.3.1-3
- 为 Magic 3.0 重建

* Fri Oct 30 2015 Liu Di <liudidi@gmail.com> - 0.3.1-2
- 更新到 0.3.1

* Sun Apr 06 2014 Liu Di <liudidi@gmail.com> - 0.4.0-1
- 更新到 0.4.0

* Thu Dec 06 2012 Liu Di <liudidi@gmail.com> - 0.3.1-6
- 为 Magic 3.0 重建

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011  Peng Wu <pwu@redhat.com> - 0.3.1-2
- Fixes wqy-zenhei-fonts deps.

* Tue Aug 10 2010  Peng Wu <pwu@redhat.com> - 0.3.1-1
- Renamed from cjkuni-fonts-ghostscript.

* Fri Jul 23 2010  Peng Wu <pwu@redhat.com> - 0.3-1
- Add license file.

* Mon Jul 19 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-44
- Clean up the spec.

* Tue Jul 13 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-43
- The Initial Version.
  Split from cjkuni-fonts.
