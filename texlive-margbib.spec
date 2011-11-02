Name:		texlive-margbib
Version:	1.0c
Release:	1
Summary:	Display bibitem tags in the margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/margbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package redefines the 'thebibliography' environment to
place the citation key into the margin.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
