Summary:	Voice over IP
Name:		voicechat
%define		alt_version 0.40-beta
Version:	0.40_beta
Release:	1
Group:		Applications/Sound	
######		Unknown group!
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	%{name}-%{alt_version}.tar.gz
Patch0:		%{name}-make.patch
BuildPrereq:	libgsm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voice over IP

%prep
%setup  -q -n %{name}-%{alt_version}
%patch0 -p1

%build
%{__make} CFLAGS="-Wall $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf README 

install -d		$RPM_BUILD_ROOT%{_bindir}
install voicevolume	$RPM_BUILD_ROOT%{_bindir}
install voicechat 	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
