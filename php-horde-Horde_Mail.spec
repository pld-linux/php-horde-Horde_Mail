%define		status		stable
%define		pearname	Horde_Mail
Summary:	%{pearname} - Horde Mail Library
Name:		php-horde-Horde_Mail
Version:	1.2.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	8450426ec314640441a3ec6fdfd297dc
URL:		https://github.com/horde/horde/tree/master/framework/Mail/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-pear-Net_DNS2
Suggests:	php-pear-Net_SMTP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Net/DNS2.*) pear(Net/SMTP.*)

%description
The Horde_Mail library is a fork of the PEAR Mail library that
provides additional functionality, including (but not limited to):
- Allows a stream to be passed in.
- Allows raw headertext to be used in the outgoing messages (required
  for things like message redirection pursuant to RFC 5322 [3.6.6]).
- Native PHP 5 code.
- PHPUnit test suite.
- Provides more comprehensive sendmail error messages.
- Uses Exceptions instead of PEAR_Errors.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Mail.php
%{php_pear_dir}/Horde/Mail
