%define realname   capitalization
%define upstream_version 0.03

Name:		perl-%{realname}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl module that allows no capitalization on method names

Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/%{realname}-%{upstream_version}.tar.bz2
Url:		https://search.cpan.org/dist/%{realname}
BuildRequires:	perl-devel
BuildRequires:	perl-Devel-Symdump
BuildArch:	noarch

%description
capitalization.pm allows you to use familiar style on method naming.

%prep
%setup -q -n %{realname}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}

%clean

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*



