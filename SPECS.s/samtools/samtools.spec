Name:		samtools
Version:	0.1.19
Release:	3%{?dist}
Summary:	Tools for nucleotide sequence alignments in the SAM format
Summary(zh_CN.UTF-8): 以 SAM 格式进行核苷酸序列比对的工具 

Group:		Applications/Engineering
Group(zh_CN.UTF-8): 应用程序/工程
License:	MIT
URL:		http://samtools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		samtools-0.1.14-soname.patch
Patch1:		samtools-0.1.19-faidx_fetch_seq2.patch
# The Rsamtools upstream is fixing issues in the samtools 0.1.19 codebase
Patch2:		samtools-0.1.19-R-fixes.patch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	zlib-devel >= 1.2.3
BuildRequires:	ncurses-devel

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment.
SAM Tools provide various utilities for manipulating alignments in the
SAM format, including sorting, merging, indexing and generating
alignments in a per-position format.

%description -l zh_CN.UTF-8
以 SAM 格式进行核苷酸序列比对的工具。

%package devel
Summary:	Header files and libraries for compiling against %{name}
Summary(zh_CN.UTF-8): %{name} 的开发包
Group:		Development/Libraries
Group(zh_CN.UTF-8): 开发/库
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files and libraries for compiling against %{name}

%description devel -l zh_CN.UTF-8
%{name} 的开发包。

%package libs
Summary:	Libraries for applications using %{name}
Summary(zh_CN.UTF-8): %{name} 的运行库
Group:		System Environment/Libraries
Group(zh_CN.UTF-8): 系统环境/库

%description libs
Libraries for applications using %name

%description libs -l zh_CN.UTF-8
%{name} 的运行库。

%prep
%setup -q
%patch0 -p1 -b .soname
%patch1 -p1 -b .seq2
%patch2 -p1 -b .Rfixes

# fix wrong interpreter
perl -pi -e "s[/software/bin/python][%{__python}]" misc/varfilter.py

# fix eol encoding
sed -i 's/\r//' misc/export2sam.pl


%build
make CFLAGS="%{optflags}" dylib %{?_smp_mflags}
make CFLAGS="%{optflags} -fPIC" samtools razip %{?_smp_mflags}

cd misc/
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

cd ../bcftools
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p samtools razip %{buildroot}%{_bindir}

# header and library files
mkdir -p %{buildroot}%{_includedir}/%{name}
install -p -m 644 *.h %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_libdir}
strip libbam.so.1
install -p -m 755 libbam.so.1 %{buildroot}%{_libdir}
ln -sf libbam.so.1 %{buildroot}%{_libdir}/libbam.so

mkdir -p %{buildroot}%{_mandir}/man1/
cp -p samtools.1 %{buildroot}%{_mandir}/man1/
#cp -p bcftools/bcftools.1 %{buildroot}%{_mandir}/man1/

cd misc/
install -p blast2sam.pl bowtie2sam.pl export2sam.pl interpolate_sam.pl	\
    maq2sam-long maq2sam-short md5fa md5sum-lite novo2sam.pl psl2sam.pl	\
    sam2vcf.pl samtools.pl soap2sam.pl varfilter.py wgsim wgsim_eval.pl	\
    zoom2sam.pl 	   	       		    			\
    %{buildroot}%{_bindir}

cd ../bcftools/
install -p bcftools vcfutils.pl %{buildroot}%{_bindir}
mv README README.bcftools
magic_rpm_clean.sh

%clean
rm -rf %{buildroot}


%post libs -p /sbin/ldconfig


%postun libs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog.old COPYING INSTALL NEWS examples/ bcftools/README.bcftools bcftools/bcf.tex
%{_bindir}/*
%{_mandir}/man1/*


%files	devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/libbam.so


%files libs
%defattr(-,root,root,-)
%{_libdir}/libbam.so.*


%changelog
* Wed Nov 04 2015 Liu Di <liudidi@gmail.com> - 0.1.19-3
- 为 Magic 3.0 重建

* Fri Sep 25 2015 Liu Di <liudidi@gmail.com> - 0.1.19-2
- 为 Magic 3.0 重建

* Fri Sep 25 2015 Liu Di <liudidi@gmail.com> - 0.1.19-1
- 更新到 0.1.19

* Sat Sep 19 2015 Liu Di <liudidi@gmail.com> - 0.1.18-5
- 为 Magic 3.0 重建

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Adam Huffman <verdurin@fedoraproject.org> - 0.1.18-2
- make sure new seqtk tool included

* Tue Sep  6 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.18-1
- Updated to 0.1.18

* Tue May 10 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.16-1
- Updated to 0.1.16

* Mon Apr 11 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.15-1
- Updated to 0.1.15

* Wed Mar 23 2011 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.14-1
- Updated to 0.1.14
- Build shared library instead of static

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.12a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-2
- Fixed header files directory ownership
- Added missing header files

* Mon Dec  6 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.12a-1
- Updated to 0.1.12a

* Tue Nov 23 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- cleanup man page handling

* Sun Oct 10 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-4
- fix attributes for devel subpackage
- fix library location

* Sun Sep 26 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-3
- put headers and library in standard locations

* Mon Sep 6 2010 Adam Huffman <bloch@verdurin.com> - 0.1.8-2
- merge Rasmus' latest changes (0.1.8 update)
- include bam.h and libbam.a for Bio-SamTools compilation
- move bam.h and libbam.a to single directory
- put bgzf.h, khash.h and faidx.h in the same place
- add -fPIC to CFLAGS to make Bio-SamTools happy
- add virtual Provide as per guidelines

* Tue Aug 17 2010 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.8-1
- Updated to 0.1.8.

* Mon Nov 30 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.7a-1
- Updated to 0.1.7a.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 12 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-3
- Specfile cleanup.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-2
- Fixed manpage location.
- Make sure optflags is passed to the makefiles.

* Sat Jul 11 2009 Rasmus Ory Nielsen <ron@ron.dk> - 0.1.5c-1
- Initial build.
