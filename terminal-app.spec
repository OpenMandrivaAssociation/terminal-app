%define debug_package %nil
%define debugcflags %nil

Summary:	Terminal app for Papryos
Name:		terminal-app
Version:	0.1.1
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/terminal-app
# git clone https://github.com/papyros/terminal-app.git
# git archive --format=tar --prefix terminal-app-0.1.0-$(date +%Y%m%d)/ HEAD | xz -vf > terminal-app-0.1.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Papyros)

%description
The system settings app for Papyros.

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/papyros-terminal
%{_datadir}/applications/io.papyros.Terminal.desktop
%{_datadir}/appdata/io.papyros.Terminal.appdata.xml

