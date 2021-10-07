%define		php_min_version 5.3.2
%define		pkgname	xdebug-handler
Summary:	Restarts a process without xdebug
Name:		php-composer-%{pkgname}
Version:	2.0.2
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/composer/xdebug-handler/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	086af3eec788f6691849498c43a10591
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
