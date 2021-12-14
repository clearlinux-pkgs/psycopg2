#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6013BD3AFCF957DE (daniele.varrazzo@gmail.com)
#
Name     : psycopg2
Version  : 2.9.2
Release  : 80
URL      : https://files.pythonhosted.org/packages/33/ed/79434011d773e5ea4c51262f6ebfb86680c2908d7677f31ebccd5aa9f1b3/psycopg2-2.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/33/ed/79434011d773e5ea4c51262f6ebfb86680c2908d7677f31ebccd5aa9f1b3/psycopg2-2.9.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/33/ed/79434011d773e5ea4c51262f6ebfb86680c2908d7677f31ebccd5aa9f1b3/psycopg2-2.9.2.tar.gz.asc
Summary  : psycopg2 - Python-PostgreSQL Database Adapter
Group    : Development/Tools
License  : LGPL-3.0
Requires: psycopg2-license = %{version}-%{release}
Requires: psycopg2-python = %{version}-%{release}
Requires: psycopg2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : postgresql-dev
BuildRequires : python3-dev

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

%package license
Summary: license components for the psycopg2 package.
Group: Default

%description license
license components for the psycopg2 package.


%package python
Summary: python components for the psycopg2 package.
Group: Default
Requires: psycopg2-python3 = %{version}-%{release}

%description python
python components for the psycopg2 package.


%package python3
Summary: python3 components for the psycopg2 package.
Group: Default
Requires: python3-core
Provides: pypi(psycopg2)

%description python3
python3 components for the psycopg2 package.


%prep
%setup -q -n psycopg2-2.9.2
cd %{_builddir}/psycopg2-2.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636732356
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/psycopg2
cp %{_builddir}/psycopg2-2.9.2/LICENSE %{buildroot}/usr/share/package-licenses/psycopg2/8962684fea8c5eca411c030d957afd571d2069a1
cp %{_builddir}/psycopg2-2.9.2/doc/COPYING.LESSER %{buildroot}/usr/share/package-licenses/psycopg2/e203d4ef09d404fa5c03cf6590e44231665be689
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/psycopg2/8962684fea8c5eca411c030d957afd571d2069a1
/usr/share/package-licenses/psycopg2/e203d4ef09d404fa5c03cf6590e44231665be689

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
