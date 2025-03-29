# TODO: libcxx and libunwind docs
Summary:	LibC++ - C++ standard library from LLVM project
Summary(pl.UTF-8):	LibC++ - biblioteka standardowa C++ z projektu LLVM
Name:		llvm-libcxx
Version:	19.1.7
Release:	1
License:	MIT or BSD-like
Group:		Libraries
#Source0Download: https://github.com/llvm/llvm-project/releases/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxx-%{version}.src.tar.xz
# Source0-md5:	82dad4d1be8d7390f05ebcf65e19fbdc
#Source1Download: https://github.com/llvm/llvm-project/releases/
Source1:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxxabi-%{version}.src.tar.xz
# Source1-md5:	abbd3e2df635e1df5d90b507ecac141b
#Source2Download: https://github.com/llvm/llvm-project/releases/
Source2:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libunwind-%{version}.src.tar.xz
# Source2-md5:	32e100deacedceebab60772edf5d379a
#Source3Download: https://github.com/llvm/llvm-project/releases/
Source3:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/cmake-%{version}.src.tar.xz
# Source3-md5:	52b5249a06305e19c3bdae2e972c99c3
Source4:	https://github.com/llvm/llvm-project/raw/llvmorg-%{version}/runtimes/cmake/Modules/HandleFlags.cmake
# Source4-md5:	fd2dadedcdd386d8fa40753667c1f841
Source5:	https://github.com/llvm/llvm-project/raw/llvmorg-%{version}/runtimes/cmake/Modules/WarningFlags.cmake
# Source5-md5:	892fda2cd869e0a03c82db3c8f7ac8a4
URL:		https://libcxx.llvm.org/
# or gcc 10+
BuildRequires:	clang >= %{version}
BuildRequires:	cmake >= 3.20.0
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	llvm-libcxxabi = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libc++ is a new implementation of the C++ standard library, targeting
C++11 and above.

%description -l pl.UTF-8
libc++ to nowa implementacja biblioteki standardowej C++ ze wskazaniem
na standard C++11 i nowsze.

%package devel
Summary:	Header files of LLVM LibC++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LLVM LibC++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	llvm-libcxxabi-devel = %{version}-%{release}

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

%package -n llvm-libcxxabi
Summary:	libc++abi - C++ standard library support from LLVM project
Summary(pl.UTF-8):	libc++abi - wsparcie dla biblioteki standardowej C++ z projektu LLVM
Group:		Libraries
URL:		https://libcxxabi.llvm.org/

%description -n llvm-libcxxabi
libc++abi is a new implementation of low level support for a standard
C++ library.

%description -n llvm-libcxxabi -l pl.UTF-8
libc++abi to nowa implementacja niskopoziomowego wsparcia dla
biblioteki standardowej C++.

%package -n llvm-libcxxabi-devel
Summary:	Development files for LLVM libc++abi library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki LLVM libc++abi
Group:		Development/Libraries
URL:		https://libcxxabi.llvm.org/
Requires:	llvm-libcxxabi = %{version}-%{release}

%description -n llvm-libcxxabi-devel
Development files for LLVM libc++abi library.

%description -n llvm-libcxxabi-devel -l pl.UTF-8
Pliki programistyczne biblioteki LLVM libc++abi.

%package -n llvm-libcxxabi-static
Summary:	Static LLVM libc++abi library
Summary(pl.UTF-8):	Statyczna biblioteka LLVM libc++abi
Group:		Development/Libraries
URL:		https://libcxxabi.llvm.org/
Requires:	llvm-libcxxabi-devel = %{version}-%{release}

%description -n llvm-libcxxabi-static
Static LLVM libc++abi library.

%description -n llvm-libcxxabi-static -l pl.UTF-8
Statyczna biblioteka LLVM libc++abi.

%package -n llvm-libunwind
Summary:	LLVM libunwind implementation
Summary(pl.UTF-8):	Implementacja biblioteki libunwind z projektu LLVM
Group:		Libraries

%description -n llvm-libunwind
LLVM libunwind implementation.

%description -n llvm-libunwind -l pl.UTF-8
Implementacja biblioteki libunwind z projektu LLVM.

%package -n llvm-libunwind-devel
Summary:	Header file for LLVM libunwind implementation
Summary(pl.UTF-8):	Plik nagłówkowy implementacji LLVM libunwind
Group:		Development/Libraries
Requires:	llvm-libunwind = %{version}-%{release}

%description -n llvm-libunwind-devel
Header file for LLVM libunwind implementation.

%description -n llvm-libunwind-devel -l pl.UTF-8
Plik nagłówkowy implementacji LLVM libunwind.

