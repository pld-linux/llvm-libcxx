#
# Conditional build:
%bcond_with	gnu	# GNU libstdc++/libsupc++ ABI instead of LLVM libcxxabi
#
Summary:	LibC++ - C++ standard library from LLVM project
Summary(pl.UTF-8):	LibC++ - biblioteka standardowa C++ z projektu LLVM
Name:		llvm-libcxx
Version:	15.0.7
Release:	1
License:	MIT or BSD-like
Group:		Libraries
#Source0Download: https://github.com/llvm/llvm-project/releases/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxx-%{version}.src.tar.xz
# Source0-md5:	c2c0724be18c153ab902a5a880796af8
#Source1Download: https://github.com/llvm/llvm-project/releases/
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxxabi-%{version}.src.tar.xz
# Source1-md5:	c1f77222397506239dd79d8109a9113d
#Source2Download: https://github.com/llvm/llvm-project/releases/
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/llvm-%{version}.src.tar.xz
# Source2-md5:	c77db4c71e1eb267358204dffe2c6e10
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/cmake-%{version}.src.tar.xz
# Source3-md5:	5be9535f0b93cb6232d0171a8abb3137
URL:		https://libcxx.llvm.org/
# or gcc 10+
BuildRequires:	clang >= %{version}
BuildRequires:	cmake >= 3.13.4
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with gnu}
BuildRequires:	libstdc++-devel >= 6:10
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

%package static
Summary:	Static LLVM LibC++ library
Summary(pl.UTF-8):	Statyczna biblioteka LLVM LibC++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LLVM LibC++ library.

%description static -l pl.UTF-8
Statyczna biblioteka LLVM LibC++.

%prep
%setup -q -c -a1 -a2 -a3

%{__mv} libcxx-%{version}.src libcxx
%{__mv} libcxxabi-%{version}.src libcxxabi
%{__mv} llvm-%{version}.src llvm
%{__mv} cmake-%{version}.src cmake

%build
%if %{without gnu}
# requires C++20 compiler (clang ? or gcc 10+)
CC="clang"
CXX="clang++"
%endif
libsubdir=%{_lib}
%cmake -B build -S libcxx \
	-DLIBCXX_ENABLE_EXPERIMENTAL_LIBRARY=ON \
	-DLIBCXX_INCLUDE_BENCHMARKS=OFF \
	-DLIBCXX_LIBDIR_SUFFIX="${libsubdir#lib}" \
%if %{with gnu}
	-DLIBCXX_CXX_ABI=libstdc++ \
	-DLIBCXX_CXX_ABI_INCLUDE_PATHS="%{_includedir}/c++/%{cxx_version};%{_includedir}/c++/%{cxx_version}/%{_host}"
%else
	-DLIBCXX_CXX_ABI=system-libcxxabi \
	-DLIBCXX_CXX_ABI_INCLUDE_PATHS="%{_includedir}/libcxxabi"
%endif

%{__make} -C build

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
%doc libcxx/{CREDITS.TXT,LICENSE.TXT,TODO.TXT}
%attr(755,root,root) %{_libdir}/libc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++.so
%{_libdir}/libc++experimental.a
%dir %{_includedir}/c++
%{_includedir}/c++/v1

%files static
%defattr(644,root,root,755)
%{_libdir}/libc++.a
