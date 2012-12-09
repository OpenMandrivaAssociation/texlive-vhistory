# revision 19901
# category Package
# catalog-ctan /macros/latex/contrib/vhistory
# catalog-date 2010-07-19 00:40:21 +0200
# catalog-license lppl1.2
# catalog-version 1.5
Name:		texlive-vhistory
Version:	1.5
Release:	2
Summary:	Support for creating a change log
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vhistory
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vhistory.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Vhistory simplifies the creation of a history of versions of a
document. You can easily extract information like the current
version of a list of authors from that history. It helps you to
get consistent documents. The package sets, which is used by
vhistory, allows you to use sets containing text. You can use
the usual operations to create the union of sets or the
intersection of sets etc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vhistory/sets.sty
%{_texmfdistdir}/tex/latex/vhistory/vhistory.sty
%doc %{_texmfdistdir}/doc/latex/vhistory/CHANGES
%doc %{_texmfdistdir}/doc/latex/vhistory/README
%doc %{_texmfdistdir}/doc/latex/vhistory/README.doc
%doc %{_texmfdistdir}/doc/latex/vhistory/de_beispiel.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_einleitung.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_sets.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/de_vhistory.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_example.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_introduction.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_sets.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/en_vhistory.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/hyperref.cfg
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_set_example.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_set_example.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_de.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_de.tex
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_en.pdf
%doc %{_texmfdistdir}/doc/latex/vhistory/vh_sets_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5-2
+ Revision: 757422
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5-1
+ Revision: 719889
- texlive-vhistory
- texlive-vhistory
- texlive-vhistory

