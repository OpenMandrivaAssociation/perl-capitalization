%define realname   capitalization

Name:		perl-%{realname}
Version:    0.03
Release: %mkrel 8
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Perl module that allows no capitalization on method names
Source0:    http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-Devel-Symdump
BuildArch: noarch

%description
capitalization.pm allows you to use familiar style on method naming.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/*
%{_mandir}/man3/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.03-8mdv2010.0
+ Revision: 430267
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-7mdv2009.0
+ Revision: 255476
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.03-5mdv2008.1
+ Revision: 136666
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-5mdv2008.0
+ Revision: 85923
- rebuild

  + Michael Scherer <misc@mandriva.org>
    - rebuild


* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.03-3mdk
- Do not ship empty dir

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- BuildRequires fix

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.03-1mdk
- First mandriva package

