Name:		texlive-margbib
Version:	15878
Release:	1
Summary:	Display bibitem tags in the margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/margbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines the 'thebibliography' environment to
place the citation key into the margin.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/margbib/margbib.sty
%doc %{_texmfdistdir}/doc/latex/margbib/margbib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/margbib/margbib.dtx
%doc %{_texmfdistdir}/source/latex/margbib/margbib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
