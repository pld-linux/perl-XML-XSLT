%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XSLT
Summary:	Perl XML::XSLT module
Summary(es):	Modulo Perl XML::XSLT
Summary(pl):	Modu³ perla XML::XSLT
Summary(pt_BR):	Modulo Perl XML::XSLT
Name:		perl-XML-XSLT
Version:	0.40
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.perl.com/CPAN/modules/by-module/XML/XML-XSLT-%{version}.readme
BuildRequires:	perl-Test-Simple >= 0.33
BuildRequires:	perl-URI
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-libxml-enno
BuildRequires:	perl(XML::DOM) >= 1.25
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Interface to XSL Transformational sheets.

%description -l es
Perl Interface to XSL Transformational sheets.

%description -l pl
Modu³y perla do arkuszy konwersji XSL.

%description -l pt_BR
Perl Interface to XSL Transformational sheets.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Change* MANIFEST example*
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/*
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
