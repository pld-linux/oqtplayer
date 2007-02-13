Summary:	Simple player that uses OpenQuicktime library
Summary(pl.UTF-8):	Prosty odtwarzacz korzystający z biblioteki OpenQuicktime
Name:		oqtplayer
Version:	0.5
Release:	1
License:	LGPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/openquicktime/%{name}-%{version}.tgz
# Source0-md5:	692f5a43e3f7a7819f65bd9f92f3d858
URL:		http://openquicktime.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	openquicktime-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OQTPlayer is simple player that uses OpenQuicktime library.

%description -l pl.UTF-8
OQTPlayer jest prostym odtwarzaczem korzystającym z biblioteki
OpenQuicktime.

%prep
%setup -q -n OQTPlayer-%{version}

%build
%{__make} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install oqtplayer $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme
%attr(755,root,root) %{_bindir}/*
