Summary: 	Duzzle Duddle.
Name:		dudusdl
Version:	0.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://cesnet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://dudusdl.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
DuduSDL is a clone of the well-known arcade game Puzzle Bubble,
playable in single-player and two-player modes.
 
%prep
%setup -q

%build
aclocal
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Utilitiesdir=%{_applnkdir}/Games/Arcade

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc AUTHORS COPYING ChangeLog README README.FR

%{_datadir}/%{name}
%{_pixmapsdir}/dudu.png
%{_applnkdir}/Games/Arcade/*.desktop
