#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xclip
Version  : 0.13
Release  : 8
URL      : https://github.com/astrand/xclip/archive/0.13.tar.gz
Source0  : https://github.com/astrand/xclip/archive/0.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: xclip-bin
Requires: xclip-doc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xmu)

%description
xclip is a command line utility that is designed to run on any system with an
X11 implementation. It provides an interface to X selections ("the clipboard")
from the command line. It can read data from standard in or a file and place it
in an X selection for pasting into other X applications. xclip can also print
an X selection to standard out, which can then be redirected to a file or
another program.

%package bin
Summary: bin components for the xclip package.
Group: Binaries

%description bin
bin components for the xclip package.


%package doc
Summary: doc components for the xclip package.
Group: Documentation

%description doc
doc components for the xclip package.


%prep
%setup -q -n xclip-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506369138
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1506369138
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xclip
/usr/bin/xclip-copyfile
/usr/bin/xclip-cutfile
/usr/bin/xclip-pastefile

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
