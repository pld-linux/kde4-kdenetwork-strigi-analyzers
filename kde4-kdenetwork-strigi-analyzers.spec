%define		_state		stable
%define		orgname		kdenetwork-strigi-analyzers
%define		qtver		4.8.0

Summary:	K Desktop Environment - Strigi analyzers for various network types
Name:		kde4-kdenetwork-strigi-analyzers
Version:	4.12.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	3ae5476b1769de7b31b5ec29e0faabf5
URL:		http://www.kde.org/
BuildRequires:	boost-devel
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	strigi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Strigi analyzers for various network types.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/strigi/strigita_torrent_analyzer.so