%package -n llvm-libunwind-static
Summary:	Static LLVM libunwind library
Summary(pl.UTF-8):	Statyczna biblioteka LLVM libunwind
Group:		Development/Libraries
Requires:	llvm-libunwind-devel = %{version}-%{release}

%description -n llvm-libunwind-static
Static LLVM libunwind library.

%description -n llvm-libunwind-static -l pl.UTF-8
Statyczna biblioteka LLVM libunwind.

%prep
%setup -q -c -a1 -a2 -a3

install -d runtimes
%{__mv} libcxx-%{version}.src libcxx
%{__mv} libcxxabi-%{version}.src libcxxabi
%{__mv} libunwind-%{version}.src libunwind
%{__mv} cmake-%{version}.src runtimes/cmake
cp -p %{SOURCE4} %{SOURCE5} runtimes/cmake/Modules

cat >CMakeLists.txt <<EOF
cmake_minimum_required(VERSION 3.20.0)
project(Runtimes C CXX ASM)
add_subdirectory(libcxxabi)
add_subdirectory(libcxx)
add_subdirectory(libunwind)
EOF

%build
%if %{without gnu}
# requires C++20 compiler (clang ? or gcc 10+)
%define	__cc		clang
%define	__cxx		clang++
# not supported by clang
%define	filterout	-Werror=trampolines
%endif
libsubdir=%{_lib}
%cmake -B build \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON \
	-DLIBCXX_ENABLE_ABI_LINKER_SCRIPT=ON \
	-DLIBCXX_INCLUDE_BENCHMARKS=OFF \
	-DLIBCXX_LIBDIR_SUFFIX="${libsubdir#lib}" \
	-DLIBCXXABI_LIBDIR_SUFFIX="${libsubdir#lib}" \
	-DLIBUNWIND_INSTALL_INCLUDE_DIR=%{_includedir}/llvm-libunwind \
	-DLIBUNWIND_LIBDIR_SUFFIX="${libsubdir#lib}" \
	-DLLVM_ENABLE_RUNTIMES="libcxx;libcxxabi;libunwind" \
	-DPython3_EXECUTABLE=%{__python3}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# allow parallel installation with libunwind
install -d $RPM_BUILD_ROOT%{_libdir}/llvm-libunwind
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunwind.so
ln -snf ../$(basename $RPM_BUILD_ROOT%{_libdir}/libunwind.so.*.*) $RPM_BUILD_ROOT%{_libdir}/llvm-libunwind/libunwind.so
%{__mv} $RPM_BUILD_ROOT%{_libdir}/libunwind.a $RPM_BUILD_ROOT%{_libdir}/llvm-libunwind

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n llvm-libcxxabi -p /sbin/ldconfig
%postun	-n llvm-libcxxabi -p /sbin/ldconfig

%post	-n llvm-libunwind -p /sbin/ldconfig
%postun	-n llvm-libunwind -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc libcxx/{CREDITS.TXT,LICENSE.TXT,TODO.TXT}
%attr(755,root,root) %{_libdir}/libc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++.so
%{_libdir}/libc++experimental.a
%{_libdir}/libc++.modules.json
%{_includedir}/c++/v1/*
%exclude %{_includedir}/c++/v1/cxxabi.h
%exclude %{_includedir}/c++/v1/__cxxabi_config.h
%{_datadir}/libc++

%files static
%defattr(644,root,root,755)
%{_libdir}/libc++.a

%files -n llvm-libcxxabi
%defattr(644,root,root,755)
%doc libcxxabi/{CREDITS.TXT,LICENSE.TXT}
%attr(755,root,root) %{_libdir}/libc++abi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++abi.so.1

%files -n llvm-libcxxabi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++abi.so
%dir %{_includedir}/c++
%dir %{_includedir}/c++/v1
%{_includedir}/c++/v1/cxxabi.h
%{_includedir}/c++/v1/__cxxabi_config.h

%files -n llvm-libcxxabi-static
%defattr(644,root,root,755)
%{_libdir}/libc++abi.a

%files -n llvm-libunwind
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunwind.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libunwind.so.1

%files -n llvm-libunwind-devel
%defattr(644,root,root,755)
%doc libunwind/LICENSE.TXT
%dir %{_libdir}/llvm-libunwind
%attr(755,root,root) %{_libdir}/llvm-libunwind/libunwind.so
%{_includedir}/llvm-libunwind

%files -n llvm-libunwind-static
%defattr(644,root,root,755)
%{_libdir}/llvm-libunwind/libunwind.a
