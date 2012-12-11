# Generated from appraisal-0.1.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	appraisal

Summary:	Find out what your Ruby gems are worth
Name:		rubygem-%{rbname}

Version:	0.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/thoughtbot/appraisal
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called
"appraisals."

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f features

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/*.feature
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features/step_definitions
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/step_definitions/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/features/support
%{ruby_gemdir}/gems/%{rbname}-%{version}/features/support/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/appraisal
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/appraisal/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}



%changelog
* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1-1
+ Revision: 644376
- imported package rubygem-appraisal


* Sun Mar 13 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1-1
- Initial package
