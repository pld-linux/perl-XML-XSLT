%define PackageName XML-XSLT
%{expand: %%define perl_version  %(perl -V:version | sed "s!.*='!!;s!'.*!!")}

Name: perl-%{PackageName}
Version: 0.30
Release: 2cl
Summary: Perl XML::XSLT module
Summary(pt_BR): Modulo Perl XML::XSLT
Summary(es): Modulo Perl XML::XSLT
Group: Libraries
Group(pt_BR): Bibliotecas
Group(es): Bibliotecas
License: GPL
Source: http://www.perl.com/CPAN/modules/by-module/XML/%{PackageName}-%{version}.tar.gz
URL: http://www.perl.com/CPAN/modules/by-module/XML/%{PackageName}-%{version}.readme
AutoProv: no
BuildRequires: perl perl-devel perl-XML-Parser perl-HTML-Parser perl-libxml-enno
PreReq: perl = %{perl_version}
Requires: perl-XML-Parser perl-HTML-Parser perl-libxml-enno 
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%{expand: %%define perl_man1ext  %(perl -V:man1ext | sed "s!.*='!!;s!'.*!!")}
%{expand: %%define perl_man3ext  %(perl -V:man3ext | sed "s!.*='!!;s!'.*!!")}
%{expand: %%define perl_installman1dir %(perl -V:installman1dir | sed "s!.*='!!;s!'.*!!")}
%{expand: %%define perl_installman3dir %(perl -V:installman3dir | sed "s!.*='!!;s!'.*!!")}
%{expand: %%define perl_installarchlib %(perl -V:installarchlib | sed "s!.*='!!;s!'.*!!")}
%{expand: %%define perl_prefix  %(if [ %{perl_version} != 5.00503 ]; then echo %{buildroot};else echo /; fi) }


%description
Perl Interface to XSL Transformational sheets.

%description -l pt_BR
Perl Interface to XSL Transformational sheets.

%description -l es
Perl Interface to XSL Transformational sheets.


%prep
%setup -q -n %{PackageName}-%{version}

%build
#Some modules require POLLUTE=1 in the next line
CFLAGS="%{optflags}" perl Makefile.PL           \
INSTALLMAN1DIR=%{perl_prefix}%{perl_installman1dir}         \
INSTALLMAN3DIR=%{perl_prefix}%{perl_installman3dir}
make OPTIMIZE="%{optflags}"
#make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_installarchlib}
mkdir -p %{buildroot}%{perl_installman1dir}
mkdir -p %{buildroot}%{perl_installman3dir}
mkdir -p %{buildroot}%{_libdir}/perl5/perllocal
make PREFIX=%{buildroot}%{_prefix} install

#Get the file "perllocal.pod" location
find %{buildroot}%{_prefix} -type f -print | grep perllocal.pod > podfile_full.lst

#move it to docs
mv `cat podfile_full.lst` .

#Correct the data inside the file
perl -pi -e 's@%{buildroot}@@g' podfile_full.lst

#Add glob to man pages
find %{buildroot}%{_prefix} -type f -print |\
    perl -pe 's!%{buildroot}!!g; m!man\d/.*\.\d! && s!$!\*!' > file-list.lst

cp perllocal.pod %{buildroot}%{_libdir}/perl5/perllocal/%{name}-perllocal.pod
cp podfile_full.lst %{buildroot}%{_libdir}/perl5/perllocal/%{name}-podfile_full.lst

#get the dirs
find %{buildroot}%{_libdir}/perl5 -type d -print | perl -pe " \
    s!^%{buildroot}!!;					\
    s!^%{_libdir}/perl5\n!!;				\
    s!^%{_libdir}/perl5/%{perl_version}\n!!;		\
    s!^%{installarchlib}\n!!;				\
    s!^%{installarchlib}/auto\n!!;			\
    s!^%{_libdir}/perl5/perllocal\n!!;			\
    s!^%{_libdir}/perl5/site_perl\n!!;			\
    s!^%{_libdir}/perl5/site_perl/%{perl_version}\n!!;	\
    s!^%{_libdir}/perl5/site_perl/%{perl_version}/i386-linux\n!!;	\
    s!^%{_libdir}/perl5/site_perl/%{perl_version}/i386-linux/auto\n!!;	\
    s!^!%dir !;" >> file-list.lst

#Some authors leave docs with the exec bit on 
find . -type f  -exec chmod 0644 {} \; 

#correct a few permitions
find %{buildroot} -type d  -exec chmod 0755 {} \; 
find %{buildroot} -type f  -exec chmod 0644 {} \; 
chmod 0755 %{buildroot}%{_bindir}/*


%clean
rm -rf %{_builddir}/%{PackageName}-%{version}
rm -rf %{buildroot}


%files -f file-list.lst
%defattr(-,root,root, 0755)
%doc README* Change* MANIFEST example*
%{_libdir}/perl5/perllocal/%{name}-perllocal.pod
%{_libdir}/perl5/perllocal/%{name}-podfile_full.lst


%post

#Adjusts the date too
cat %{_libdir}/perl5/perllocal/%{name}-perllocal.pod |\
sed -e "s@\(^=head2 \).*\(:.*\)@\1`date`\2@" >> `cat %{_libdir}/perl5/perllocal/%{name}-podfile_full.lst`


%changelog
* Mon Jan 22 2001 Raul Dias <rsd@conectiva.com>
+ perl-XML-XSLT-0.30-2cl
- first build
