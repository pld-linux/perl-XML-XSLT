%define	pdir	XML
%define	pnam	XSLT
%include	/usr/lib/rpm/macros.perl
Summary:	Perl XML::XSLT module
Summary(es):	Modulo Perl XML::XSLT
Summary(pl):	Modu³ perla XML::XSLT
Summary(pt_BR):	Modulo Perl XML::XSLT
Name:		perl-XML-XSLT
Version:	0.32
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.perl.com/CPAN/modules/by-module/XML/XML-XSLT-%{version}.readme
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-URI
BuildRequires:	perl-libxml-enno
BuildRequires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl Interface to XSL Transformational sheets.

%description -l es
Perl Interface to XSL Transformational sheets.

%description -l pl
Mody³y perla do arkuszy konwersji XSL.

%description -l pt_BR
Perl Interface to XSL Transformational sheets.

%prep
%setup -q -n XML-XSLT-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README* Change* MANIFEST

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example*
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/*
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
