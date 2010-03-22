%define upstream_name    Test-POE-Server-TCP
%define upstream_version 1.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A POE Component providing TCP server services for test cases
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Filter)
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::ParseWords)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/Test
