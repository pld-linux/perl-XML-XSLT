#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_without	autodeps	# do not BR packages, needed only
				# for resolving deps
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XSLT
Summary:	Perl XML::XSLT module
Summary(es):	Modulo Perl XML::XSLT
Summary(pl):	Modu³ perla XML::XSLT
Summary(pt_BR):	Modulo Perl XML::XSLT
Name:		perl-XML-XSLT
Version:	0.48
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	44d6d9e183d5c49c5d422ae42e7a9f68
URL:		http://www.perl.com/CPAN/modules/by-module/XML/XML-XSLT-%{version}.readme
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.33
%endif
%if %{with tests} || %{with autodeps}
BuildRequires:	perl-libwww
BuildRequires:	perl-URI
BuildRequires:	perl-XML-DOM >= 1.25
BuildRequires:	perl-XML-Parser >= 2.23
%endif
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

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
%{perl_vendorlib}/XML/*
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
