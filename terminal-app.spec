%define debug_package %nil
%define debugcflags %nil

Summary:	Terminal app for Papryos
Name:		terminal-app
Version:	0.1.0
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
%cmake_qt5

%build
%ninja -C build

%install
%ninja_install -C build

%files
