#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : psycopg2
Version  : 2.6.2
Release  : 19
URL      : http://pypi.debian.net/psycopg2/psycopg2-2.6.2.tar.gz
Source0  : http://pypi.debian.net/psycopg2/psycopg2-2.6.2.tar.gz
Summary  : psycopg2 - Python-PostgreSQL Database Adapter
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0 ZPL-2.0
Requires: psycopg2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : postgresql-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
psycopg2 - Python-PostgreSQL Database Adapter
=============================================

%package python
Summary: python components for the psycopg2 package.
Group: Default

%description python
python components for the psycopg2 package.


%prep
%setup -q -n psycopg2-2.6.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484563184
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484563184
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
