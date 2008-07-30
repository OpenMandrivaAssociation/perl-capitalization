%define realname   capitalization

Name:		perl-%{realname}
Version:    0.03
Release: %mkrel 7
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

