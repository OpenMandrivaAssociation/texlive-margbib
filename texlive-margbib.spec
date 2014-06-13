# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/margbib
# catalog-date 2008-09-23 13:30:27 +0200
# catalog-license gpl
# catalog-version 1.0c
Name:		texlive-margbib
Version:	1.0c
Release:	7
Summary:	Display bibitem tags in the margins
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/margbib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/margbib.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-2
+ Revision: 753737
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 718954
- texlive-margbib
- texlive-margbib
- texlive-margbib
- texlive-margbib

