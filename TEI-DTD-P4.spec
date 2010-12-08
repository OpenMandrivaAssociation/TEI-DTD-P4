%define name TEI-DTD-P4
%define version 1.0
%define release %mkrel 10
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
Requires(Pre):	sgml-common >= 0.6.3-2mdk

BuildRoot   	: %{_tmppath}/%{name}-buildroot

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
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT%{sgmlbase}/TEI/dtd-%{dtdver}
mkdir -p $DESTDIR
install -m644 teicatalog.xml catalog.tei catalog.xml $DESTDIR
install -m644 *.dtd $DESTDIR
install -m644 *.ent $DESTDIR
install -m644 *.dec $DESTDIR

%clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr (-,root,root)
%doc index.html index.xml
%dir %{sgmlbase}/TEI/dtd-%{dtdver}
%{sgmlbase}/TEI

# Catalogs management left for brave packagers.
 
