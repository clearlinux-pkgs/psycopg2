#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : psycopg2
Version  : 2.7.3.2
Release  : 35
URL      : http://pypi.debian.net/psycopg2/psycopg2-2.7.3.2.tar.gz
Source0  : http://pypi.debian.net/psycopg2/psycopg2-2.7.3.2.tar.gz
Source99 : http://pypi.debian.net/psycopg2/psycopg2-2.7.3.2.tar.gz.asc
Summary  : psycopg2 - Python-PostgreSQL Database Adapter
Group    : Development/Tools
License  : LGPL-3.0 ZPL-2.0
Requires: psycopg2-python3
Requires: psycopg2-python
Requires: Pygments
Requires: Sphinx
BuildRequires : pbr
BuildRequires : pip
BuildRequires : postgresql-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
programming language.  Its main features are the complete implementation of
        the Python DB API 2.0 specification and the thread safety (several threads can
        share the same connection).  It was designed for heavily multi-threaded
        applications that create and destroy lots of cursors and make a large number
        of concurrent "INSERT"s or "UPDATE"s.
        
        Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being
        both efficient and secure.  It features client-side and server-side cursors,
        asynchronous communication and notifications, "COPY TO/COPY FROM" support.
        Many Python types are supported out-of-the-box and adapted to matching
        PostgreSQL data types; adaptation can be extended and customized thanks to a
        flexible objects adaptation system.
        
        Psycopg 2 is both Unicode and Python 3 friendly.
        
        
        Documentation
        -------------
        
        Documentation is included in the ``doc`` directory and is `available online`__.

%package legacypython
Summary: legacypython components for the psycopg2 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the psycopg2 package.


%package python
Summary: python components for the psycopg2 package.
Group: Default
Requires: psycopg2-python3

%description python
python components for the psycopg2 package.


%package python3
Summary: python3 components for the psycopg2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the psycopg2 package.


%prep
%setup -q -n psycopg2-2.7.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528574074
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1528574074
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
