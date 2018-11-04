%define		php_min_version 5.3.2
%define		pkgname	xdebug-handler
%include	/usr/lib/rpm/macros.php
Summary:	Restarts a process without xdebug
Name:		php-composer-%{pkgname}
Version:	1.3.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/composer/xdebug-handler/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	c34c243322d141277cc0d86357b89ed2
URL:		https://github.com/composer/xdebug-handler
Requires:	php(core) >= %{php_min_version}
Requires:	php-psr-log >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Restart a CLI process without loading the xdebug extension.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Composer/XdebugHandler
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Composer/XdebugHandler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{php_data_dir}/Composer
%{php_data_dir}/Composer/XdebugHandler
