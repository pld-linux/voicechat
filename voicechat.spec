Summary:	Voice chat over IP
Summary(pl):	Rozmowa przez Internet
Name:		voicechat
%define		alt_version 0.40-beta
Version:	0.40_beta
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://sunsite.unc.edu/pub/Linux/apps/sound/talk/%{name}-%{alt_version}.tar.gz
Patch0:		%{name}-make.patch
BuildRequires:	libgsm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Two-person bidirectional voice (and text) chat via a small-bandwidth
TCP/IP network.

%description -l pl
Aplikacja do prowadzenia dwuosobowych, obukierunkowych rozm�w
(i przesy�ania tekstu) przez sie� TCP/IP ma�ej przepustowo�ci.

%prep
%setup  -q -n %{name}-%{alt_version}
%patch0 -p1

%build
%{__make} CFLAGS="-Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d		$RPM_BUILD_ROOT%{_bindir}
install voicevolume	$RPM_BUILD_ROOT%{_bindir}
install voicechat 	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
