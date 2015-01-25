#
# Conditional build:
%bcond_with	gnu	# GNU libstdc++/libsupc++ ABI instead of LLVM libcxxabi
#
Summary:	LibC++ - C++ standard library from LLVM project
Summary(pl.UTF-8):	LibC++ - biblioteka standardowa C++ z projektu LLVM
Name:		llvm-libcxx
Version:	3.5.1
Release:	1
License:	MIT or BSD-like
Group:		Libraries
Source0:	http://llvm.org/releases/%{version}/libcxx-%{version}.src.tar.xz
# Source0-md5:	406f09b1dab529f3f7879f4d548329d2
URL:		http://dragonegg.llvm.org/
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with gnu}
BuildRequires:	libstdc++-devel
%else
BuildRequires:	llvm-libcxxabi-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libc++ is a new implementation of the C++ standard library, targeting
C++11.

%description -l pl.UTF-8
libc++ to nowa implementacja biblioteki standardowej C++ ze wskazaniem
na standard C++11.

%package devel
Summary:	Header files of LLVM LibC++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LLVM LibC++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with gnu}
Requires:	libstdc++-devel
%else
Requires:	llvm-libcxxabi-devel
%endif

%description devel
Header files of LLVM LibC++ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LLVM LibC++.

%prep
%setup -q -n libcxx-%{version}.src

%build
install -d build
cd build
%cmake .. \
%if %{with gnu}
	-DLIBCXX_CXX_ABI=libstdc++ \
	-DLIBCXX_LIBSUPCXX_INCLUDE_PATHS="%{_includedir}/c++/%{cxx_version};%{_includedir}/c++/%{cxx_version}/%{_host}"
%else
	-DLIBCXX_CXX_ABI=libcxxabi
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT
%attr(755,root,root) %{_libdir}/libc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++.so
%dir %{_includedir}/c++
%{_includedir}/c++/v1
