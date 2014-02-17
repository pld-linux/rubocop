#
# Conditional build:
%bcond_with	tests		# build without tests

Summary:	A robust Ruby code analyzer, based on the community Ruby style guide
Name:		rubocop
Version:	0.18.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	a265af5e5e3272e03c854b3c1635770c
Patch0:		rpmpath.patch
URL:		http://github.com/bbatsov/rubocop
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-rake < 11
BuildRequires:	ruby-rake >= 10.1
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.14
BuildRequires:	ruby-simplecov < 1
BuildRequires:	ruby-simplecov >= 0.7
BuildRequires:	ruby-yard < 1
BuildRequires:	ruby-yard >= 0.8
%endif
Requires:	ruby-json < 2
Requires:	ruby-json >= 1.7.7
Requires:	ruby-parser < 2.2
Requires:	ruby-parser >= 2.1.3
Requires:	ruby-powerpack < 0.1
Requires:	ruby-powerpack >= 0.0.6
Requires:	ruby-rainbow < 3.0
Requires:	ruby-rainbow >= 1.99.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatic Ruby code style checking tool. Aims to enforce the
community-driven Ruby Style Guide.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a config $RPM_BUILD_ROOT%{ruby_vendorlibdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rubocop
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}