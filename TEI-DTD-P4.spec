%define name TEI-DTD-P4
%define version 1.0
%define release 11
%define dtdver P4

Name: %{name}
Version: %{version}
Release: %{release}
Group       	: Publishing

Summary     	: XML document type definition for TEI

License   	: Artistic like
URL         	: http://www.tei-c.org/

Provides: 	TEI-DTD
Requires(Pre): 	coreutils
Requires(Pre):	sgml-common

# Zip file downloadable at http://www.tei-c.org/P4X/DTD/dtd.zip
Source0		: %{name}.tar.bz2
BuildArch	: noarch  


%define sgmlbase %{_datadir}/sgml

%Description

The TEI (Text Encoding Initiative) Document Type Definition (DTD)
describes the syntax of literature and human sciences related texts.
This syntax is XML-compliant and is developed by the TEI consortium.
This is the version %{dtdver} of this DTD.

%Prep
%setup -n %{name}

%Build

%Install
DESTDIR=$RPM_BUILD_ROOT%{sgmlbase}/TEI/dtd-%{dtdver}
mkdir -p $DESTDIR
install -m644 teicatalog.xml catalog.tei catalog.xml $DESTDIR
install -m644 *.dtd $DESTDIR
install -m644 *.ent $DESTDIR
install -m644 *.dec $DESTDIR

%Files
%defattr (-,root,root)
%doc index.html index.xml
%{sgmlbase}/TEI/dtd-%{dtdver}

# Catalogs management left for brave packagers.
 


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2011.0
+ Revision: 616456
- the mass rebuild of 2010.0 packages

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0-9mdv2010.0
+ Revision: 434331
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2009.0
+ Revision: 261459
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-7mdv2009.0
+ Revision: 254355
- rebuild

* Fri Feb 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2008.1
+ Revision: 164093
- require coreutils instead of fileutils

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0-4mdv2008.1
+ Revision: 136535
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import TEI-DTD-P4


* Wed Mar 22 2006 Camille Begnis <camille@mandriva.com> 1.0-4mdk
- pleases rpmlint

* Mon Sep 06 2004  <camille@ke.mandrakesoft.com> 1.0-3mdk
- rebuild

* Fri Aug 29 2003  <camille@ke.mandrakesoft.com> 1.0-2mdk
- add missing dir

* Mon Jul 21 2003  <camille@ke.mandrakesoft.com> 1.0-1mdk
- First specs for MDK
