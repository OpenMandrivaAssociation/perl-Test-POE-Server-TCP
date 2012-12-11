%define upstream_name    Test-POE-Server-TCP
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A POE Component providing TCP server services for test cases
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Filter)
BuildRequires:	perl(POE::Filter::Line)
BuildRequires:	perl(POE::Wheel::ReadWrite)
BuildRequires:	perl(POE::Wheel::SocketFactory)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::ParseWords)
BuildArch:	noarch

%description
Test::POE::Server::TCP is a the POE manpage component that provides a TCP
server framework for inclusion in client component test cases, instead of
having to roll your own.

Once registered with the component, a session will receive events related
to client connects, disconnects, input and flushed output. Each of these
events will refer to a unique client ID which may be used in communication
with the component when sending data to the client or disconnecting a
client connection.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Test


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 688832
- update to new version 1.16

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.140.0-1mdv2011.0
+ Revision: 561042
- update to 1.14

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 553976
- update to 1.12

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 526457
- update to 1.10

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 405592
- rebuild using %%perl_convert_version

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2010.0
+ Revision: 396227
- update to new version 1.08

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2010.0
+ Revision: 385255
- update to new version 1.06

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2010.0
+ Revision: 370231
- update to new version 1.04

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.1
+ Revision: 336787
- update to new version 0.18

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 331592
- update to new version 0.16
- update to new version 0.16

* Fri Jan 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 330196
- update to new version 0.14

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2009.0
+ Revision: 270397
- update to new version 0.12

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.10-2mdv2009.0
+ Revision: 268737
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
+ Revision: 214558
- import perl-Test-POE-Server-TCP


* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2009.0
- first mdv release
